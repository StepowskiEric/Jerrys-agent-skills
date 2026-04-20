# Skill: Thought-Retriever with Coppermind

## Purpose

Enable sub-agents to build collective reasoning memory using the Coppermind three-layer memory architecture. Instead of just returning answers, agents store structured "thoughts" (intermediate reasoning) as Coppermind memories that future agents can retrieve and build upon.

This skill bridges the paper's Thought-Retriever algorithm with Coppermind's working/episodic/semantic memory layers, giving agents self-evolving long-term memory that grows more capable through continuous interaction.

---

## When to Use

- Complex multi-step problems where future similar tasks will arise
- When you want agents to learn from each other's problem-solving approaches  
- Debugging, research, design tasks where "how we got here" matters as much as "what we concluded"
- Cross-session work where memory must persist beyond a single conversation

---

## Coppermind Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         COPPERMIND MEMORY                           │
├─────────────────┬─────────────────┬─────────────────────────────────┤
│  Working Layer  │  Episodic Layer │      Semantic Layer             │
│  (Session)      │  (Episodes)     │      (Long-term)                │
├─────────────────┼─────────────────┼─────────────────────────────────┤
│ Active thoughts │ Thought episodes│ Abstracted reasoning patterns     │
│ being generated │ with full       │ ("how we solve auth problems")   │
│ right now       │ context + trace │                                   │
└────────┬────────┴────────┬────────┴────────────────┬────────────────┘
         │                 │                       │
         ▼                 ▼                       ▼
   Real-time          Persistent              Generalized
   reasoning          task memory             knowledge
```

**Thought Types Map to Layers:**

| Thought Type | Coppermind Layer | Purpose |
|--------------|------------------|---------|
| `observation` | Working → Episodic | Facts detected during task execution |
| `inference` | Episodic | Reasoning steps connecting observations |
| `hypothesis` | Working | Candidate explanations being tested |
| `uncertainty` | Episodic | Known unknowns, gaps in understanding |
| `conclusion` | Semantic | Validated findings promoted to long-term |

---

## Pattern

```
┌─────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Sub-agent  │────▶│  Thought Store   │────▶│  Coppermind      │
│  solves task│     │  (structured)    │     │  Memory System   │
└─────────────┘     └──────────────────┘     └────────┬─────────┘
                                                        │
                              ┌─────────────────────────┘
                              │
┌─────────────┐     ┌─────────▼─────────┐     ┌─────────────┐
│  Sub-agent  │◀────│  Retrieved        │◀────│  Semantic   │
│  builds on  │     │  Thoughts         │     │  Search     │
│  prior work │     │  (context-rich)   │     │  + Episodic │
└─────────────┘     └───────────────────┘     └─────────────┘
```

---

## Mandatory Thought Structure

Every thought stored in Coppermind must include:

```yaml
thought:
  id: "thought_<timestamp>_<hash>"  # Unique identifier
  type: "observation|inference|hypothesis|uncertainty|conclusion"
  content: "The actual reasoning content"
  confidence: 0.0-1.0               # Certainty level
  source:                           # Traceability
    agent_id: "<sub-agent-name>"
    task_id: "<parent-task-id>"
    session_id: "<coppermind-session>"
  context:                          # Retrieval context
    domain: "auth|performance|security|etc"
    tags: ["jwt", "react", "ssr"]
    related_files: ["/middleware/auth.ts"]
  temporal:                         # For memory lifecycle
    created: "<iso-timestamp>"
    last_accessed: "<iso-timestamp>"
    access_count: 0                 # For liveness scoring
```

---

## Workflow

### Phase 1: Thought Generation (During Task Execution)

As the sub-agent works, it generates thoughts:

```
## State: Working → Generate Thoughts

When making observations:
- Store as type: "observation"
- Include file paths, line numbers, exact quotes
- Confidence: 0.9+ for direct evidence, 0.7-0.8 for interpretation

When drawing conclusions:
- Store as type: "inference" 
- Link to supporting observations via thought_ids
- Confidence reflects strength of reasoning chain

When encountering gaps:
- Store as type: "uncertainty"
- Be explicit about what's unknown
- These become valuable retrieval targets for future debugging

When completing:
- Store as type: "conclusion"
- Summarize key findings
- These may be promoted to semantic layer
```

### Phase 2: Thought Persistence (To Coppermind)

```
## State: Store → Coppermind Integration

For each thought:
1. Serialize to Coppermind memory format
2. Store in appropriate layer:
   - Working: Active task context (auto-expires)
   - Episodic: Full episode with thought trace (persistent)
   - Semantic: Abstracted patterns (if conclusion type + high confidence)

3. Create cross-references:
   - Link observations → inferences → conclusions
   - Tag with domain vocabulary for retrieval
   - Index file paths for code-aware retrieval
```

### Phase 3: Thought Retrieval (For New Tasks)

```
## State: Retrieve → Prior Work Integration

Before starting new task:
1. Query Coppermind semantic layer for relevant patterns:
   - "How have we solved {domain} problems before?"
   - Retrieve abstracted reasoning patterns

2. Query Coppermind episodic layer for specific precedents:
   - "What thoughts exist about {specific files/topics}?"
   - Retrieve full reasoning traces

3. Rank by relevance + confidence + recency:
   - Semantic match score
   - Confidence threshold (default: 0.7)
   - Liveness score (access-based decay)

4. Inject retrieved thoughts as context:
   - Include thought content + source traceability
   - Preserve uncertainty markers
   - Surface conflicting inferences if present
```

---

## Example Usage

### Parent Agent Spawns Researcher

```yaml
delegate_task:
  goal: "Research authentication patterns in this codebase"
  context: |
    Focus on JWT handling, token refresh, and session management.
    Use thought-retriever pattern: store observations, inferences, 
    and uncertainties as you discover them.
  
  # Sub-agent returns structured result with thoughts
```

### Sub-Agent Output (Stored to Coppermind)

```yaml
result:
  answer: "Found 3 auth patterns: middleware-based, hook-based, and HOC-based"
  
  thoughts:
    - id: "thought_20250420_001"
      type: "observation"
      content: "Middleware pattern in /middleware/auth.ts uses edge runtime"
      confidence: 0.95
      source:
        agent_id: "auth-researcher"
        task_id: "auth-pattern-research"
      context:
        domain: "auth"
        tags: ["middleware", "edge", "jwt"]
        related_files: ["/middleware/auth.ts"]
      
    - id: "thought_20250420_002"
      type: "inference"
      content: "Hook pattern couples auth state with React lifecycle - potential SSR issues"
      confidence: 0.80
      source:
        agent_id: "auth-researcher"
        task_id: "auth-pattern-research"
      context:
        domain: "auth"
        tags: ["hooks", "react", "ssr", "lifecycle"]
        related_files: ["/hooks/useAuth.ts"]
      supporting_thoughts: ["thought_20250420_003"]  # Links to observation
      
    - id: "thought_20250420_003"
      type: "uncertainty"
      content: "HOC pattern usage unclear - may be legacy, needs verification"
      confidence: 0.40
      source:
        agent_id: "auth-researcher"
        task_id: "auth-pattern-research"
      context:
        domain: "auth"
        tags: ["hoc", "legacy", "verification-needed"]
        related_files: ["/components/withAuth.tsx"]
```

### Later: Different Sub-Agent Queries Thought Memory

```yaml
thought_retriever:
  query: "What auth patterns have SSR compatibility issues?"
  filters:
    domain: "auth"
    confidence_min: 0.70
    thought_types: ["inference", "conclusion"]
  
# Returns:
retrieved_thoughts:
  - id: "thought_20250420_002"
    type: "inference"
    content: "Hook pattern couples auth state with React lifecycle - potential SSR issues"
    confidence: 0.80
    source:
      agent_id: "auth-researcher"
      task_id: "auth-pattern-research"
      created: "2025-04-20T10:30:00Z"
    # Includes full traceability and context
```

---

## Integration with Coppermind Tools

### Storing Thoughts (via MCP)

```
Use mcp_coppermind_store_memory with:
- content: serialized thought JSON
- layer: "episodic" (default) or "semantic" (for conclusions)
- metadata: thought context, tags, source traceability
- episode_id: link to parent task episode
```

### Retrieving Thoughts (via MCP)

```
Use mcp_coppermind_semantic_search_nodes with:
- query: natural language description of needed reasoning
- kind: "Thought" (if using custom node types)
- filters: confidence, domain, recency

Or use mcp_coppermind_traverse_graph:
- query: thought_id to expand from
- mode: "bfs" to find related thoughts
- depth: 2-3 for reasoning chains
```

---

## Confidence Thresholds

| Confidence | Interpretation | Retrieval Behavior |
|------------|----------------|-------------------|
| 0.90-1.0 | Direct observation, verified fact | Always retrieve, high priority |
| 0.70-0.89 | Strong inference, good evidence | Retrieve unless contradicted |
| 0.50-0.69 | Weak inference, some evidence | Retrieve with uncertainty flag |
| 0.30-0.49 | Hypothesis, unverified | Retrieve only if no better options |
| <0.30 | Pure speculation | Do not retrieve (store for record) |

---

## Memory Lifecycle

Thoughts in Coppermind follow access-based liveness:

```
Creation → Active Use → Decay → Archive/Delete
   │           │          │          │
   ▼           ▼          ▼          ▼
High score   Accessed    Not accessed Purged or
freshness    increases   for N days archived to
             liveness    → liveness   cold storage
                         decays
```

**Implementation:**
- Use Coppermind's liveness scoring if available
- Otherwise: track `access_count` and `last_accessed` in thought metadata
- Decay function: `liveness = access_count / (days_since_access + 1)`

---

## Anti-Patterns

**Don't:**
- Store raw outputs without reasoning structure
- Merge conflicting thoughts without marking conflict
- Retrieve low-confidence thoughts without flagging uncertainty
- Forget to include source traceability (makes thoughts untrustworthy)

**Do:**
- Be explicit about uncertainty — it's valuable for future debugging
- Link related thoughts (observation → inference → conclusion)
- Include file paths and code snippets in observation thoughts
- Let high-confidence conclusions bubble up to semantic layer

---

## See Also

- Paper: "Thought-Retriever: Don't Just Retrieve Raw Data, Retrieve Thoughts" (arXiv:2604.12231)
- Coppermind three-layer memory architecture
- `rashomon-triad-hybrid-skill` — for when multiple conflicting perspectives exist
