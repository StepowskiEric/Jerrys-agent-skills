#!/usr/bin/env python3
"""
Query code facts using Datalog-style logic queries.

Executes logic queries against the fact database created by extract_code_facts.py.
Supports queries about:
- Call graphs (who calls what)
- Data flows (where data originates and transforms)
- Type hierarchies (implementations of interfaces)
- Structural patterns (functions matching criteria)

Usage:
    python query_code_facts.py facts.json --query "find(F) :- calls(F, 'validate')."
    python query_code_facts.py facts.json --query-file query.dl
    python query_code_facts.py facts.json --interactive

Query Syntax (Datalog subset):
    find(X) :- predicate1(X), predicate2(X, Y), not(predicate3(X)).
    
    Available predicates:
    - function(F), class(C), file(F)
    - calls(F, Target), called_by(F, Source)
    - reads(F, Data), writes(F, Data)
    - imports(F, Module)
    - extends(C, Parent), implements(C, Interface)
    - has_method(C, Method)
    - test_file(F), async(F)
    - path(Source, Target, Path)  # transitive call paths
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple


class FactDatabase:
    """In-memory fact database with index structures for efficient querying."""
    
    def __init__(self, facts_data: Dict):
        self.facts = facts_data.get('facts', facts_data)
        self.metadata = facts_data.get('metadata', {})
        
        # Build indexes
        self._build_indexes()
    
    def _build_indexes(self):
        """Build lookup indexes for efficient querying."""
        # By ID
        self.by_id = {}
        for func in self.facts.get('functions', []):
            self.by_id[func['id']] = func
        for cls in self.facts.get('classes', []):
            self.by_id[cls['id']] = cls
        
        # Call graph indexes
        self.calls_index = defaultdict(set)  # caller -> callees
        self.called_by_index = defaultdict(set)  # callee -> callers
        
        for func in self.facts.get('functions', []):
            caller = func['id']
            for callee in func.get('calls', []):
                # Try to resolve callee name to ID
                callee_ids = self._resolve_function_name(callee)
                for callee_id in callee_ids:
                    self.calls_index[caller].add(callee_id)
                    self.called_by_index[callee_id].add(caller)
        
        # Data flow indexes
        self.reads_index = defaultdict(set)  # var -> functions
        self.writes_index = defaultdict(set)  # var -> functions
        
        for func in self.facts.get('functions', []):
            for var in func.get('reads', []):
                self.reads_index[var].add(func['id'])
            for var in func.get('writes', []):
                self.writes_index[var].add(func['id'])
        
        # Type indexes
        self.implements_index = defaultdict(set)  # interface -> implementations
        self.extends_index = defaultdict(set)   # parent -> children
        
        for cls in self.facts.get('classes', []):
            if cls.get('extends'):
                self.extends_index[cls['extends']].add(cls['id'])
            for impl in cls.get('implements', []):
                self.implements_index[impl].add(cls['id'])
        
        # File index
        self.functions_by_file = defaultdict(list)
        for func in self.facts.get('functions', []):
            self.functions_by_file[func.get('file', '')].append(func['id'])
    
    def _resolve_function_name(self, name: str) -> List[str]:
        """Resolve a function name to IDs (handles simple name matching)."""
        ids = []
        for func in self.facts.get('functions', []):
            if func['name'] == name:
                ids.append(func['id'])
            # Also match method syntax: Class.method
            if '.' in name:
                parts = name.split('.')
                if len(parts) == 2 and func['name'] == parts[1]:
                    # Could be this method
                    ids.append(func['id'])
        return ids
    
    def get_function(self, func_id: str) -> Optional[Dict]:
        """Get function by ID."""
        return self.by_id.get(func_id)
    
    def get_transitive_calls(self, func_id: str, depth: int = 5) -> Set[str]:
        """Get all transitive callees (calls, calls of calls, etc)."""
        visited = set()
        frontier = {func_id}
        
        for _ in range(depth):
            new_frontier = set()
            for f in frontier:
                if f not in visited:
                    visited.add(f)
                    new_frontier.update(self.calls_index.get(f, set()))
            frontier = new_frontier
            if not frontier:
                break
        
        return visited - {func_id}
    
    def get_transitive_callers(self, func_id: str, depth: int = 5) -> Set[str]:
        """Get all transitive callers (who calls this, who calls them, etc)."""
        visited = set()
        frontier = {func_id}
        
        for _ in range(depth):
            new_frontier = set()
            for f in frontier:
                if f not in visited:
                    visited.add(f)
                    new_frontier.update(self.called_by_index.get(f, set()))
            frontier = new_frontier
            if not frontier:
                break
        
        return visited - {func_id}
    
    def find_path(self, source: str, target: str, max_depth: int = 5) -> Optional[List[str]]:
        """Find a call path from source to target."""
        # BFS
        from collections import deque
        
        queue = deque([(source, [source])])
        visited = {source}
        
        while queue and len(queue[0][1]) <= max_depth:
            current, path = queue.popleft()
            
            if current == target and len(path) > 1:
                return path
            
            for neighbor in self.calls_index.get(current, set()):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None


class DatalogQueryEngine:
    """Simple Datalog query engine for code facts."""
    
    def __init__(self, db: FactDatabase):
        self.db = db
        self.predicates = self._build_predicates()
    
    def _build_predicates(self) -> Dict:
        """Build predicate functions."""
        return {
            # Basic type predicates
            'function': lambda x: x in self.db.by_id and 'parameters' in self.db.by_id[x],
            'class': lambda x: x in self.db.by_id and 'methods' in self.db.by_id[x],
            'file': lambda x: isinstance(x, str) and any(x == f['path'] for f in self.db.facts.get('files', [])),
            
            # Call graph
            'calls': self._pred_calls,
            'called_by': self._pred_called_by,
            'calls+': lambda x, y: y in self.db.get_transitive_calls(x),
            'called_by+': lambda x, y: y in self.db.get_transitive_callers(x),
            
            # Data access
            'reads': lambda f, data: f in self.db.reads_index.get(data, set()),
            'writes': lambda f, data: f in self.db.writes_index.get(data, set()),
            'touches': lambda f, data: f in (self.db.reads_index.get(data, set()) | 
                                             self.db.writes_index.get(data, set())),
            
            # Type hierarchy
            'extends': lambda c, parent: c in self.db.extends_index.get(parent, set()),
            'implements': lambda c, iface: c in self.db.implements_index.get(iface, set()),
            'has_method': self._pred_has_method,
            
            # Module
            'imports': self._pred_imports,
            'imported_by': lambda m, f: self._pred_imports(f, m),
            
            # Properties
            'test_file': self._pred_test_file,
            'async': self._pred_async,
            'method': self._pred_method,
            'exported': self._pred_exported,
            
            # Path finding
            'path': self._pred_path,
            'reaches': lambda x, y: self.db.find_path(x, y) is not None,
        }
    
    def _pred_calls(self, caller: str, callee: str) -> bool:
        """Check if caller calls callee."""
        # Try as ID first
        if callee in self.db.calls_index.get(caller, set()):
            return True
        # Try as name
        callee_ids = self.db._resolve_function_name(callee)
        return any(cid in self.db.calls_index.get(caller, set()) for cid in callee_ids)
    
    def _pred_called_by(self, callee: str, caller: str) -> bool:
        """Check if callee is called by caller."""
        return self._pred_calls(caller, callee)
    
    def _pred_has_method(self, cls: str, method: str) -> bool:
        """Check if class has method."""
        cls_data = self.db.by_id.get(cls)
        if cls_data:
            return method in cls_data.get('methods', [])
        return False
    
    def _pred_imports(self, func_or_file: str, module: str) -> bool:
        """Check if function/file imports module."""
        # Check if it's a file
        for imp in self.db.facts.get('imports', []):
            if imp.get('file') == func_or_file:
                if module in imp.get('source', '') or module in imp.get('names', []):
                    return True
        
        # Check function's file
        func_data = self.db.by_id.get(func_or_file)
        if func_data:
            file = func_data.get('file', '')
            return self._pred_imports(file, module)
        
        return False
    
    def _pred_test_file(self, x: str) -> bool:
        """Check if file or function is in a test file."""
        if isinstance(x, str):
            # Check if it's a file path
            if 'test' in x.lower() or 'spec' in x.lower():
                return True
            # Check if it's a function
            func = self.db.by_id.get(x)
            if func:
                file = func.get('file', '')
                return 'test' in file.lower() or 'spec' in file.lower()
        return False
    
    def _pred_async(self, func_id: str) -> bool:
        """Check if function is async."""
        func = self.db.by_id.get(func_id)
        if func:
            # Check name or calls
            return (func['name'].startswith('async') or 
                    any('await' in str(c) or 'Promise' in str(c) 
                        for c in func.get('calls', [])))
        return False
    
    def _pred_method(self, func_id: str) -> bool:
        """Check if function is a method (belongs to a class)."""
        func = self.db.by_id.get(func_id)
        if func:
            # Check if any class has this as a method
            for cls in self.db.facts.get('classes', []):
                if func['name'] in cls.get('methods', []):
                    return True
        return False
    
    def _pred_exported(self, func_id: str) -> bool:
        """Check if function is exported (heuristic)."""
        func = self.db.by_id.get(func_id)
        if func:
            # Heuristic: exported if name doesn't start with _
            return not func['name'].startswith('_')
        return False
    
    def _pred_path(self, source: str, target: str, path_var: str) -> bool:
        """Check if path exists (path_var is a placeholder)."""
        # This is special - we return the actual path
        path = self.db.find_path(source, target)
        return path is not None
    
    def parse_query(self, query: str) -> Dict:
        """Parse a Datalog query."""
        # Simple parser for: find(X) :- pred1(X), pred2(X, Y), not(pred3(X)).
        query = query.strip()
        
        # Match find pattern
        match = re.match(r'find\((\w+)\)\s*:-\s*(.+)', query, re.DOTALL)
        if not match:
            raise ValueError(f"Invalid query format. Expected: find(X) :- pred1(X), ...")
        
        result_var = match.group(1)
        body = match.group(2)
        
        # Parse predicates
        predicates = []
        
        # Split by comma, but handle nested parentheses
        depth = 0
        current = ""
        for char in body:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif char == ',' and depth == 0:
                predicates.append(current.strip())
                current = ""
                continue
            current += char
        
        if current.strip():
            predicates.append(current.strip())
        
        return {
            'result_var': result_var,
            'predicates': predicates,
        }
    
    def execute_query(self, query: str) -> List[Dict]:
        """Execute a Datalog query."""
        parsed = self.parse_query(query)
        result_var = parsed['result_var']
        predicates = parsed['predicates']
        
        # Get candidate bindings
        candidates = self._get_candidates(result_var, predicates)
        
        # Filter by predicates
        results = []
        for candidate in candidates:
            if self._satisfies_predicates(candidate, result_var, predicates):
                results.append(self._enrich_result(candidate))
        
        return results
    
    def _get_candidates(self, result_var: str, predicates: List[str]) -> Set[str]:
        """Get candidate values for the result variable."""
        candidates = set()
        
        # Look for type constraints
        for pred in predicates:
            # Check for function(X), class(X), etc.
            match = re.match(r'(\w+)\((\w+)\)', pred)
            if match:
                pred_name = match.group(1)
                var = match.group(2)
                
                if var == result_var:
                    if pred_name == 'function':
                        candidates.update(f['id'] for f in self.db.facts.get('functions', []))
                    elif pred_name == 'class':
                        candidates.update(c['id'] for c in self.db.facts.get('classes', []))
                    elif pred_name == 'file':
                        candidates.update(f['path'] for f in self.db.facts.get('files', []))
        
        # If no type constraint, include all entities
        if not candidates:
            candidates.update(self.db.by_id.keys())
        
        return candidates
    
    def _satisfies_predicates(self, candidate: str, result_var: str, predicates: List[str]) -> bool:
        """Check if candidate satisfies all predicates."""
        # Build variable bindings
        bindings = {result_var: candidate}
        
        for pred in predicates:
            pred = pred.strip()
            
            # Handle not()
            if pred.startswith('not(') and pred.endswith(')'):
                inner = pred[4:-1]
                if self._eval_predicate(inner, bindings):
                    return False
                continue
            
            # Handle regular predicates
            if not self._eval_predicate(pred, bindings):
                return False
        
        return True
    
    def _eval_predicate(self, pred: str, bindings: Dict) -> bool:
        """Evaluate a single predicate."""
        # Parse predicate
        match = re.match(r'(\w+)\(([^)]+)\)', pred)
        if not match:
            return False
        
        pred_name = match.group(1)
        args_str = match.group(2)
        
        # Parse arguments
        args = [a.strip() for a in args_str.split(',')]
        
        # Resolve variables
        resolved_args = []
        for arg in args:
            if arg in bindings:
                resolved_args.append(bindings[arg])
            else:
                # Check if it's a string literal
                if (arg.startswith('"') and arg.endswith('"')) or \
                   (arg.startswith("'") and arg.endswith("'")):
                    resolved_args.append(arg[1:-1])
                else:
                    # It's a free variable - we need to handle this differently
                    # For now, treat as string
                    resolved_args.append(arg)
        
        # Get predicate function
        pred_func = self.predicates.get(pred_name)
        if not pred_func:
            return False
        
        # Call predicate
        try:
            if len(resolved_args) == 1:
                return pred_func(resolved_args[0])
            elif len(resolved_args) == 2:
                return pred_func(resolved_args[0], resolved_args[1])
            elif len(resolved_args) == 3:
                return pred_func(resolved_args[0], resolved_args[1], resolved_args[2])
            else:
                return False
        except Exception as e:
            print(f"Error evaluating {pred}: {e}")
            return False
    
    def _enrich_result(self, result_id: str) -> Dict:
        """Enrich result with full entity data."""
        entity = self.db.by_id.get(result_id)
        if entity:
            return {
                'id': result_id,
                'type': 'function' if 'parameters' in entity else 'class',
                **entity
            }
        
        # Might be a file path
        return {
            'id': result_id,
            'type': 'file',
            'path': result_id,
        }


def interactive_mode(engine: DatalogQueryEngine):
    """Run interactive query mode."""
    print("\nInteractive Query Mode")
    print("Type 'help' for examples, 'quit' to exit")
    print("-" * 50)
    
    while True:
        try:
            query = input("\nquery> ").strip()
            
            if query.lower() in ('quit', 'exit', 'q'):
                break
            
            if query.lower() == 'help':
                print_examples()
                continue
            
            if not query:
                continue
            
            results = engine.execute_query(query)
            
            print(f"\nFound {len(results)} results:")
            for i, r in enumerate(results[:10], 1):  # Show first 10
                print(f"\n{i}. {r.get('name', r.get('path', r['id']))}")
                print(f"   File: {r.get('file', 'N/A')}")
                if 'line' in r:
                    print(f"   Line: {r['line']}")
                
            if len(results) > 10:
                print(f"\n... and {len(results) - 10} more")
                
        except Exception as e:
            print(f"Error: {e}")


def print_examples():
    """Print example queries."""
    examples = [
        ("Find all functions", "find(F) :- function(F)."),
        ("Find functions that call 'validate'", "find(F) :- function(F), calls(F, 'validate')."),
        ("Find auth-related functions (keyword-agnostic)", 
         "find(F) :- function(F), touches(F, 'token'), touches(F, 'session'), not(test_file(F))."),
        ("Find functions that read from request and write to database",
         "find(F) :- reads(F, 'req'), writes(F, 'db'), not(test_file(F))."),
        ("Find implementations of an interface",
         "find(C) :- class(C), implements(C, 'AuthProvider')."),
        ("Find uncaught API calls",
         "find(F) :- calls(F, 'fetch'), not(test_file(F)), not(calls(F, 'catch'))."),
    ]
    
    print("\nExample Queries:")
    for desc, query in examples:
        print(f"\n{desc}")
        print(f"  {query}")


def main():
    parser = argparse.ArgumentParser(
        description='Query code facts using Datalog-style logic queries'
    )
    parser.add_argument('facts_file', help='JSON file with extracted facts')
    parser.add_argument('--query', '-q', help='Single query to execute')
    parser.add_argument('--query-file', '-f', help='File containing queries')
    parser.add_argument('--interactive', '-i', action='store_true',
                        help='Interactive query mode')
    parser.add_argument('--output', '-o', help='Output file for results (JSON)')
    parser.add_argument('--format', choices=['json', 'text'], default='text',
                        help='Output format')
    
    args = parser.parse_args()
    
    # Load facts
    with open(args.facts_file) as f:
        facts_data = json.load(f)
    
    db = FactDatabase(facts_data)
    engine = DatalogQueryEngine(db)
    
    print(f"Loaded facts from: {args.facts_file}")
    print(f"  Functions: {len(db.facts.get('functions', []))}")
    print(f"  Classes: {len(db.facts.get('classes', []))}")
    print(f"  Data flows: {len(db.facts.get('data_flows', []))}")
    
    # Interactive mode
    if args.interactive:
        interactive_mode(engine)
        return
    
    # Execute single query
    if args.query:
        print(f"\nExecuting: {args.query}")
        results = engine.execute_query(args.query)
        
        if args.format == 'json':
            output = {
                'query': args.query,
                'results': results,
                'count': len(results),
            }
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump(output, f, indent=2)
                print(f"Results written to: {args.output}")
            else:
                print(json.dumps(output, indent=2))
        else:
            print(f"\nFound {len(results)} results:")
            for i, r in enumerate(results, 1):
                print(f"\n{i}. {r.get('name', r.get('path', r['id']))}")
                print(f"   File: {r.get('file', 'N/A')}")
                if 'line' in r:
                    print(f"   Line: {r['line']}")
                if 'calls' in r and r['calls']:
                    print(f"   Calls: {', '.join(r['calls'][:5])}")
                if 'reads' in r and r['reads']:
                    print(f"   Reads: {', '.join(r['reads'][:3])}")
                if 'writes' in r and r['writes']:
                    print(f"   Writes: {', '.join(r['writes'][:3])}")
    
    # Execute queries from file
    elif args.query_file:
        with open(args.query_file) as f:
            queries = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        all_results = []
        for query in queries:
            print(f"\nExecuting: {query}")
            results = engine.execute_query(query)
            all_results.append({
                'query': query,
                'results': results,
                'count': len(results),
            })
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(all_results, f, indent=2)
            print(f"\nResults written to: {args.output}")
    
    else:
        print("\nNo query specified. Use --query, --query-file, or --interactive")
        print_examples()


if __name__ == '__main__':
    main()
