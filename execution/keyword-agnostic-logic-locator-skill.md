# Skill: Keyword-Agnostic Logic Locator

## Purpose

Find code by structural relationships and logical queries rather than name matching. Extracts program facts (call graphs, data flows, type hierarchies) into a queryable knowledge graph, then uses Datalog-style logic to locate code without relying on function names, file paths, or keywords.

Based on "Neurosymbolic Repo-level Code Localization" (arXiv:2604.16021) — addressing the "Keyword Shortcut" problem where agents rely on superficial lexical matching instead of genuine structural reasoning.

---

## When to Use

- Codebases where function/file names are unclear or misleading
- Finding code by "what it does" not "what it's called"
- Complex navigation: "Where does data X get transformed before reaching Y?"
- Cross-language codebases where naming conventions differ
- Legacy code with poor naming
- Any time `grep` returns too many false positives

**Don't use when:**
- You already know the exact file/function name
- The codebase is small and easily searchable
- You need full-text search (use regular search instead)

---

## Core Concept

**The Keyword Shortcut Problem:**
```
User asks: "Where is the authentication logic?"
Agent greps: "auth", "login", "authenticate"
Problem: 
  - Finds AuthService.ts (correct)
  - Also finds auth.test.ts, auth.types.ts, auth.mock.ts (noise)
  - Misses SessionManager.ts (also does auth, but named differently)
  - Misses middleware.ts (has auth logic, generic name)
```

**Logic-Based Alternative:**
```
Query: find(X) :- modifies(X, 'session'), validates(X, 'token')
Result: SessionManager.update(), middleware.verifyJWT() — regardless of names
```

**The Pipeline:**
```
Codebase → Fact Extractor → Knowledge Graph → Logic Query Engine → Results
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    KEYWORD-AGNOSTIC LOCATOR                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐        │
│  │   Extract    │───▶│   Store      │───▶│   Query      │        │
│  │   (Python)   │    │   (Graph)    │    │   (Datalog)  │        │
│  └──────────────┘    └──────────────┘    └──────────────┘        │
│         │                  │                  │                    │
│         ▼                  ▼                  ▼                    │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐        │
│  │  Call Graph  │    │  Nodes:      │    │  Logic       │        │
│  │  Data Flow   │    │  Functions   │    │  Rules       │        │
│  │  Types       │    │  Classes     │    │  Constraints │        │
│  │  Imports     │    │  Files       │    │  Filters     │        │
│  └──────────────┘    │  Relations   │    └──────────────┘        │
│                      └──────────────┘                            │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Fact Extraction

Run the Python extractor on your codebase:

```bash
python scripts/extract_code_facts.py /path/to/repo --output facts.json
```

**Extracted facts include:**

```json
{
  "functions": [
    {
      "id": "func_001",
      "name": "validateSession",
      "file": "/auth/session.ts",
      "line": 45,
      "parameters": ["token", "options"],
      "returns": "Session",
      "calls": ["parseJWT", "checkExpiry", "db.query"],
      "reads": ["req.headers", "process.env.JWT_SECRET"],
      "writes": ["req.session", "cache"],
      "imports": ["jsonwebtoken", "./db"]
    }
  ],
  "classes": [
    {
      "id": "class_001",
      "name": "SessionManager",
      "methods": ["create", "validate", "destroy"],
      "extends": "EventEmitter",
      "used_by": ["auth.middleware", "login.handler"]
    }
  ],
  "data_flows": [
    {
      "from": "req.headers.authorization",
      "to": "validateSession.token",
      "via": ["parseJWT"],
      "transformations": ["split", "verify"]
    }
  ],
  "type_hierarchies": [
    {
      "base": "AuthProvider",
      "implementations": ["JWTAuth", "OAuthProvider", "SessionAuth"]
    }
  ]
}
```

---

## Phase 2: Query Formulation

Write logic queries instead of text searches:

### Query Types

**1. Call Graph Queries**
```prolog
% Find functions that call X but aren't tests
find(F) :- calls(F, X), not(test_file(F)).

% Find all transitive callers (who depends on this?)
find(F) :- calls+(F, X).  % + = transitive
```

**2. Data Flow Queries**
```prolog
% Where does data from A get transformed before reaching B?
find(X) :- 
  reads(X, A),
  writes(X, Temp),
  reads(Y, Temp),
  writes(Y, B).

% Find all functions that touch sensitive data
find(F) :- 
  (reads(F, 'password'); writes(F, 'password')),
  not(imports(F, 'bcrypt')).  % Missing encryption!
```

**3. Structural Queries**
```prolog
% Find implementations of interface X
find(C) :- implements(C, X).

% Find classes with many dependencies (potential god objects)
find(C) :- 
  class(C),
  count(depends_on(C, _), N),
  N > 10.
```

**4. Semantic Queries**
```prolog
% Find auth logic regardless of naming
find(F) :-
  (reads(F, 'token'); reads(F, 'session')),
  (writes(F, 'req.user'); writes(F, 'context.user')),
  validates(F, _).

% Find error handling gaps
find(F) :- 
  calls(F, 'db.query'),
  not(catches(F, 'DatabaseError')).
```

---

## Phase 3: Execution

Run queries against the knowledge graph:

```bash
python scripts/query_code_facts.py facts.json --query query.dl
```

**Results:**
```json
{
  "query": "auth logic",
  "results": [
    {
      "id": "func_042",
      "name": "SessionManager.validate",
      "file": "/auth/session.ts",
      "line": 45,
      "why_matched": [
        "reads: req.headers.authorization",
        "writes: req.session",
        "validates: token signature"
      ],
      "confidence": 0.95
    },
    {
      "id": "func_067",
      "name": "middleware",  % Generic name!
      "file": "/middleware/auth.ts",
      "line": 12,
      "why_matched": [
        "reads: req.cookies.session",
        "writes: req.user",
        "validates: expiry"
      ],
      "confidence": 0.88
    }
  ],
  "keyword_search_would_have_missed": ["func_067"]
}
```

---

## State Machine

### State 0: Extract Facts

**Goal:** Build the knowledge graph from codebase.

**Action:**
```bash
python scripts/extract_code_facts.py ./src --output facts.json
```

**Exit condition:** `facts.json` exists with valid structure.

**Artifacts:**
```yaml
extraction_report:
  files_processed: 150
  functions_extracted: 450
  classes_extracted: 32
  data_flows_traced: 89
  errors: []  # Files that couldn't be parsed
```

---

### State 1: Formulate Query

**Goal:** Translate natural language need to logic query.

**Process:**
```
User need: "Where does session data get validated?"

↓ Translate to constraints

reads(X, 'session') ∧ validates(X, _) ∧ ¬test(X)

↓ Write as Datalog

find(F) :- 
  reads(F, 'session'),
  validates(F, Data),
  Data != null,
  not(test_file(F)).
```

**Exit condition:** Query written, constraints explicit.

---

### State 2: Execute Query

**Goal:** Run logic query against knowledge graph.

**Action:**
```bash
python scripts/query_code_facts.py facts.json --query session_validation.dl
```

**Exit condition:** Results returned with confidence scores.

---

### State 3: Validate Results

**Goal:** Verify results make sense, not false positives.

**Check:**
```yaml
validation:
  for_each_result:
    - check_source_code: true  # Read the actual file
    - verify_why_matched: true  # Do the claimed facts hold?
    - assess_relevance: "Does this actually answer the query?"
    
  false_positive_check:
    - "Result mentions 'session' but doesn't validate it"
    - "Result is a test file (should have been filtered)"
    - "Result is a type definition, not implementation"
```

**Exit condition:** Results validated or false positives removed.

---

### State 4: Refine or Return

**If results insufficient:**
```yaml
refinement:
  analysis: "Too many results — need to narrow"
  action: "Add constraint: only functions that write to 'req.user'"
  new_query: |
    find(F) :- 
      reads(F, 'session'),
      validates(F, _),
      writes(F, 'req.user'),
      not(test_file(F)).
```

**If results good:**
```yaml
return:
  locations: ["SessionManager.validate", "middleware.auth"]
  approach: "keyword-agnostic logic query"
  confidence: 0.92
```

---

## Example Queries

### Example 1: Find Auth Logic (Keyword-Agnostic)

**Natural language:** "Find authentication logic"

**Keyword search:** `grep -r "auth" .` → 200+ results, mostly noise

**Logic query:**
```prolog
find(F) :-
  % Reads credentials from request
  (reads(F, 'req.headers.authorization');
   reads(F, 'req.cookies.session')),
  
  % Performs validation
  (calls(F, 'verify'); calls(F, 'validate');
   uses(F, 'crypto')),
  
  % Sets user context
  (writes(F, 'req.user'); writes(F, 'context.user')),
  
  % Not a test
  not(test_file(F)).
```

**Results:**
- `SessionManager.validate` (obvious)
- `middleware.ts:verifyRequest` (would have missed — generic name)
- `api.gateway:checkToken` (would have missed — different vocabulary)

---

### Example 2: Find Data Transformation Chain

**Natural language:** "Where does user input get sanitized before database?"

**Logic query:**
```prolog
find(Chain) :-
  % Start: reads user input
  reads(Start, 'req.body'),
  
  % End: writes to database
  writes(End, 'db.users'),
  
  % Path exists between them
  path(Start, End, Chain),
  
  % At least one step sanitizes
  member(SanitizeStep, Chain),
  (calls(SanitizeStep, 'sanitize');
   calls(SanitizeStep, 'escape');
   imports(SanitizeStep, 'validator')),
  
  % No step bypasses validation
  not((member(Step, Chain), 
       writes(Step, 'db.users'),
       not(calls(Step, 'sanitize'))) ).
```

**Results:** Complete chain from input → sanitization → database.

---

### Example 3: Find Missing Error Handling

**Natural language:** "Where do we call external APIs without error handling?"

**Logic query:**
```prolog
find(F) :-
  % Makes external call
  (calls(F, 'fetch'); calls(F, 'axios');
   calls(F, 'request')),
  
  % In async context
  async(F),
  
  % No error handling
  not((catches(F, _); 
       calls(F, 'tryCatch');
       calls(F, 'handleError'))).
```

**Results:** Functions making unprotected external calls — bug candidates.

---

## Integration with Other Skills

- Use **before** `abductive-first-debugging` to locate relevant code
- Use **with** `thought-retriever` to store discovered relationships
- Use **after** `compression-as-understanding` to verify the knowledge graph is correct

---

## Python Scripts

Two scripts provided:

1. **`scripts/extract_code_facts.py`** — Extracts facts from codebase
2. **`scripts/query_code_facts.py`** — Executes Datalog queries

See script headers for usage details.

---

## Anti-Patterns

**Don't:**
- Use this for simple name-based lookups (overkill)
- Trust results without reading source code
- Build huge queries without testing incrementally
- Ignore extraction errors (they indicate blind spots)

**Do:**
- Start with small queries, add constraints incrementally
- Validate results against source
- Re-extract facts when codebase changes significantly
- Combine with keyword search for hybrid approach

---

## See Also

- Paper: "Neurosymbolic Repo-level Code Localization" (arXiv:2604.16021)
- Datalog query language
- CodeQL (GitHub's semantic code analysis)
- `code-review-graph-hermes-integration` — for codebase understanding
