#!/usr/bin/env python3
"""
Extract code facts from a repository for keyword-agnostic logic queries.

Parses source files to extract:
- Functions (name, parameters, calls, reads, writes)
- Classes (name, methods, inheritance)
- Data flows (where data originates and transforms)
- Type hierarchies (interfaces, implementations)
- Import relationships

Outputs JSON fact database for query_code_facts.py

Usage:
    python extract_code_facts.py /path/to/repo --output facts.json
    python extract_code_facts.py /path/to/repo --include "*.ts,*.js" --exclude "node_modules/*"

Requirements:
    pip install tree-sitter tree-sitter-python tree-sitter-javascript tree-sitter-typescript
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    from tree_sitter import Language, Parser, TreeCursor
    HAS_TREE_SITTER = True
except ImportError:
    HAS_TREE_SITTER = False
    print("Warning: tree-sitter not installed. Using regex fallback (less accurate).")
    print("Install: pip install tree-sitter tree-sitter-python tree-sitter-javascript tree-sitter-typescript")


# Language file extensions
LANGUAGE_MAP = {
    '.py': 'python',
    '.js': 'javascript',
    '.ts': 'typescript',
    '.tsx': 'tsx',
    '.jsx': 'javascript',
    '.java': 'java',
    '.go': 'go',
    '.rs': 'rust',
}


class CodeFactExtractor:
    """Extracts facts from source code using tree-sitter or regex fallback."""
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.facts = {
            'functions': [],
            'classes': [],
            'data_flows': [],
            'type_hierarchies': [],
            'imports': [],
            'files': [],
        }
        self.id_counter = 0
        self.parsers = {}
        
        if HAS_TREE_SITTER:
            self._init_parsers()
    
    def _init_parsers(self):
        """Initialize tree-sitter parsers for supported languages."""
        try:
            import tree_sitter_python as tspython
            import tree_sitter_javascript as tsjs
            import tree_sitter_typescript as tsts
            
            self.parsers['python'] = Parser(Language(tspython.language()))
            self.parsers['javascript'] = Parser(Language(tsjs.language()))
            self.parsers['typescript'] = Parser(Language(tsts.language()))
        except ImportError as e:
            print(f"Warning: Some language parsers not available: {e}")
    
    def _next_id(self, prefix: str) -> str:
        """Generate unique ID for extracted entities."""
        self.id_counter += 1
        return f"{prefix}_{self.id_counter:04d}"
    
    def extract_file(self, file_path: Path) -> Dict[str, Any]:
        """Extract facts from a single file."""
        ext = file_path.suffix
        language = LANGUAGE_MAP.get(ext)
        
        if not language:
            return {}
        
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return {}
        
        # Use tree-sitter if available, else regex
        if HAS_TREE_SITTER and language in self.parsers:
            return self._extract_with_treesitter(file_path, content, language)
        else:
            return self._extract_with_regex(file_path, content, language)
    
    def _extract_with_treesitter(self, file_path: Path, content: str, language: str) -> Dict[str, Any]:
        """Extract facts using tree-sitter AST parsing."""
        parser = self.parsers.get(language)
        if not parser:
            return self._extract_with_regex(file_path, content, language)
        
        tree = parser.parse(content.encode())
        root = tree.root_node
        
        facts = {
            'functions': [],
            'classes': [],
            'imports': [],
        }
        
        def walk(node, parent=None):
            # Extract functions
            if node.type in ('function_definition', 'function_declaration', 'method_definition'):
                func_fact = self._extract_function(node, file_path, content)
                if func_fact:
                    facts['functions'].append(func_fact)
            
            # Extract classes
            elif node.type in ('class_definition', 'class_declaration'):
                class_fact = self._extract_class(node, file_path, content)
                if class_fact:
                    facts['classes'].append(class_fact)
            
            # Extract imports
            elif node.type in ('import_statement', 'import_declaration', 'import_from_statement'):
                imp_fact = self._extract_import(node, file_path, content)
                if imp_fact:
                    facts['imports'].append(imp_fact)
            
            for child in node.children:
                walk(child, node)
        
        walk(root)
        return facts
    
    def _extract_function(self, node, file_path: Path, content: str) -> Optional[Dict]:
        """Extract function facts from AST node."""
        func_id = self._next_id('func')
        
        # Get function name
        name_node = None
        for child in node.children:
            if child.type in ('identifier', 'property_identifier'):
                name_node = child
                break
        
        name = name_node.text.decode() if name_node else '<anonymous>'
        
        # Get parameters
        params = []
        for child in node.children:
            if child.type in ('parameters', 'formal_parameters'):
                for param in child.children:
                    if param.type in ('identifier', 'pattern'):
                        params.append(param.text.decode())
        
        # Extract body for calls, reads, writes
        body = None
        for child in node.children:
            if child.type in ('block', 'statement_block', 'function_body'):
                body = child
                break
        
        calls = []
        reads = []
        writes = []
        
        if body:
            calls = self._extract_calls(body, content)
            reads, writes = self._extract_data_access(body, content)
        
        return {
            'id': func_id,
            'name': name,
            'file': str(file_path.relative_to(self.repo_path)),
            'line': node.start_point[0] + 1,
            'parameters': params,
            'calls': calls,
            'reads': reads,
            'writes': writes,
            'language': LANGUAGE_MAP.get(file_path.suffix, 'unknown'),
        }
    
    def _extract_class(self, node, file_path: Path, content: str) -> Optional[Dict]:
        """Extract class facts from AST node."""
        class_id = self._next_id('class')
        
        # Get class name
        name = '<anonymous>'
        for child in node.children:
            if child.type == 'identifier':
                name = child.text.decode()
                break
        
        # Get methods
        methods = []
        extends = None
        implements = []
        
        for child in node.children:
            if child.type in ('class_body', 'body'):
                for member in child.children:
                    if member.type in ('method_definition', 'function_definition'):
                        method_name = None
                        for mchild in member.children:
                            if mchild.type in ('identifier', 'property_identifier'):
                                method_name = mchild.text.decode()
                                break
                        if method_name:
                            methods.append(method_name)
            
            elif child.type == 'extends_clause':
                for echild in child.children:
                    if echild.type == 'identifier':
                        extends = echild.text.decode()
            
            elif child.type == 'implements_clause':
                for ichild in child.children:
                    if ichild.type == 'identifier':
                        implements.append(ichild.text.decode())
        
        return {
            'id': class_id,
            'name': name,
            'file': str(file_path.relative_to(self.repo_path)),
            'line': node.start_point[0] + 1,
            'methods': methods,
            'extends': extends,
            'implements': implements,
        }
    
    def _extract_import(self, node, file_path: Path, content: str) -> Optional[Dict]:
        """Extract import facts."""
        source = None
        names = []
        
        for child in node.children:
            if child.type == 'string_fragment':
                source = child.text.decode()
            elif child.type in ('identifier', 'import_specifier'):
                names.append(child.text.decode())
        
        if source:
            return {
                'file': str(file_path.relative_to(self.repo_path)),
                'source': source,
                'names': names,
                'line': node.start_point[0] + 1,
            }
        return None
    
    def _extract_calls(self, node, content: str) -> List[str]:
        """Extract function calls from a node."""
        calls = []
        
        def walk_calls(n):
            if n.type == 'call_expression':
                func_node = n.children[0] if n.children else None
                if func_node:
                    if func_node.type == 'identifier':
                        calls.append(func_node.text.decode())
                    elif func_node.type == 'member_expression':
                        # object.method
                        text = func_node.text.decode()
                        calls.append(text)
            
            for child in n.children:
                walk_calls(child)
        
        walk_calls(node)
        return list(set(calls))
    
    def _extract_data_access(self, node, content: str) -> Tuple[List[str], List[str]]:
        """Extract data reads and writes."""
        reads = []
        writes = []
        
        def walk_access(n, in_assignment=False):
            # Detect writes (assignments)
            if n.type in ('assignment_expression', 'assignment_pattern'):
                left = n.children[0] if n.children else None
                if left:
                    text = left.text.decode()
                    writes.append(text)
                # Continue walking right side as read
                if len(n.children) > 1:
                    walk_access(n.children[1], False)
            
            # Detect member access as reads
            elif n.type == 'member_expression' and not in_assignment:
                text = n.text.decode()
                reads.append(text)
            
            # Detect variable reads
            elif n.type == 'identifier' and not in_assignment:
                reads.append(n.text.decode())
            
            for child in n.children:
                walk_access(child, in_assignment)
        
        walk_access(node)
        return list(set(reads)), list(set(writes))
    
    def _extract_with_regex(self, file_path: Path, content: str, language: str) -> Dict[str, Any]:
        """Fallback regex-based extraction (less accurate but works without tree-sitter)."""
        facts = {
            'functions': [],
            'classes': [],
            'imports': [],
        }
        
        lines = content.split('\n')
        
        # Extract functions (language-specific patterns)
        if language in ('javascript', 'typescript', 'tsx', 'jsx'):
            # Match: function name(...) or const name = (...) =>
            func_pattern = r'(?:function\s+(\w+)|const\s+(\w+)\s*=\s*(?:async\s*)?(?:\([^)]*\)\s*=>|function)|(\w+)\s*\([^)]*\)\s*\{)'
            for i, line in enumerate(lines, 1):
                matches = re.finditer(func_pattern, line)
                for match in matches:
                    name = match.group(1) or match.group(2) or match.group(3)
                    if name:
                        facts['functions'].append({
                            'id': self._next_id('func'),
                            'name': name,
                            'file': str(file_path.relative_to(self.repo_path)),
                            'line': i,
                            'parameters': [],  # Would need deeper parsing
                            'calls': [],
                            'reads': [],
                            'writes': [],
                            'language': language,
                            'extraction_method': 'regex',
                        })
        
        elif language == 'python':
            # Match: def name(...) or async def name(...)
            func_pattern = r'(?:async\s+)?def\s+(\w+)\s*\('
            for i, line in enumerate(lines, 1):
                match = re.search(func_pattern, line)
                if match:
                    facts['functions'].append({
                        'id': self._next_id('func'),
                        'name': match.group(1),
                        'file': str(file_path.relative_to(self.repo_path)),
                        'line': i,
                        'parameters': [],
                        'calls': [],
                        'reads': [],
                        'writes': [],
                        'language': language,
                        'extraction_method': 'regex',
                    })
        
        # Extract classes
        if language in ('javascript', 'typescript'):
            class_pattern = r'class\s+(\w+)(?:\s+extends\s+(\w+))?'
        elif language == 'python':
            class_pattern = r'class\s+(\w+)(?:\([^)]*\))?:'
        else:
            class_pattern = r'class\s+(\w+)'
        
        for i, line in enumerate(lines, 1):
            match = re.search(class_pattern, line)
            if match:
                extends = match.group(2) if len(match.groups()) > 1 and match.group(2) else None
                facts['classes'].append({
                    'id': self._next_id('class'),
                    'name': match.group(1),
                    'file': str(file_path.relative_to(self.repo_path)),
                    'line': i,
                    'methods': [],
                    'extends': extends,
                    'implements': [],
                    'extraction_method': 'regex',
                })
        
        # Extract imports
        if language in ('javascript', 'typescript'):
            import_patterns = [
                r"import\s+.*?\s+from\s+['\"]([^'\"]+)['\"]",
                r"import\s+['\"]([^'\"]+)['\"]",
            ]
        elif language == 'python':
            import_patterns = [
                r'import\s+(\w+)',
                r'from\s+(\S+)\s+import',
            ]
        else:
            import_patterns = []
        
        for i, line in enumerate(lines, 1):
            for pattern in import_patterns:
                matches = re.finditer(pattern, line)
                for match in matches:
                    facts['imports'].append({
                        'file': str(file_path.relative_to(self.repo_path)),
                        'source': match.group(1),
                        'names': [],
                        'line': i,
                        'extraction_method': 'regex',
                    })
        
        return facts
    
    def extract_repo(self, include_patterns: List[str] = None, 
                     exclude_patterns: List[str] = None) -> Dict[str, Any]:
        """Extract facts from entire repository."""
        include_patterns = include_patterns or ['*']
        exclude_patterns = exclude_patterns or [
            'node_modules', '.git', 'dist', 'build', 
            '__pycache__', '*.min.js', '*.bundle.js'
        ]
        
        files_processed = 0
        errors = []
        
        for root, dirs, files in os.walk(self.repo_path):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not any(ex in d for ex in exclude_patterns)]
            
            for file in files:
                file_path = Path(root) / file
                
                # Check include patterns
                if not any(self._match_pattern(file, p) for p in include_patterns):
                    continue
                
                # Check exclude patterns
                if any(self._match_pattern(str(file_path), p) for p in exclude_patterns):
                    continue
                
                # Check if language is supported
                ext = file_path.suffix
                if ext not in LANGUAGE_MAP:
                    continue
                
                try:
                    file_facts = self.extract_file(file_path)
                    
                    # Merge into main facts
                    for key in ['functions', 'classes', 'imports']:
                        self.facts[key].extend(file_facts.get(key, []))
                    
                    self.facts['files'].append({
                        'path': str(file_path.relative_to(self.repo_path)),
                        'language': LANGUAGE_MAP.get(ext, 'unknown'),
                    })
                    
                    files_processed += 1
                    
                    if files_processed % 50 == 0:
                        print(f"Processed {files_processed} files...")
                        
                except Exception as e:
                    errors.append(f"{file_path}: {e}")
        
        # Build data flows from function reads/writes
        self._infer_data_flows()
        
        # Build type hierarchies
        self._infer_type_hierarchies()
        
        return {
            'facts': self.facts,
            'metadata': {
                'repo_path': str(self.repo_path),
                'files_processed': files_processed,
                'functions_extracted': len(self.facts['functions']),
                'classes_extracted': len(self.facts['classes']),
                'errors': errors[:10],  # First 10 errors
            }
        }
    
    def _match_pattern(self, text: str, pattern: str) -> bool:
        """Match text against glob pattern."""
        import fnmatch
        return fnmatch.fnmatch(text, pattern)
    
    def _infer_data_flows(self):
        """Infer data flows from function reads/writes."""
        # Simple: if function A writes X and function B reads X, there's a flow
        writes = defaultdict(list)  # var -> [func_ids]
        reads = defaultdict(list)     # var -> [func_ids]
        
        for func in self.facts['functions']:
            for write in func.get('writes', []):
                writes[write].append(func['id'])
            for read in func.get('reads', []):
                reads[read].append(func['id'])
        
        # Find connections
        flows = []
        for var, writer_ids in writes.items():
            reader_ids = reads.get(var, [])
            for writer in writer_ids:
                for reader in reader_ids:
                    if writer != reader:
                        flows.append({
                            'id': self._next_id('flow'),
                            'from': writer,
                            'to': reader,
                            'variable': var,
                            'type': 'data_flow',
                        })
        
        self.facts['data_flows'] = flows
    
    def _infer_type_hierarchies(self):
        """Infer type hierarchies from class extends/implements."""
        hierarchies = []
        
        # Group by base class
        by_base = defaultdict(list)
        for cls in self.facts['classes']:
            if cls.get('extends'):
                by_base[cls['extends']].append(cls['name'])
        
        for base, implementations in by_base.items():
            hierarchies.append({
                'id': self._next_id('hierarchy'),
                'base': base,
                'implementations': implementations,
                'type': 'inheritance',
            })
        
        self.facts['type_hierarchies'] = hierarchies


def main():
    parser = argparse.ArgumentParser(
        description='Extract code facts for keyword-agnostic logic queries'
    )
    parser.add_argument('repo_path', help='Path to code repository')
    parser.add_argument('--output', '-o', default='facts.json',
                        help='Output JSON file (default: facts.json)')
    parser.add_argument('--include', default='*',
                        help='Comma-separated include patterns (default: *)')
    parser.add_argument('--exclude', 
                        default='node_modules,.git,dist,build,__pycache__',
                        help='Comma-separated exclude patterns')
    
    args = parser.parse_args()
    
    include_patterns = [p.strip() for p in args.include.split(',')]
    exclude_patterns = [p.strip() for p in args.exclude.split(',')]
    
    print(f"Extracting facts from: {args.repo_path}")
    print(f"Include: {include_patterns}")
    print(f"Exclude: {exclude_patterns}")
    
    extractor = CodeFactExtractor(args.repo_path)
    result = extractor.extract_repo(include_patterns, exclude_patterns)
    
    # Write output
    output_path = Path(args.output)
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\nExtraction complete:")
    print(f"  Files processed: {result['metadata']['files_processed']}")
    print(f"  Functions: {result['metadata']['functions_extracted']}")
    print(f"  Classes: {result['metadata']['classes_extracted']}")
    print(f"  Output: {output_path.absolute()}")
    
    if result['metadata']['errors']:
        print(f"\nErrors (first {len(result['metadata']['errors'])}):")
        for err in result['metadata']['errors']:
            print(f"  - {err}")


if __name__ == '__main__':
    main()
