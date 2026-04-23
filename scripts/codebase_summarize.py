#!/usr/bin/env python3
"""
Hierarchical codebase summarization and semantic ranking for divide-and-conquer search.

Implements the Comprehend and Divide phases of the codebase-divide-conquer-search protocol.
Based on research from Meta-RAG (arXiv:2508.02611), GenLoc (arXiv:2508.00253),
AgentGroupChat-V2 (arXiv:2506.15451), RepoAudit (arXiv:2501.18160), and
Code-Craft / HCGS (arXiv:2504.08975).

Usage:
    # Phase 0: Generate summary tree
    python codebase_summarize.py /path/to/repo --output summaries.json

    # Phase 1: Query and rank candidate zones
    python codebase_summarize.py /path/to/repo \
        --query "Where is session validation logic?" \
        --output rankings.json \
        --top-k 5

Requirements:
    pip install tree-sitter tree-sitter-python tree-sitter-javascript tree-sitter-typescript sentence-transformers
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    from tree_sitter import Language, Parser
    HAS_TREE_SITTER = True
except ImportError:
    HAS_TREE_SITTER = False
    print("Warning: tree-sitter not installed. Using regex fallback (less accurate).", file=sys.stderr)
    print("Install: pip install tree-sitter tree-sitter-python tree-sitter-javascript tree-sitter-typescript", file=sys.stderr)

try:
    from sentence_transformers import SentenceTransformer, util
    HAS_EMBEDDINGS = True
except ImportError:
    HAS_EMBEDDINGS = False
    print("Warning: sentence-transformers not installed. Semantic ranking disabled.", file=sys.stderr)
    print("Install: pip install sentence-transformers", file=sys.stderr)


LANGUAGE_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.tsx': 'typescript',
    '.jsx': 'javascript',
}

SUMMARY_TEMPLATE = """# File Summary
# File: {path}
{classes}
{functions}
"""

CLASS_TEMPLATE = """- Class Summary: {name}
  - Summary: {summary}
  - Methods: {methods}"""

FUNC_TEMPLATE = """- Function Summary: {name}
  - Type declaration: {signature}
  - Summary: {summary}"""


def _init_parsers() -> Dict[str, Parser]:
    parsers = {}
    if not HAS_TREE_SITTER:
        return parsers
    try:
        import tree_sitter_python as tspython
        import tree_sitter_javascript as tsjs
        import tree_sitter_typescript as tsts
        parsers['python'] = Parser(Language(tspython.language()))
        parsers['javascript'] = Parser(Language(tsjs.language()))
        parsers['typescript'] = Parser(Language(tsts.language()))
    except ImportError as e:
        print(f"Warning: Some language parsers not available: {e}", file=sys.stderr)
    return parsers


class HierarchicalSummarizer:
    """Parses a codebase and generates hierarchical summaries."""

    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.parsers = _init_parsers()
        self.summaries: List[Dict[str, Any]] = []
        self.stats = {
            'files_processed': 0,
            'files_skipped': 0,
            'functions_extracted': 0,
            'classes_extracted': 0,
            'errors': [],
        }

    def summarize_repo(self, include_patterns: Optional[List[str]] = None,
                       exclude_patterns: Optional[List[str]] = None) -> Dict[str, Any]:
        include_patterns = include_patterns or ['*.py', '*.js', '*.ts', '*.tsx', '*.jsx']
        exclude_patterns = exclude_patterns or [
            'node_modules', '.git', 'dist', 'build',
            '__pycache__', '.venv', 'venv', '*.min.js'
        ]

        for root, dirs, files in os.walk(self.repo_path):
            dirs[:] = [d for d in dirs if not any(ex in d for ex in exclude_patterns)]

            for file in files:
                file_path = Path(root) / file
                if not any(file_path.match(p) for p in include_patterns):
                    continue
                if any(ex in str(file_path) for ex in exclude_patterns):
                    continue
                ext = file_path.suffix
                if ext not in LANGUAGE_MAP:
                    continue

                try:
                    summary = self._summarize_file(file_path)
                    if summary:
                        self.summaries.append(summary)
                        self.stats['files_processed'] += 1
                        self.stats['functions_extracted'] += len(summary.get('functions', []))
                        self.stats['classes_extracted'] += len(summary.get('classes', []))
                except Exception as e:
                    self.stats['errors'].append(f"{file_path}: {e}")

        return {
            'summaries': self.summaries,
            'stats': self.stats,
        }

    def _summarize_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
        except Exception:
            return None

        ext = file_path.suffix
        language = LANGUAGE_MAP.get(ext)
        if not language:
            return None

        if HAS_TREE_SITTER and language in self.parsers:
            return self._summarize_with_treesitter(file_path, content, language)
        else:
            return self._summarize_with_regex(file_path, content, language)

    def _summarize_with_treesitter(self, file_path: Path, content: str, language: str) -> Dict[str, Any]:
        parser = self.parsers.get(language)
        if not parser:
            return self._summarize_with_regex(file_path, content, language)

        tree = parser.parse(content.encode())
        root = tree.root_node

        functions = []
        classes = []
        imports = []

        def walk(node):
            if node.type in ('function_definition', 'function_declaration', 'method_definition', 'arrow_function'):
                func = self._extract_function(node, file_path, content)
                if func:
                    functions.append(func)
            elif node.type in ('class_definition', 'class_declaration'):
                cls = self._extract_class(node, file_path, content)
                if cls:
                    classes.append(cls)
            elif node.type in ('import_statement', 'import_declaration', 'import_from_statement'):
                imp = self._extract_import(node, content)
                if imp:
                    imports.append(imp)
            for child in node.children:
                walk(child)

        walk(root)

        rel_path = str(file_path.relative_to(self.repo_path))
        file_summary = self._generate_file_summary(rel_path, classes, functions, imports, content)

        return {
            'path': rel_path,
            'language': language,
            'file_summary': file_summary,
            'classes': classes,
            'functions': functions,
            'imports': imports,
        }

    def _extract_function(self, node, file_path: Path, content: str) -> Optional[Dict[str, Any]]:
        name_node = None
        for child in node.children:
            if child.type in ('identifier', 'property_identifier'):
                name_node = child
                break

        name = name_node.text.decode() if name_node else '<anonymous>'
        line = node.start_point[0] + 1

        params = []
        for child in node.children:
            if child.type in ('parameters', 'formal_parameters'):
                for param in child.children:
                    if param.type in ('identifier', 'pattern', 'shorthand_property_identifier_pattern'):
                        params.append(param.text.decode())

        signature = f"{name}({', '.join(params)})"
        body_text = content[node.start_byte:node.end_byte][:200].replace('\n', ' ')
        summary = f"Defined at line {line}. {body_text[:120]}..."

        return {
            'name': name,
            'line': line,
            'signature': signature,
            'summary': summary,
        }

    def _extract_class(self, node, file_path: Path, content: str) -> Optional[Dict[str, Any]]:
        name = '<anonymous>'
        for child in node.children:
            if child.type == 'identifier':
                name = child.text.decode()
                break

        methods = []
        extends = None
        for child in node.children:
            if child.type in ('class_body', 'body'):
                for member in child.children:
                    if member.type in ('method_definition', 'function_definition'):
                        for mchild in member.children:
                            if mchild.type in ('identifier', 'property_identifier'):
                                methods.append(mchild.text.decode())
                                break
            elif child.type == 'extends_clause':
                for echild in child.children:
                    if echild.type == 'identifier':
                        extends = echild.text.decode()
                        break

        line = node.start_point[0] + 1
        return {
            'name': name,
            'line': line,
            'summary': f"Class with methods: {', '.join(methods)}. Line {line}.",
            'methods': methods,
            'extends': extends,
        }

    def _extract_import(self, node, content: str) -> Optional[str]:
        for child in node.children:
            if child.type == 'string_fragment':
                return child.text.decode()
        return None

    def _generate_file_summary(self, path: str, classes: List[Dict], functions: List[Dict],
                               imports: List[str], content: str) -> str:
        first_lines = content[:300].replace('\n', ' ')
        class_summaries = []
        for cls in classes:
            class_summaries.append(CLASS_TEMPLATE.format(
                name=cls['name'],
                summary=cls['summary'],
                methods=', '.join(cls['methods'])
            ))

        func_summaries = []
        for func in functions:
            func_summaries.append(FUNC_TEMPLATE.format(
                name=func['name'],
                signature=func['signature'],
                summary=func['summary']
            ))

        return SUMMARY_TEMPLATE.format(
            path=path,
            classes='\n'.join(class_summaries) if class_summaries else '- No classes',
            functions='\n'.join(func_summaries) if func_summaries else '- No top-level functions',
        )

    def _summarize_with_regex(self, file_path: Path, content: str, language: str) -> Dict[str, Any]:
        rel_path = str(file_path.relative_to(self.repo_path))
        lines = content.split('\n')
        functions = []
        classes = []
        imports = []

        if language == 'python':
            func_re = re.compile(r'(?:async\s+)?def\s+(\w+)\s*\(([^)]*)\)')
            class_re = re.compile(r'class\s+(\w+)(?:\([^)]*\))?:')
            import_re = re.compile(r'^(?:import\s+(\S+)|from\s+(\S+)\s+import)')
        else:
            func_re = re.compile(r'(?:function\s+(\w+)|(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s*)?(?:\(([^)]*)\)\s*=>|function))')
            class_re = re.compile(r'class\s+(\w+)(?:\s+extends\s+(\w+))?')
            import_re = re.compile(r"import\s+.*?\s+from\s+['\"]([^'\"]+)['\"]")

        for i, line in enumerate(lines, 1):
            m = func_re.search(line)
            if m:
                name = m.group(1) or m.group(2)
                params = m.group(3) if len(m.groups()) >= 3 and m.group(3) is not None else ''
                functions.append({
                    'name': name,
                    'line': i,
                    'signature': f"{name}({params})",
                    'summary': f"Function defined at line {i} (regex-extracted).",
                })

            m = class_re.search(line)
            if m:
                classes.append({
                    'name': m.group(1),
                    'line': i,
                    'summary': f"Class defined at line {i} (regex-extracted).",
                    'methods': [],
                    'extends': m.group(2) if m.lastindex > 1 else None,
                })

            m = import_re.search(line)
            if m:
                imports.append(m.group(1) or m.group(2))

        return {
            'path': rel_path,
            'language': language,
            'file_summary': self._generate_file_summary(rel_path, classes, functions, imports, content),
            'classes': classes,
            'functions': functions,
            'imports': imports,
        }


class SemanticRanker:
    """Ranks summary nodes by cosine similarity to a query embedding."""

    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        self.model = None
        if HAS_EMBEDDINGS:
            try:
                self.model = SentenceTransformer(model_name)
            except Exception as e:
                print(f"Warning: Could not load embedding model: {e}", file=sys.stderr)

    def rank(self, summaries: List[Dict[str, Any]], query: str, top_k: int = 5,
             context_budget: int = 50000) -> Dict[str, Any]:
        if not self.model:
            raise RuntimeError("Embedding model not available. Install sentence-transformers.")

        nodes = []
        texts = []
        for file_summary in summaries:
            # File-level node
            nodes.append({
                'type': 'file',
                'path': file_summary['path'],
                'summary': file_summary['file_summary'],
            })
            texts.append(file_summary['file_summary'])

            # Class-level nodes
            for cls in file_summary.get('classes', []):
                text = f"Class {cls['name']} in {file_summary['path']}: {cls['summary']}"
                nodes.append({
                    'type': 'class',
                    'path': file_summary['path'],
                    'name': cls['name'],
                    'line': cls['line'],
                    'summary': text,
                })
                texts.append(text)

            # Function-level nodes
            for func in file_summary.get('functions', []):
                text = f"Function {func['name']} in {file_summary['path']}: {func['summary']}"
                nodes.append({
                    'type': 'function',
                    'path': file_summary['path'],
                    'name': func['name'],
                    'line': func['line'],
                    'summary': text,
                })
                texts.append(text)

        query_embedding = self.model.encode(query, convert_to_tensor=True)
        doc_embeddings = self.model.encode(texts, convert_to_tensor=True)
        similarities = util.cos_sim(query_embedding, doc_embeddings)[0].cpu().numpy()

        scored = [(float(sim), node) for sim, node in zip(similarities, nodes)]
        scored.sort(key=lambda x: x[0], reverse=True)

        # Partition top-K into non-overlapping zones by file path
        zones = []
        seen_files = set()
        for score, node in scored:
            if len(zones) >= top_k:
                break
            path = node['path']
            if path not in seen_files:
                zones.append({
                    'zone_id': len(zones) + 1,
                    'files': [path],
                    'top_nodes': [node],
                    'confidence': round(score, 4),
                })
                seen_files.add(path)
            else:
                # Add to existing zone for this file
                for zone in zones:
                    if path in zone['files']:
                        zone['top_nodes'].append(node)
                        zone['confidence'] = max(zone['confidence'], round(score, 4))
                        break

        # Merge adjacent single-file zones if total context fits budget
        # (simplified: keep as-is, agent handles context budget)
        return {
            'query': query,
            'total_nodes': len(nodes),
            'zones': zones,
            'all_ranked': [
                {'score': round(float(s), 4), 'node': n}
                for s, n in scored[:50]
            ],
        }


def main():
    parser = argparse.ArgumentParser(description='Hierarchical codebase summarization and semantic ranking')
    parser.add_argument('repo', help='Path to repository')
    parser.add_argument('--output', '-o', required=True, help='Output JSON file')
    parser.add_argument('--query', '-q', help='Search query for semantic ranking (enables Phase 1)')
    parser.add_argument('--top-k', '-k', type=int, default=5, help='Number of zones to return (default: 5)')
    parser.add_argument('--include', help='Comma-separated glob patterns (default: *.py,*.ts,*.js,*.tsx,*.jsx)')
    parser.add_argument('--exclude', help='Comma-separated exclude patterns')
    parser.add_argument('--model', default='all-MiniLM-L6-v2', help='Sentence-transformers model')
    parser.add_argument('--context-budget', type=int, default=50000, help='Max tokens per zone')
    args = parser.parse_args()

    include = args.include.split(',') if args.include else None
    exclude = args.exclude.split(',') if args.exclude else None

    summarizer = HierarchicalSummarizer(args.repo)
    result = summarizer.summarize_repo(include_patterns=include, exclude_patterns=exclude)

    if args.query:
        if not HAS_EMBEDDINGS:
            print("Error: --query requires sentence-transformers. Install it first.", file=sys.stderr)
            sys.exit(1)
        ranker = SemanticRanker(model_name=args.model)
        rankings = ranker.rank(result['summaries'], args.query, top_k=args.top_k, context_budget=args.context_budget)
        result['rankings'] = rankings

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Wrote {args.output}")
    print(f"Stats: {result['stats']}")
    if args.query and 'rankings' in result:
        print(f"Top zones: {[z['files'] for z in result['rankings']['zones']]}")


if __name__ == '__main__':
    main()
