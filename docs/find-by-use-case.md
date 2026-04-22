# Find by Use Case

**"I need a skill for..."**

### Debugging / Problem Solving

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Hard bug, don't know where to start | [`how-to-solve-it-state-machine`](execution/how-to-solve-it-state-machine-skill.md) | Forces problem framing before action |
| Multiple possible causes | [`abductive-first-debugging`](execution/abductive-first-debugging-skill.md) | Generates competing hypotheses, picks best explanation |
| Need to locate relevant code | [`keyword-agnostic-logic-locator`](execution/keyword-agnostic-logic-locator-skill.md) | Finds code by structure, not by grepping |
| **Correlate error logs and stack traces** | [`log-trace-correlation`](debugging/log-trace-correlation) | Maps traces to source, inspects context, suggests fix |
| Stuck in a rut, same failed attempts | [`cross-domain-analogy-generator`](systems-and-architecture/cross-domain-analogy-generator-skill.md) | Forces foreign-domain analogies to break fixation |
| Prematurely jumping to solutions | [`ooda-loop-state-machine`](execution/ooda-loop-state-machine-skill.md) | Observe → Orient → Decide → Act cycle |
| Over-thinking trivial bugs | [`cognitive-friction-governor`](execution/cognitive-friction-governor-skill.md) | Budgets deliberation, forces decision |
| Backtrack when reasoning goes wrong | [`process-reward-model-protocol`](execution/process-reward-model-protocol-skill.md) | Self-correcting reasoning path |
| Mid-reasoning "actually wait" self-correction | [`process-reward-model-protocol`](execution/process-reward-model-protocol-skill.md) | Self-correcting reasoning path with backtracking |
| Use analogy to solve problems | [`how-to-solve-it-analogy`](execution/how-to-solve-it-analogy-skill.md) | Structured analogy-based problem solving |
| Continuous improvement cycle | [`pdca-deming`](execution/pdca-deming-skill.md) | Plan-Do-Check-Act iterative improvement |
| Toyota-style continuous improvement | [`toyota-kata-state-machine`](execution/toyota-kata-state-machine-skill.md) | Scientific thinking pattern |
| Verify each step before proceeding | [`step-level-verification-protocol`](execution/step-level-verification-protocol-skill.md) | Prevents error propagation |

### Code Review / Quality

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Security + performance + maintainability conflict | [`rashomon-triad-hybrid`](orchestration/rashomon-triad-hybrid-skill.md) | Parallel perspectives argue, surface conflicts |
| Not sure if I understand the code | [`compression-as-understanding`](output-quality/compression-as-understanding-skill.md) | Compress to essence, test reconstruction |
| Need to verify my understanding | [`metacognitive-monitoring`](judgment-and-routing/metacognitive-monitoring-skill.md) | Explicit confidence calibration |
| Refactoring legacy code | [`working-effectively-with-legacy-code-state-machine`](execution/working-effectively-with-legacy-code-state-machine-skill.md) | Safe change protocol |
| Code smells but not sure what | [`philosophy-of-software-design-state-machine`](execution/philosophy-of-software-design-state-machine-skill.md) | Complexity management |
| Before committing changes | [`verify-before-integrate`](software-development/verify-before-integrate-skill.md) | Pre-commit verification |
| Refactoring safely | [`refactoring-state-machine`](execution/refactoring-state-machine-skill.md) | Structured refactoring protocol |
| Follow pragmatic programmer principles | [`pragmatic-programmer-state-machine`](execution/pragmatic-programmer-state-machine-skill.md) | Core programming wisdom |
| Self-check for thoroughness | [`thoroughness-check-etto`](judgment-and-routing/thoroughness-check-etto-skill.md) | Systematic completeness check |
| Strict thoroughness protocol | [`thoroughness-check-etto-state-machine`](judgment-and-routing/thoroughness-check-etto-state-machine-skill.md) | Enforced thoroughness state machine |
| Validate decisions with counterfactuals | [`counterfactual-policy-testing`](judgment-and-routing/counterfactual-policy-testing-skill.md) | Test against alternatives |
| Improve my own output | [`bounded-self-revision`](output-quality/bounded-self-revision-skill.md) | Structured self-improvement |
| Generate and verify multiple solutions | [`speculative-drafting-verification`](execution/speculative-drafting-verification-skill.md) | Parallel candidate evaluation |
| Check for cognitive biases | [`cognitive-bias-checklist`](judgment-and-routing/cognitive-bias-checklist-skill.md) | Bias detection and mitigation |
| Verify self-consistency | [`self-consistency`](output-quality/self-consistency-skill.md) | Cross-check reasoning |
| Interactive criticism of work | [`tool-interactive-critic`](output-quality/tool-interactive-critic-skill.md) | Structured critique process |

### Architecture / Design Decisions

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Prevent over-engineering, clarify scope before coding | [`intent-specification-protocol`](execution/intent-specification-protocol-skill.md) | Scope control via explicit intent specification |
| Big decision, multiple options | [`counterfactual-policy-testing`](judgment-and-routing/counterfactual-policy-testing-skill.md) | Test against null/opposite/partial alternatives |
| Trade-offs between teams/systems | [`team-topologies-ai`](systems-and-architecture/team-topologies-ai-skill.md) | Organizational architecture patterns |
| Data system design | [`designing-data-intensive-applications-ai`](systems-and-architecture/designing-data-intensive-applications-ai-skill.md) | Data system principles |
| Scalability concerns | [`sre-error-budget`](systems-and-architecture/sre-error-budget-skill.md) | Reliability vs velocity trade-offs |
| Domain modeling | [`domain-driven-design`](systems-and-architecture/domain-driven-design-skill.md) | Bounded contexts, ubiquitous language |
| Not sure what kind of problem | [`problem-mode-router-cynefin`](judgment-and-routing/problem-mode-router-cynefin-skill.md) | Cynefin framework routing |
| Accelerate delivery | [`accelerate-ai`](systems-and-architecture/accelerate-ai-skill.md) | DevOps and delivery optimization |
| Release planning | [`release-it-stability`](systems-and-architecture/release-it-stability-skill.md) | Stability patterns |
| Separation of concerns | [`separation-of-concerns`](orchestration/separation-of-concerns-skill.md) | Component boundary design |
| Router for problem types (state machine) | [`problem-mode-router-cynefin-state-machine`](judgment-and-routing/problem-mode-router-cynefin-state-machine-skill.md) | Enforced Cynefin routing |
| System thinking protocol | [`thinking-in-systems-state-machine`](systems-and-architecture/thinking-in-systems-state-machine-skill.md) | System dynamics analysis |

### Documentation / Communication

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Ambiguous requirements, need to clarify before coding | [`intent-specification-protocol`](execution/intent-specification-protocol-skill.md) | Specify and validate intent before writing code |
| Writing README / API docs | [`documentation-craft`](output-quality/documentation-craft-skill.md) | 5-phase structured writing |
| Explaining complex system simply | [`feynman-technique`](output-quality/feynman-technique-skill.md) | Explain to a child |
| Team/process problems | [`everything-as-code-conceptualizer`](systems-and-architecture/everything-as-code-conceptualizer-skill.md) | Codify non-code systems |
| Need clarity on requirements | [`socratic-clarification`](orchestration/socratic-clarification-skill.md) | Pre-execution clarification |
| Navigate large documentation | [`large-documentation-navigation`](output-quality/large-documentation-navigation-skill.md) | Structured doc exploration |
| MECE structuring | [`mece-pyramid-principle`](output-quality/mece-pyramid-principle-skill.md) | Mutually exclusive, collectively exhaustive |
| Steelman opposing views | [`steelmanning`](judgment-and-routing/steelmanning-skill.md) | Strongest version of opponent's argument |

### Planning / Estimation

| Situation | Best Skill | Why |
|-----------|------------|-----|
| How long will this take? | [`reference-class-forecasting`](judgment-and-routing/reference-class-forecasting-skill.md) | Base rate estimation |
| What could go wrong? | [`pre-mortem-state-machine`](judgment-and-routing/pre-mortem-state-machine-skill.md) | Prospective hindsight |
| Should I explore or exploit? | [`explore-vs-exploit-state-machine`](judgment-and-routing/explore-vs-exploit-state-machine-skill.md) | Resource allocation |
| Complex multi-step plan | [`checklist-manifesto`](execution/checklist-manifesto-skill.md) | Checklist discipline |
| Theory of constraints | [`the-goal-theory-of-constraints-ai`](systems-and-architecture/the-goal-theory-of-constraints-ai-skill.md) | Bottleneck identification |
| Explore vs exploit (framework) | [`explore-vs-exploit`](judgment-and-routing/explore-vs-exploit-skill.md) | Decision framework |
| Pre-mortem (framework) | [`pre-mortem`](judgment-and-routing/pre-mortem-skill.md) | Prospective hindsight analysis |

### Learning / Understanding

| Situation | Best Skill | Why |
|-----------|------------|-----|
| New codebase, need to understand | [`compression-as-understanding`](output-quality/compression-as-understanding-skill.md) | Verify understanding via compression |
| Researching a topic | [`tree-of-thoughts`](output-quality/tree-of-thoughts-skill.md) | Branching exploration |
| First principles thinking | [`first-principles`](judgment-and-routing/first-principles-skill.md) | Deconstruct to fundamentals |
| Inverting the problem | [`inversion-mental-model`](judgment-and-routing/inversion-mental-model-skill.md) | Think backwards |
| Analyzing from multiple angles | [`six-thinking-hats`](judgment-and-routing/six-thinking-hats-skill.md) | Parallel thinking modes |
| Inversion (state machine) | [`inversion-mental-model-state-machine`](judgment-and-routing/inversion-mental-model-state-machine-skill.md) | Structured backward thinking |
| Second-order effects | [`second-order-thinking`](judgment-and-routing/second-order-thinking-skill.md) | Consequences of consequences |
| Bayesian updating | [`bayesian-updating`](judgment-and-routing/bayesian-updating-skill.md) | Probabilistic belief updating |
| Recognition-primed decisions | [`recognition-primed-triage`](judgment-and-routing/recognition-primed-triage-skill.md) | Expert pattern matching |
| RPD state machine | [`recognition-primed-triage-state-machine`](judgment-and-routing/recognition-primed-triage-state-machine-skill.md) | Structured expert decision |
| Kahneman fast/slow thinking | [`kahneman-thinking-fast-slow-software-agent`](judgment-and-routing/kahneman-thinking-fast-slow-software-agent-skill.md) | Dual-process thinking |
| Detect reasoning hallucinations | [`faithfulness-aware-reasoning`](reasoning/faithfulness-aware-reasoning-skill.md) | Ensures reasoning is logically entailed |

### Development / Skill Building

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Setting up and using local LLMs for agent tasks | [`local-llm-tooling`](mlops/local-llm-tooling) | Reliable workflow for running, prompting, and extracting structured output from local LLMs |

### Software Development

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Writing features or fixing bugs, requirements unclear | [`intent-specification-protocol`](execution/intent-specification-protocol-skill.md) | Clarify intent before coding, prevent over-engineering |
| Need a structured debugging workflow | [`debug-issue`](software-development/debug-issue.md) | Forces reproduce-isolate-fix-verify cycle |
| Need to understand an unfamiliar codebase | [`explore-codebase`](software-development/explore-codebase.md) | Structured exploration with progressive deepening |
| Need to refactor code safely | [`refactor-safely`](software-development/refactor-safely.md) | Characterization testing + bounded changes |
| Need to review code changes | [`review-changes`](software-development/review-changes.md) | Structured review checklist |

### Skill Building

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Adding a new skill to this repo | [`add-new-skill-to-repository`](development/add-new-skill-to-repository/SKILL.md) | Ensures proper documentation, install support, cross-platform verification |

### Multi-Agent / Coordination

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Need to spawn specialized sub-agents | [`agentic-design-patterns-orchestrator`](orchestration/agentic-design-patterns-orchestrator-skill.md) | Agent workflow patterns |
| Orchestrator state machine | [`agentic-design-patterns-orchestrator-state-machine`](orchestration/agentic-design-patterns-orchestrator-state-machine-skill.md) | Enforced agent orchestration |
| Storing reasoning for later | [`thought-retriever-coppermind`](orchestration/thought-retriever-coppermind-skill.md) | Memory-augmented reasoning |
| Managing agent memory | [`agent-memory-hygiene`](orchestration/agent-memory-hygiene-skill.md) | Memory categorization |
| Debating which branch to pursue | [`monte-carlo-tree-search`](monte-carlo-tree-search-skill.md) | Branch allocation |
| Identify weak agent reasoning | [`weak-link-detection-multi-agent`](orchestration/weak-link-detection-multi-agent-skill.md) | Prevents error amplification |

### Risk / Safety Analysis

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Safety-critical changes | [`unsafe-control-actions-hazard-analysis`](judgment-and-routing/unsafe-control-actions-hazard-analysis-skill.md) | STPA safety analysis |
| What could break? | [`pre-mortem`](judgment-and-routing/pre-mortem-skill.md) | Prospective hindsight |
| Second-order effects | [`second-order-thinking`](judgment-and-routing/second-order-thinking-skill.md) | Consequences of consequences |
| Release planning | [`release-it-stability`](systems-and-architecture/release-it-stability-skill.md) | Stability patterns |
| Pre-mortem protocol | [`pre-mortem-state-machine`](judgment-and-routing/pre-mortem-state-machine-skill.md) | Enforced prospective analysis |

### Cognitive Load / Operator Support

| Situation | Best Skill | Why |
|-----------|------------|-----|
| Reduce cognitive load | [`cognitive-load-operator-state-machine`](output-quality/cognitive-load-operator-state-machine-skill.md) | Load management protocol |
