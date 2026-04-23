# Skill: Abductive-First Debugging — Inference to Best Explanation

## Purpose

Debug by generating multiple competing hypotheses and selecting the one that provides the *best explanation* for all observed symptoms — not the first plausible cause, not pattern-matching, but genuine abductive reasoning.

Based on "Wiring the 'Why': A Unified Taxonomy of Abductive Reasoning in LLMs" (arXiv:2604.08016) and Peirce's theory of abduction.

---

## When to Use

- Novel failures with no established pattern
- Symptoms that could have multiple causes
- When deductive tracing hits dead ends
- Complex failures where multiple systems interact
- Any bug that "doesn't make sense" given current understanding

**Don't use when:**
- Clear error message points to specific line
- Known pattern match (use inductive instead)
- Simple cause-effect chain visible (use deductive instead)
- **Deterministic code bugs with a reproducible failing test** — empirical testing shows this skill burns the entire tool-call budget on hypothesis generation without fixing the bug. In a FastAPI router bug trial, the skill agent consumed 20 tool calls and failed to produce a fix, while the baseline agent fixed it in 5 calls.
- **You have a tight tool-call budget** — the 6-state protocol (symptom collection → hypothesis generation → coherence evaluation → IBE → differential diagnosis → execution) requires ~10-15 calls before any code change. If your budget is ≤25 calls, this skill will likely fail.
- **The failure is a silent logic error in a single module** — abduction is designed for multi-system novel failures, not localized type mismatches or initialization order bugs.

---

## Core Concept

Three reasoning modes:

| Mode | Question | When to Use |
|------|----------|-------------|
| **Deductive** | "Given cause X, what effects follow?" | Known cause, predict effects |
| **Inductive** | "Given many cases, what's the pattern?" | Historical data, predict future |
| **Abductive** | "Given symptom Y, what best explains it?" | Unknown cause, infer explanation |

**Abductive reasoning steps:**
1. **Generate hypotheses:** Multiple competing explanations
2. **Evaluate explanatory coherence:** Which explains *all* symptoms?
3. **Inference to best explanation:** Select the one with least unexplained observations

---

## State Machine

### State 0: Symptom Collection

Gather all observations before hypothesizing.

```yaml
symptom_collection:
  primary_symptom: "The main failure (e.g., '500 errors under load')"
  
  secondary_symptoms:
    - "Intermittent, not consistent"
    - "Only happens with cache cold"
    - "Stops after restart"
    - "No errors in application logs"
    - "Database shows connection timeouts"
    
  negative_symptoms:  # Things that DON'T happen (equally important)
    - "Doesn't happen on single requests"
    - "Doesn't happen when cache is warm"
    - "No memory pressure observed"
    
  context:
    recent_changes: ["Deployed new auth middleware"]
    environment: "Production, 1000+ concurrent users"
    timing: "Started 2 days ago"
```

**Exit condition:** All symptoms documented, including negative observations.

---

### State 1: Hypothesis Generation (Abduction)

Generate **at least 3 competing hypotheses**. Force creativity — don't stop at the first plausible explanation.

```yaml
hypothesis_generation:
  minimum_hypotheses: 3
  
  hypotheses:
    - id: "H1"
      name: "Cache stampede"
      explanation: |
        Multiple concurrent requests hit cold cache simultaneously,
        each triggering DB query. Connection pool exhausted.
      explains:
        - "Intermittent (race condition)"
        - "Under load (concurrency required)"
        - "Cache cold (trigger condition)"
        - "Connection timeouts (effect)"
      doesnt_explain:
        - "Why restart fixes it (should still have cold cache)"
        
    - id: "H2"
      name: "Connection pool leak"
      explanation: |
        New auth middleware doesn't release connections properly.
        Pool drains over time until exhausted.
      explains:
        - "Under load (faster exhaustion)"
        - "Connection timeouts (direct effect)"
        - "Restart fixes (resets pool)"
      doesnt_explain:
        - "Why cache cold matters"
        - "Why intermittent (should be gradual)"
        
    - id: "H3"
      name: "Query plan degradation"
      explanation: |
        Cold cache means different query pattern. Auth middleware
        triggers expensive query that times out.
      explains:
        - "Cache cold (different code path)"
        - "Connection timeouts (query hangs)"
        - "Intermittent (depends on data distribution)"
      doesnt_explain:
        - "Why restart fixes (should persist)"
        
    - id: "H4"  # Force at least one "wild card"
      name: "Rate limiting misconfiguration"
      explanation: |
        New auth middleware triggers rate limiter that wasn't
        configured for production load. Appears as timeout.
      explains:
        - "Under load (trigger condition)"
        - "Restart fixes (resets rate limit window)"
        - "Intermittent (depends on request distribution)"
      doesnt_explain:
        - "Why cache cold matters"
        - "Connection timeouts specifically"
```

**Exit condition:** ≥3 hypotheses, each with explains/doesnt_explain lists.

---

### State 2: Explanatory Coherence Evaluation

Score each hypothesis on how well it explains ALL symptoms.

```yaml
coherence_evaluation:
  scoring_criteria:
    coverage: "What % of symptoms are explained"
    specificity: "Are explanations precise or hand-wavy?"
    simplicity: "Does it require many assumptions?"
    consistency: "Do the pieces fit together logically?"
    
  evaluations:
    - hypothesis: "H1"
      coverage: 80%  # 4/5 symptoms
      unexplained:
        - "Restart fix (weak explanation: 'clears load')"
      coherence_score: 0.75
      
    - hypothesis: "H2"
      coverage: 60%  # 3/5 symptoms
      unexplained:
        - "Cache cold correlation"
        - "Intermittent nature (predicts gradual)"
      coherence_score: 0.50
      
    - hypothesis: "H3"
      coverage: 60%  # 3/5 symptoms
      unexplained:
        - "Restart fix"
      coherence_score: 0.55
      
    - hypothesis: "H4"
      coverage: 60%  # 3/5 symptoms
      unexplained:
        - "Cache cold correlation"
        - "Connection timeouts specifically"
      coherence_score: 0.45
```

**Exit condition:** Each hypothesis scored, unexplained symptoms listed.

---

### State 3: Inference to Best Explanation (IBE)

Select the hypothesis with best explanatory coherence.

```yaml
ibe_selection:
  best_hypothesis: "H1"
  selection_rationale: |
    H1 explains 4/5 symptoms with high specificity. The unexplained
    "restart fix" is weakly explained by load clearing. Other
    hypotheses miss the cache-cold correlation entirely.
  
  runner_up: "H3"
  why_not_runner_up: |
    H3 fails to explain why restart fixes the issue. If it's query
    plan degradation, the problem should persist after restart.
  
  confidence: 0.75  # Not 100% — H1 isn't perfect
  
  # If no hypothesis scores >0.6:
  insufficient_explanation_action: |
    Gather more evidence specifically targeting the unexplained
    symptoms. Don't proceed with low-coherence hypotheses.
```

**Exit condition:** Best hypothesis selected with rationale.

---

### State 4: Differential Diagnosis

Design tests that discriminate between best hypothesis and alternatives.

```yaml
differential_diagnosis:
  best_hypothesis: "H1: Cache stampede"
  
  discriminatory_tests:
    - test: "Warm cache before load test"
      prediction_if_H1_correct: "No failures"
      prediction_if_H2_correct: "Still fails (pool leak)"
      prediction_if_H3_correct: "Still fails (query plan)"
      
    - test: "Monitor connection pool during cold cache request"
      prediction_if_H1_correct: "Pool exhaustion with many waiting connections"
      prediction_if_H2_correct: "Gradual drain, not sudden spike"
      prediction_if_H3_correct: "Single hanging query, not pool exhaustion"
      
    - test: "Add request coalescing (singleflight)"
      prediction_if_H1_correct: "Failures stop (eliminates stampede)"
      prediction_if_H2_correct: "Still fails (doesn't fix leak)"
      prediction_if_H3_correct: "Still fails (doesn't fix query)"
```

**Exit condition:** Tests designed that would falsify at least one hypothesis.

---

### State 5: Execute and Update

Run discriminatory tests, update confidence.

```yaml
test_execution:
  results:
    - test: "Warm cache before load test"
      result: "No failures observed"
      update: "Strong support for H1, falsifies H2 and H3"
      
    - test: "Monitor connection pool"
      result: "Sudden spike to max connections on cold cache"
      update: "Confirms H1 prediction exactly"
      
  final_assessment:
    confirmed_hypothesis: "H1: Cache stampede"
    confidence: 0.90
    action: "Implement request coalescing (singleflight)"
    
  # If test contradicts best hypothesis:
  fallback_action: |
    Re-evaluate all hypotheses. The unexplained symptom may be
    the key. Consider H4 (rate limiting) or generate new H5.
```

---

## Abductive vs Other Skills

| Situation | Use |
|-----------|-----|
| Known error pattern | Inductive pattern-matching |
| Clear cause-effect chain | Deductive tracing |
| Novel, unexplained symptoms | **This skill (abductive)** |
| Multiple interacting systems | **This skill + triad-reasoning** |

---

## Anti-Patterns

**Don't:**
- Stop at first plausible hypothesis
- Ignore symptoms that don't fit your favorite theory
- Skip differential testing
- Confuse correlation (cache cold + failure) with causation

**Do:**
- Force generation of at least 3 hypotheses
- Be explicit about what each hypothesis *doesn't* explain
- Design tests that would prove you wrong
- Update confidence based on evidence

---

## Integration

- Use **after** `metacognitive-monitoring` to assess confidence in each hypothesis
- Use **with** `thought-retriever` to store and retrieve past abductive conclusions
- Use **before** `rashomon-triad-hybrid` when multiple genuine explanations exist

---

## See Also

- Paper: "Wiring the 'Why': A Unified Taxonomy of Abductive Reasoning in LLMs" (arXiv:2604.08016)
- Peirce's theory of abduction (inference to best explanation)
- `how-to-solve-it-state-machine-skill` — for structured problem-solving
