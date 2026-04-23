# Skill Catalog

Skills are organized into topic areas. Each entry shows its file path and whether it is a **[protocol]** (state-machine, enforces a workflow) or a **[framework]** (conceptual lens, improves judgment).

---

# Skill Catalog

Skills are organized into five topic areas. Each entry shows its file path and whether it is a **[protocol]** (state-machine, enforces a workflow) or a **[framework]** (conceptual lens, improves judgment).

---

## 🔧 Execution — how-to-do-the-work protocols

Skills for executing technical work in a bounded, disciplined way.

### `execution/how-to-solve-it-state-machine-skill.md` · [protocol]
**What it is:** A disciplined problem-solving protocol that forces problem framing, evidence gathering, planning, execution, and reflection.

**Use it when:** The task is hard, uncertain, or likely to tempt premature coding.

**Best for:** Debugging, algorithmic reasoning, difficult implementation tasks, root-cause work.

---

### `execution/refactoring-state-machine-skill.md` · [protocol]
**What it is:** A bounded refactoring protocol that defines a target, accounts for shared surfaces, limits the transformation budget, and stops cleanly with an anti-loop circuit breaker.

**Use it when:** Structure needs improvement but the task could spiral into endless cleanup.

**Best for:** Safe refactors, complexity reduction, targeted cleanup, anti-slop work.

---

### `execution/working-effectively-with-legacy-code-state-machine-skill.md` · [protocol]
**What it is:** A protocol for making brittle code safe to change before trying to improve it. Forces characterization testing, seam creation, and explicit stopping to prevent rewrite gambling and cleanup drift.

**Use it when:** The system has weak tests, unclear behavior, tight coupling, or rewrite temptation.

**Best for:** Characterization testing, seam creation, change safety, legacy modernization.

---

### `execution/toyota-kata-state-machine-skill.md` · [protocol]
**What it is:** A continuous-improvement protocol that forces the agent to define the current condition, set the next target condition, isolate one obstacle, and run one bounded experiment at a time.

**Use it when:** The path forward is uncertain and progress should be discovered iteratively rather than through one large redesign.

**Best for:** Optimization, process improvement, performance tuning, workflow refinement, developer-experience improvements, and safe iterative experimentation.

---

### `execution/pragmatic-programmer-state-machine-skill.md` · [protocol]
**What it is:** A practical engineering protocol focused on bounded changes, reversible decisions, automation, and root-cause fixes. Enforces blast-radius accounting, consumer discovery, and clean stopping.

**Use it when:** The agent needs to work like a senior pragmatist instead of an idealist or cleanup maximalist.

**Best for:** Day-to-day engineering work, tooling, repetitive toil reduction, incremental improvements.

---

### `execution/philosophy-of-software-design-state-machine-skill.md` · [protocol]
**What it is:** A protocol for managing complexity, building deeper modules, and avoiding shallow abstraction sprawl. Adds hard gates for consumer discovery before shared-interface edits, unknowns/blast-radius declaration, and bounded change scope.

**Use it when:** The agent is changing shared interfaces or making design decisions that can spread complexity.

**Best for:** API design, module boundaries, simplification, architecture cleanup.

---

### `execution/ooda-loop-state-machine-skill.md` · [protocol]
**What it is:** A decision-tempo protocol based on Boyd's OODA Loop: Observe → Orient → Decide → Act → Loop. Enforces explicit observation before interpretation, mandatory model updates at each cycle, bounded action scope, and loop assessment after every action.

**Use it when:** The environment is changing rapidly, adversarially, or unpredictably between actions — where conditions shift before the previous move settles.

**Best for:** Rapidly-changing incidents, adversarial debugging, dynamic ops response, situations where tempo matters as much as correctness.

---

### `execution/checklist-manifesto-skill.md` · [protocol]
**What it is:** A pre-execution checklist protocol based on Gawande's *The Checklist Manifesto*. Builds the minimal purposeful checklist before any high-stakes procedure, enforces read-do or do-confirm execution, gates each step with confirmation evidence, and halts on exception triggers.

**Use it when:** The task is a high-stakes, known procedure where expert skip-ahead causes failures — and confidence is not a substitute for verification.

**Best for:** Deployment procedures, database migrations, security changes, incident remediation steps, any procedure that has caused failures through missed steps.

---

### `execution/pdca-deming-skill.md` · [protocol]
**What it is:** A measurement-anchored improvement protocol based on the Shewhart/Deming PDCA cycle. Requires a measurable baseline and written prediction before action, mandates a Check phase comparing actual vs. predicted results, and gates standardization on confirmed measurement rather than felt improvement.

**Use it when:** Improving a system or process where you must verify what worked before standardizing it — and where "it seemed better" is not a sufficient conclusion.

**Best for:** Process improvement, performance tuning, quality improvement, any work where standardization should follow verified results.

---

### `execution/step-level-verification-protocol-skill.md` · [protocol]
**What it is:** A verification protocol that validates each reasoning step before proceeding to the next. Prevents error propagation by catching mistakes early in multi-step chains.

**Use it when:** Working on multi-step tasks where early errors compound into larger failures downstream.

**Best for:** Complex debugging, multi-step reasoning, algorithmic work, any task where verification at each step prevents cascading errors.

---

### `execution/speculative-drafting-verification-skill.md` · [protocol]
**What it is:** A parallel solution generation protocol that creates multiple candidate branches, verifies each against constraints, and selects the best. Prevents local minima traps.

**Use it when:** The problem has multiple plausible approaches and committing to one too early risks suboptimal outcomes.

**Best for:** Design decisions, architecture choices, optimization problems, any task where exploring alternatives before committing improves outcomes.

---

### `execution/process-reward-model-protocol-skill.md` · [protocol]
**What it is:** A self-correcting reasoning protocol that assigns process rewards to each step and backtracks when cumulative reward drops below threshold.

**Use it when:** Reasoning may go down wrong paths and needs mechanism to detect and recover from poor reasoning chains.

**Best for:** Complex reasoning tasks, multi-step planning, any work where reasoning quality varies and early detection of bad paths matters.

---

### `execution/how-to-solve-it-analogy-skill.md` · [framework]
**What it is:** A transfer-reasoning skill based on Polya's analogy technique from *How to Solve It*. Finds structural analogs to the current problem, makes the mapping explicit, identifies what transfers and what does not, and adapts the imported solution structure.

**Use it when:** The problem resembles a previously solved one and importing the solution structure would accelerate the work — but only after verifying the mapping holds.

**Best for:** Design decisions, algorithm selection, architecture patterns, any problem where a known solution from another domain is structurally applicable.

---

### `execution/intent-specification-protocol-skill.md` · [protocol]
**What it is:** Crystallize vague coding requests into precise, testable specs before writing code. Prevents over-engineering via the Intent-Behavior Mirroring Effect.

**Use it when:** The request is vague, ambiguous, or likely to lead to over-engineering.

**Best for:** Requirement clarification, spec writing, preventing over-engineering, aligning with stakeholders.

---

### `debugging/log-trace-correlation/SKILL.md` · [protocol]
**What it is:** A protocol for correlating error logs and stack traces to source code to identify root cause and suggest fixes.

**Use it when:** You have an error log with a stack trace and need to determine the exact location and cause of failure.

**Best for:** Debugging, root-cause analysis, failure triage.

---

### `debugging/bisect-debugging/SKILL.md` · [protocol]
**What it is:** Binary search through git history to isolate the exact commit that introduced a regression.

**Use it when:** Tests pass on an older commit but fail on HEAD, or a feature worked previously but is now broken.

**Best for:** Finding regression commits, understanding what changed, root-cause analysis.

---

### `debugging/debug-subagent/SKILL.md` · [protocol]
**What it is:** A dedicated debugging subagent that must be consulted before making code edits. Wraps debugger complexity behind natural-language queries and enforces "debug before edit" workflow.

**Use it when:** The bug is not immediately obvious from the error message, or static analysis hasn't revealed the root cause.

**Best for:** Interactive debugging, program repair, enforcing debug-before-edit discipline. Based on Debug2Fix research (+13-22% bug fix rate).

---

### `debugging/purify-test-output/SKILL.md` · [protocol]
**What it is:** Slice failing test output to only failure-relevant lines before showing to the LLM. Removes noise and reduces tokens by ~18.6%.

**Use it when:** Failing tests produce verbose output, or stack traces include framework frames that drown out user code.

**Best for:** Token efficiency, debugging focus, test output processing. Based on DebugRepair research.

---

### `debugging/simulate-instrumentation/SKILL.md` · [protocol]
**What it is:** Auto-insert temporary print/logging statements at key points, run the failing test, and feed captured runtime state to the LLM.

**Use it when:** The bug involves runtime state invisible in source code, or static analysis has hit a dead end.

**Best for:** Runtime state capture, verifying data flow assumptions, debugging logic errors. Based on DebugRepair research (+26.3% when removed in ablation).

---

### `debugging/iterative-patch-repair/SKILL.md` · [protocol]
**What it is:** Loop of generate patch → run test → capture runtime state → refine patch. Max N iterations with patch augmentation to avoid overfitting.

**Use it when:** The first patch attempt failed, or multiple plausible fixes exist and you need to find the correct one.

**Best for:** Non-obvious bugs, avoiding symptom-only fixes, patch search and verification. Based on DebugRepair research (+19.9% from patch augmentation alone).

## 🧭 Judgment & Routing — deciding what to do and how rigorously

Skills for routing tasks, calibrating rigor, and reasoning about risks and tradeoffs.

### `judgment-and-routing/problem-mode-router-cynefin-skill.md` · [framework]
**What it is:** A routing skill based on Cynefin-style problem classification that helps the agent decide whether the situation is obvious, complicated, complex, chaotic, or still disordered.

**Use it when:** The first question is not "what do I do?" but "what kind of problem is this, and what response style fits it?"

**Best for:** Task routing, incident routing, skill-stack selection, project kickoff diagnosis, and preventing the wrong reasoning mode from dominating the task.

---

### `judgment-and-routing/recognition-primed-triage-skill.md` · [framework]
**What it is:** A fast-judgment skill for urgent situations that tells the agent to recognize the pattern, choose the first plausible strong move, mentally simulate it, and then reassess.

**Use it when:** Delay is costly, information is incomplete, and the agent needs a high-quality first move rather than exhaustive comparison.

**Best for:** Incident triage, outage response, urgent debugging, ops escalation, and fast prioritization under pressure.

---

### `judgment-and-routing/kahneman-thinking-fast-slow-software-agent-skill.md` · [framework]
**What it is:** A judgment skill based on fast versus slow thinking for software engineering work. Uses fast mode for cheap pattern recognition and slow mode for anything expensive, irreversible, ambiguous, or security-sensitive.

**Use it when:** The agent needs to decide when cheap pattern recognition is fine and when slow, careful reasoning is mandatory.

**Best for:** Coding, debugging, estimation, review, ambiguous architecture decisions.

---

### `judgment-and-routing/unsafe-control-actions-hazard-analysis-skill.md` · [framework]
**What it is:** A hazard-analysis skill for checking whether a consequential action becomes unsafe if it is omitted, applied incorrectly, mistimed, misordered, or left in place too long.

**Use it when:** The agent is about to recommend or perform a high-consequence action where timing, sequencing, constraints, and safeguards matter.

**Best for:** Risky automations, infra changes, migrations, data mutations, security-sensitive operations, rollout decisions, and any tool action that changes external state.

---

### `judgment-and-routing/thoroughness-check-etto-skill.md` · [framework]
**What it is:** A conceptual version of the ETTO principle for deciding the right rigor level before work begins.

**Use it when:** You want the judgment of ETTO without a formal gate.

**Best for:** Prompting style, advisory workflows, lightweight preflight reasoning.

---

### `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md` · [protocol]
**What it is:** A universal preflight gate based on the efficiency–thoroughness trade-off. Decides how much evidence is required, whether the agent may act yet, what tools are permitted, and when to stop or escalate.

**Use it when:** The agent should decide how much evidence, validation, and caution are required before acting.

**Best for:** Almost any non-trivial task, especially when risk or irreversibility is involved.

---

### `judgment-and-routing/explore-vs-exploit-skill.md` · [framework]
**What it is:** A conceptual version of the exploration-vs-commitment tradeoff.

**Use it when:** You want the agent to think clearly about search breadth versus action, without a rigid execution protocol.

**Best for:** Planning, ideation, research strategy, lightweight debugging decisions.

---

### `judgment-and-routing/explore-vs-exploit-state-machine-skill.md` · [protocol]
**What it is:** A control system for deciding whether to keep gathering information or commit to action.

**Use it when:** The agent risks either acting too early or searching forever.

**Best for:** Research, debugging, planning, decision support, ambiguous tasks.

---

### `judgment-and-routing/inversion-mental-model-skill.md` · [framework]
**What it is:** A conceptual version of inversion as a reasoning tool for risks, blind spots, and failure modes.

**Use it when:** The agent needs a better strategic lens rather than a formal failure-mapping workflow.

**Best for:** Strategy, critique, planning, pre-mortems, anti-goal analysis.

---

### `judgment-and-routing/inversion-mental-model-state-machine-skill.md` · [protocol]
**What it is:** A protocol for reasoning from failure backward: define the opposite of success, enumerate failure paths, rank them, and turn them into guardrails.

**Use it when:** Risk, blind spots, defensive design, or failure modes matter.

**Best for:** Safety checks, architecture review, incident prevention, rollout planning.

---

### `judgment-and-routing/problem-mode-router-cynefin-state-machine-skill.md` · [protocol]
**What it is:** The protocol version of the Cynefin router. Gates all subsequent work on an explicit, challenged domain classification before any tool use or execution may begin. Enforces the unjustified-Obvious check, mandates evaluation of all five domains, and monitors for reclassification triggers during execution.

**Use it when:** You need domain classification to be an enforced gate, not an optional lens — especially when over-classifying as Obvious is a known risk.

**Best for:** High-stakes task routing, incident classification, skill-stack selection for complex or chaotic situations, any workflow where using the wrong response style would be costly.

---

### `judgment-and-routing/recognition-primed-triage-state-machine-skill.md` · [protocol]
**What it is:** The protocol version of Recognition-Primed Triage. Enforces four gated phases: pattern recognition + confidence declaration, mandatory mental simulation before action, bounded first action within declared scope, and mandatory reassessment before continuing or handing off.

**Use it when:** You need urgent triage to be fast and disciplined — not fast and reckless — and you need the reasoning documented at each gate.

**Best for:** On-call incident response, outage containment, automated incident response workflows, any urgent situation where scope expansion during triage is a known failure mode.

---

### `judgment-and-routing/first-principles-skill.md` · [framework]
**What it is:** A reasoning skill for decomposing problems to their axiomatic constraints before reasoning upward. Separates confirmed facts from inherited assumptions, distinguishes hard constraints from soft ones, and builds solutions from verified foundations rather than from convention or analogy.

**Use it when:** The problem feels intractable because every option has been tried, the framing imports constraints from a prior context that may not apply, or a creative solution requires questioning the problem itself.

**Best for:** Architecture decisions, intractable engineering problems, questioning inherited constraints, situations where the conventional approach is the problem rather than the solution.

---

### `judgment-and-routing/second-order-thinking-skill.md` · [framework]
**What it is:** A consequence-tracing skill that asks "and then what?" at least twice after every first-order effect. Traces how systems, stakeholders, and feedback loops adapt to a change and whether the benefit holds, erodes, or reverses across time horizons.

**Use it when:** A recommendation has a clear first-order benefit but the downstream effects on the system, stakeholders, or incentives have not been traced.

**Best for:** Architecture recommendations, policy changes, process improvements, any decision where the obvious short-term benefit might produce unintended long-term consequences.

---

### `judgment-and-routing/pre-mortem-skill.md` · [framework]
**What it is:** A plan-validation skill based on Gary Klein's prospective hindsight technique. Assumes the plan has already failed and generates specific narrative failure stories from that vantage point, then ranks and converts them into plan adjustments.

**Use it when:** A plan is being finalized before execution and the team or agent has strong consensus that it will work (the highest-risk time for optimism blindness).

**Best for:** Project planning, rollout validation, strategy review, architecture commitment, any plan where consensus has reduced scrutiny.

---

### `judgment-and-routing/pre-mortem-state-machine-skill.md` · [protocol]
**What it is:** The protocol version of the Pre-Mortem. Enforces minimum failure story generation, mandatory ranking, required risk profiles with prevention and detection for top risks, and a formal proceed/adjust/do-not-proceed verdict before execution is unlocked.

**Use it when:** A high-stakes plan requires formal validation and the pre-mortem must be a genuine gate, not a formality.

**Best for:** High-consequence launches, migrations, architectural commitments, any plan where a failed pre-mortem should halt execution.

---

### `judgment-and-routing/six-thinking-hats-skill.md` · [framework]
**What it is:** A multi-perspective analysis skill based on Edward de Bono's *Six Thinking Hats*. Separates White (facts), Red (intuition), Black (caution), Yellow (value), Green (alternatives), and Blue (process) thinking into distinct phases so each mode can operate fully without interference.

**Use it when:** A decision involves multiple stakeholders or perspectives, one reasoning mode (usually caution or optimism) is dominating unfairly, or the agent needs to generate alternatives before evaluating them.

**Best for:** Architecture reviews, stakeholder-sensitive decisions, design proposals, multi-criteria evaluation, any situation where one-mode collapse is a risk.

---

### `judgment-and-routing/steelmanning-skill.md` · [framework]
**What it is:** A commitment-quality skill that requires the agent to build the strongest possible case for the opposing position before finalizing a recommendation. Prevents confirmation bias, distinguishes strawman arguments from genuine alternatives, and requires the residual tension to be named honestly.

**Use it when:** The agent has formed a preference and needs to test it against the best available counter-argument before committing.

**Best for:** Architecture tradeoffs, technology decisions, strategic recommendations, any situation where a genuine alternative exists and the agent is tempted to dismiss it.

---

### `judgment-and-routing/reference-class-forecasting-skill.md` · [framework]
**What it is:** An estimation skill that anchors forecasts to the base rate of similar past projects before applying inside-view reasoning. Corrects for planning fallacy by requiring an explicit reference class, base rate evidence, and evidence-based adjustments rather than optimism-based ones.

**Use it when:** The agent must estimate a timeline, cost, or success probability and the estimate might otherwise be built from the imagined happy path.

**Best for:** Project estimation, sprint planning, migration scoping, any commitment where optimistic inside-view estimates have caused problems before.

---

### `judgment-and-routing/bayesian-updating-skill.md` · [framework]
**What it is:** A belief-management skill for maintaining and updating competing hypotheses as evidence arrives. Prevents over-updating on single data points and under-updating on disconfirming evidence by keeping priors explicit and requiring likelihood assessment for each piece of evidence.

**Use it when:** The agent must reason across multiple observations rather than flipping belief at each signal — debugging, incident analysis, planning under uncertainty, or any multi-step investigation.

**Best for:** Root-cause debugging, incident diagnosis, architecture tradeoff reasoning, planning where beliefs should evolve across evidence rather than reset at each signal.

---

### `judgment-and-routing/cognitive-bias-checklist-skill.md` · [framework]
**What it is:** A post-analysis checklist of the eight biases most dangerous to agents in slow-mode reasoning: anchoring, availability heuristic, confirmation bias, planning fallacy, scope insensitivity, overconfidence, substitution, and narrative fallacy. Requires explicit correction before finalizing any slow-mode output.

**Use it when:** The agent has completed a slow-mode analysis, recommendation, or estimate and needs to verify that these biases have not contaminated the output.

**Best for:** Any slow-mode output — estimates, recommendations, architecture decisions, diagnoses — especially when the output feels obviously correct.

---

## ✨ Output Quality — improving what the agent produces

Skills that refine, critique, and simplify the agent's own outputs.

### `output-quality/bounded-self-revision-skill.md` · [framework]
**What it is:** A disciplined self-refine skill that generates an initial output, critiques it against explicit dimensions, revises it up to two passes, and stops when gains flatten. Prevents endless polish loops, vague self-criticism, and rewriting without improvement.

**Use it when:** The first draft is decent but should improve through one or two structured refinement passes, and you need the revision to stay finite and purposeful.

**Best for:** Writing, planning, structured outputs, explanations, prompts, design memos, decision docs, summaries, and complex reasoning presentations.

---

### `output-quality/tool-interactive-critic-skill.md` · [framework]
**What it is:** A post-generation verification skill based on the CRITIC pattern. Generates an initial output, selects the right external tools to critique it, revises only where tool-grounded evidence demands it, and stops when the major weaknesses are resolved.

**Use it when:** The first draft is plausible but not yet trustworthy, and external tools can materially improve the answer's accuracy or safety.

**Best for:** Factual answers, technical explanations, code review with tests or search, plans that depend on current facts, operational recommendations, and tool-using agent workflows.

---

### `output-quality/cognitive-load-operator-state-machine-skill.md` · [protocol]
**What it is:** A protocol for making outputs easier to understand, retain, and act on. Forces the agent to inspect complexity before output, identify overload sources, choose a lower-load structure, and verify the result is easier to process.

**Use it when:** An answer is technically correct but mentally expensive.

**Best for:** Documentation, workflows, instructions, prompts, onboarding, dense explanations.

---

### `output-quality/feynman-technique-skill.md` · [framework]
**What it is:** A verification skill based on Feynman's teaching philosophy. After generating an explanation, plan, or recommendation, re-explains the core mechanism in plain language to expose gaps. Where the simple explanation breaks down is where the understanding is incomplete.

**Use it when:** The agent has generated an explanation or recommendation and needs to verify it actually understands what it produced — not just that it can recite correct-sounding language.

**Best for:** Explanations, technical documentation, plan verification, complex recommendations where jargon might be masking gaps in reasoning.

---

### `output-quality/mece-pyramid-principle-skill.md` · [framework]
**What it is:** A structure skill based on Barbara Minto's *The Pyramid Principle*. Requires the governing thought to be stated first, supporting arguments to be Mutually Exclusive and Collectively Exhaustive (MECE), and evidence to belong to exactly one argument. Applies the MECE test to identify overlaps and gaps.

**Use it when:** Structuring a complex output — plan, memo, architecture decision, analysis, recommendation — to be complete, non-redundant, and clear.

**Best for:** Strategy memos, architecture decision records, long-form recommendations, any structured analysis where completeness and non-redundancy matter.

---

### `output-quality/tree-of-thoughts-skill.md` · [framework]
**What it is:** A problem-solving skill based on the Tree of Thoughts paper (Yao et al., 2023). Generates multiple candidate reasoning branches, develops each to an intermediate checkpoint, evaluates their promise, prunes weak branches, and pursues only the strongest paths to a conclusion.

**Use it when:** The problem has multiple plausible solution strategies and committing to one too early risks a confident but wrong conclusion.

**Best for:** Complex debugging with multiple competing hypotheses, architecture decisions with multiple viable approaches, any reasoning task where a single path could lead to confident wrongness.

---

### `output-quality/self-consistency-skill.md` · [framework]
**What it is:** A reasoning-verification skill based on the Self-Consistency paper (Wang et al., 2022). Generates multiple independent reasoning chains to the same conclusion, checks whether they converge, and investigates divergence points where the reasoning is uncertain.

**Use it when:** A single reasoning chain has produced a confident-looking conclusion and the stakes are high enough to warrant checking whether independent paths agree.

**Best for:** High-stakes logical deductions, multi-step quantitative reasoning, complex diagnoses, any conclusion where fluent single-path reasoning might mask an underlying uncertainty.

---

### `reasoning/faithfulness-aware-reasoning-skill.md` · [framework]
**What it is:** A reasoning-verification skill that detects faithfulness hallucinations — reasoning that sounds plausible but isn't logically entailed by the premises. Based on arXiv:2602.05897 research on measuring faithfulness in chain-of-thought reasoning.

**Use it when:** The agent produces confident-sounding reasoning that may not actually follow from the stated facts or premises.

**Best for:** Multi-step reasoning, explanations, justifications, any output where logical entailment matters more than rhetorical plausibility.

---

### `reasoning/context-density-operator-skill.md` · [protocol]
**What it is:** A context-management protocol that maximizes decision-relevant information per token. Uses hierarchical memory (always-visible / summarized / reference-table tiers), redundancy elimination, and on-demand expansion to keep the context window dense. Based on GenericAgent (arXiv:2604.17091) and information bottleneck principles.

**Use it when:** The context window is filling during long-horizon tasks, retrieved memories or tool outputs are drowning out decision-relevant info, or you need to preserve reasoning quality while reducing token burn.

**Best for:** Long debugging sessions, multi-step implementation, agent tasks with heavy tool use or memory retrieval.

---

### `reasoning/cot-pruning-reasoning-skill.md` · [protocol]
**What it is:** A chain-of-thought compression protocol that applies two-pass pruning: coarse step-level (does removing this step change the conclusion?) and fine token-level (keep only assertions, key evidence, and logical connectors). Based on CoT-Influx (arXiv:2312.08901) and sufficiency-conciseness trade-off research.

**Use it when:** Chain-of-thought reasoning exceeds 10 steps, contains redundant justifications, or you need to fit more reasoning within a context budget.

**Best for:** Multi-step debugging, complex reasoning tasks, any situation where verbose CoT consumes too much context.

---

### `reasoning/selective-halt-reasoning-skill.md` · [protocol]
**What it is:** An early-stopping protocol that monitors reasoning output for semantic stabilization. Halts after 3 consecutive no-change steps or when halting criteria are met. Based on DASH delta-attention selective halting (arXiv:2604.18103) adapted for agent reasoning.

**Use it when:** Reasoning is converging but continuing to elaborate, token budget is constrained, or you need to know when to stop iterating.

**Best for:** Iterative debugging, convergent reasoning, satisficing problems where "good enough" is acceptable.

---

### `reasoning/token-budget-operator-skill.md` · [protocol]
**What it is:** A master token-efficiency protocol that orchestrates four techniques in sequence: context density maximization (Phase 1), CoT pruning (Phase 2), selective halting (Phase 3), and SOP capture (Phase 4). Designed for long-horizon tasks where token burn is the bottleneck.

**Use it when:** Context window is filling during multi-step tasks, you expect >10 reasoning steps, or you want experience to compound via reusable SOPs.

**Best for:** Complex debugging, multi-step implementation, recurring tasks where similar problems appear repeatedly. The compounding effect means each subsequent similar task gets cheaper as SOPs accumulate.

---

### `output-quality/documentation-craft-skill.md` · [framework]
**What it is:** A structured technical writing skill for generating high-quality documentation. Follows a 5-phase process: outline-first planning, context enrichment, drafting, verification, and refinement. Based on DocAgent multi-agent architecture and literate programming research.

**Use it when:** Writing README files, API documentation, architecture decision records, or any technical documentation where clarity and completeness matter.

**Best for:** Repository documentation, API docs, complex function/class documentation, architecture explanations, onboarding guides.

---

### `output-quality/large-documentation-navigation-skill.md` · [framework]
**What it is:** A skill for transforming unwieldy documentation repositories into navigable, user-centered knowledge bases. Builds multi-layered navigation systems that help users find what they need based on their situation, not just categorical listings.

**Use it when:** Documentation has grown beyond 20+ items, users report "can't find anything", or the README is just a long list without situational guidance.

**Best for:** Large skill catalogs, extensive API documentation, multi-module project documentation, any reference library where users think in tasks, not categories.

|---


### `systems-and-architecture/the-goal-theory-of-constraints-ai-skill.md` · [framework]
**What it is:** A throughput and bottleneck lens based on Theory of Constraints. Every system has a limiting constraint; identify, exploit, and elevate it before optimizing anything else.

**Use it when:** The agent must improve performance or delivery by finding the real limiting factor rather than optimizing everything.

**Best for:** Performance tuning, workflow optimization, queue reduction, system throughput improvement.

---

### `systems-and-architecture/team-topologies-ai-skill.md` · [framework]
**What it is:** A coordination and ownership lens for multi-agent or multi-team systems. Enforces bounded ownership, clear interaction modes, cognitive load control, and stream-aligned delivery.

**Use it when:** The problem is less about one task and more about how work should be split, owned, and coordinated.

**Best for:** Multi-agent systems, platform teams, ownership design, reducing coordination chaos.

---

### `systems-and-architecture/accelerate-ai-skill.md` · [framework]
**What it is:** A delivery and reliability lens inspired by Accelerate-style thinking. Optimizes flow, stability, and feedback together; measures what matters; prefers capability improvements over vanity activity.

**Use it when:** The agent must improve engineering throughput, feedback loops, reliability, or team productivity using evidence rather than folklore.

**Best for:** Delivery metrics, operational improvement, recovery time reduction, batch-size reduction.

---

### `systems-and-architecture/designing-data-intensive-applications-ai-skill.md` · [framework]
**What it is:** A data-systems reasoning lens inspired by DDIA. Reasons about consistency, replication, partitioning, failure modes, and data flow choices consciously.

**Use it when:** The agent must reason about storage, distributed systems, consistency, replication, partitioning, messaging, or reliability tradeoffs.

**Best for:** Backends, data architecture, infra design, state management, event-driven systems.

---

### `systems-and-architecture/domain-driven-design-skill.md` · [framework]
**What it is:** A domain-modeling lens based on Eric Evans' *Domain-Driven Design*. Identifies bounded contexts, ubiquitous language gaps, aggregate boundaries, domain events, and anti-corruption layer needs. Maps how contexts relate (shared kernel, customer-supplier, conformist, ACL) and aligns system structure to domain structure.

**Use it when:** The agent must make architecture decisions about service or module boundaries, ownership, or integration patterns — especially when the existing structure has drifted from the domain it serves.

**Best for:** Service decomposition, modular monolith design, API contract design, team boundary alignment, legacy system restructuring around domain concerns.

---

### `systems-and-architecture/release-it-stability-skill.md` · [framework]
**What it is:** A production-resilience lens based on Michael Nygard's *Release It!*. Checks every integration point for circuit breakers, timeouts, and bulkheads; identifies unbounded accumulations that cause time-deferred failure; verifies fail-fast, load-shedding, and steady-state patterns are present.

**Use it when:** The agent is designing or reviewing a distributed system and needs to verify it is stable under failure conditions, not just under normal operation.

**Best for:** Distributed system architecture review, third-party integration design, production readiness assessment, post-incident architecture analysis.

---

### `systems-and-architecture/sre-error-budget-skill.md` · [framework]
**What it is:** A reliability-governance lens based on Google's *Site Reliability Engineering* book. Defines SLIs and SLOs at the right level, calculates error budgets, and enforces a release policy: spend the budget on velocity when healthy, freeze non-critical changes when depleted. Includes toil assessment and automation targeting.

**Use it when:** The agent must reason about the tradeoff between reliability and deployment velocity — making that tradeoff explicit, measurable, and governed rather than implicit and conflict-driven.

**Best for:** Deployment decisions, change-freeze recommendations, reliability target setting, on-call sustainability improvement, post-incident policy review.

---

## 🤖 Orchestration — agent coordination and workflow control

Skills for structuring how agents plan, route, delegate, and control complex workflows.

### `orchestration/agentic-design-patterns-orchestrator-skill.md` · [framework]
**What it is:** A conceptual version of the orchestration skill focused on planning, routing, deliberate tool use, reflection, memory, sub-agents, and human-in-the-loop behavior.

**Use it when:** You want the agent to reason with agentic patterns without necessarily enforcing a strict protocol.

**Best for:** Strategy design, agent architecture thinking, early-stage workflow design.

---

### `orchestration/agentic-design-patterns-orchestrator-state-machine-skill.md` · [protocol]
**What it is:** A workflow-control skill for tasks that need classification, planning, routing, evidence gathering, execution, reflection, verification, and stopping.

**Use it when:** The agent should behave like an orchestrated system, not a one-shot responder.

**Best for:** Multi-step tasks, sub-agent coordination, tool-using workflows, bounded execution.

---

### `orchestration/socratic-clarification-skill.md` · [protocol]
**What it is:** A pre-execution clarification protocol. Maps the agent's assumptions explicitly, identifies the single most critical assumption whose failure would redirect the work, formulates one targeted clarifying question, and gates execution on the answer — or requires the ambiguity to be explicitly accepted with stated reasoning.

**Use it when:** The agent is about to execute an ambiguous or high-stakes task where confident wrong execution is the primary failure risk.

**Best for:** Any task where the user's intent, scope, or constraints are ambiguous; high-stakes actions where wrong-direction execution has significant cost; recurring tasks where assumptions about context have caused rework before.

---

### `orchestration/separation-of-concerns-skill.md` · [framework]
**What it is:** An orchestration-discipline skill based on Dijkstra's Separation of Concerns principle. Explicitly separates planning from execution, diagnosis from remediation, observation from interpretation, and design from review — so that concerns in one phase do not contaminate the reasoning or side effects of another.

**Use it when:** A multi-step task is producing confused or contaminated output because different kinds of work are happening simultaneously, or the agent is diagnosing and fixing at the same time.

**Best for:** Multi-step complex tasks, debugging workflows where diagnosis and remediation have been mixed, long orchestrations where scope drift is a risk.

---

### `orchestration/agent-memory-hygiene-skill.md` · [framework]
**What it is:** A memory-management skill for agents that have cross-session memory or stored context. Categorizes stored items by durability and trust level (durable fact / working context / provisional belief / decision + rationale), applies staleness signals when retrieving, and ensures stored decisions include their rationale and the conditions under which they should be revisited.

**Use it when:** The agent has access to stored context from prior sessions and needs to decide what to trust, what to re-verify, and what to prune.

**Best for:** Long-running agent workflows with cross-session memory, recurring task agents that accumulate context, any workflow where over-trusting stale memory has caused errors.


---

### `orchestration/sop-evolution-memory-skill.md` · [protocol]
**What it is:** A trajectory-distillation protocol that turns successful task executions into reusable Standard Operating Procedures (SOPs). Future similar tasks load the compact SOP (500 tokens) instead of the full trajectory (3000+ tokens). Includes indexing, retrieval, and quality gates. Based on GenericAgent self-evolution (arXiv:2604.17091).

**Use it when:** You repeatedly solve similar tasks, previous trajectories contain reusable patterns, or context budget is too tight to load full historical traces.

**Best for:** Recurring debugging patterns, repeated implementation workflows, any domain where experience should compound rather than reset each session.

---

### `orchestration/monte-carlo-tree-search-skill.md` · [framework]
**What it is:** A branch-allocation skill based on Monte Carlo Tree Search (MCTS). Generates distinct candidate branches, spends more effort on branches that earn it through evidence, preserves limited exploration to avoid early lock-in, and uses bounded probes instead of full commitment too early.

**Use it when:** Multiple plausible strategies exist and the agent needs a disciplined way to decide which branch deserves more reasoning, testing, or tool budget.

**Best for:** Hard debugging, refactor-path selection, architecture tradeoffs, repo-scale investigations, and tool-using agents with measurable feedback.

---

### `orchestration/thought-retriever-coppermind-skill.md` · [protocol]
**What it is:** A memory-augmented reasoning skill that stores structured "thoughts" (observations, inferences, hypotheses, uncertainties, conclusions) in the Coppermind three-layer memory system. Enables sub-agents to retrieve not just raw data but the reasoning traces of prior agents.

**Use it when:** You want agents to build collective memory across sessions, learn from each other's problem-solving approaches, or retrieve "how we thought about this" not just "what we concluded."

**Best for:** Complex debugging, research tasks, design decisions, and cross-session work where reasoning context matters as much as answers.

**Key technique:** From "Thought-Retriever: Don't Just Retrieve Raw Data, Retrieve Thoughts" (arXiv:2604.12231) — maps thoughts to Coppermind's working/episodic/semantic layers with confidence scoring and access-based liveness.

---

### `orchestration/weak-link-detection-multi-agent-skill.md` · [protocol]
**What it is:** A multi-agent quality control protocol that identifies and isolates the weakest reasoning chain before aggregation. Prevents error amplification when one agent produces poor output.

**Use it when:** Coordinating multiple agents where one bad output could contaminate the final result.

**Best for:** Multi-agent systems, ensemble reasoning, voting/agreement mechanisms, any setup where agent outputs need quality filtering before combination.

---

### `orchestration/rashomon-triad-hybrid-skill.md` · [protocol]
**What it is:** A multi-perspective structured reasoning system combining Rashomon Memory (parallel goal-conditioned perspectives that maintain conflicting interpretations) with Triad Reasoning (abductive hypothesis generation → deductive verification → inductive pattern extraction). Perspectives argue via structured argumentation; Dung's semantics determines winners.

**Use it when:** Multiple stakeholders have genuinely conflicting goals, the decision has no single "correct" answer, or you need to surface and document why alternatives were rejected rather than hiding conflict behind false consensus.

**Best for:** Architecture reviews with trade-offs, security vs performance decisions, high-stakes choices where "it depends" is the honest answer.

**Key techniques:** From "Rashomon Memory" (arXiv:2604.03588) and "Structured Abductive-Deductive-Inductive Reasoning" (arXiv:2604.15727) — supports three output modes: selection (pick winner), composition (merge non-conflicting), conflict surfacing (return attack graph as explanation).

---

### Power Combinations

- **Tree of Thoughts + Monte Carlo Tree Search** → generate diverse branches first, then allocate deeper effort to the branches that earn it through evidence rather than equal exploration or first-branch lock-in

- **Thought-Retriever + Coppermind** → store reasoning traces, not just outputs; retrieve "how we solved this" for future similar problems

- **Rashomon-Triad Hybrid** → spawn parallel perspectives with conflicting goals; let them argue; surface the conflict graph as explanation

- **Metacognitive Monitoring + Compression** → force explicit confidence calibration, then verify understanding by compressing to essence

- **Abductive Debugging + Logic Locator** → debug by generating competing hypotheses, then locate code structurally without keyword matching

- **Everything-as-Code** → codify messy human problems to reveal hidden assumptions and structure

- **Counterfactual Policy Testing** → validate decisions by testing against explicit alternatives (null, opposite, partial) before committing

- **Cognitive Friction Governor** → impose deliberation budgets with friction costs per operation, forcing bounded purposeful thinking

- **Cross-Domain Analogy Generator** → break fixation by forcing structural analogies from unrelated domains (biology, music, traffic)

- **Skill Development with Supporting Files** → workflow for creating skills that need external scripts, templates, or data files

---

### `judgment-and-routing/counterfactual-policy-testing-skill.md` · [protocol]
**What it is:** A decision-validation protocol that tests proposed changes against three explicit counterfactuals — null (do nothing), opposite (do reverse), partial (do 50%) — and only proceeds if the change beats all alternatives.

**Use it when:** Before significant code changes, when multiple solutions seem plausible, or when you need to prevent "we did X, therefore X caused Y" fallacies.

**Key technique:** From counterfactual reasoning research (arXiv:2604.10511) — forces comparison against explicit alternatives rather than assuming the proposed path is optimal.

---

### `execution/cognitive-friction-governor-skill.md` · [protocol]
**What it is:** A deliberation budgeting system that assigns "friction costs" to cognitive operations (search=1, read=2, analysis=10, etc.). When budget is exhausted, you must decide or explicitly request more budget with justification.

**Use it when:** You tend to over-think trivial problems or under-think complex ones, or when analysis paralysis is a recurring issue.

**Key technique:** From "Cognitive Friction: A Decision-Theoretic Framework for Bounded Deliberation" (arXiv:2603.30031) — friction forces trade-offs between deep analysis and quick action.

---

### `systems-and-architecture/cross-domain-analogy-generator-skill.md` · [framework]
**What it is:** A creative problem-solving lens that breaks fixation by forcing structural analogies from unrelated domains (biology, music, traffic engineering, cooking). Maps problem structures to foreign frameworks and transfers insights.

**Use it when:** Stuck on a problem with repeated failed attempts, when local optima seem like global optima, or when you need "fresh eyes" on a familiar problem.

**Key technique:** From "Serendipity by Design" (arXiv:2603.19087) — cross-domain mappings stimulate creativity by importing foreign structural patterns.

---

### `development/skill-development-with-supporting-files.md` · [framework]
**What it is:** A workflow guide for developing skills that require supporting files beyond the main `.md` file — such as Python scripts, templates, or reference documents. Documents the manual steps required because `npx jerry-skills install` only copies `.md` files.

**Use it when:** Your skill needs external scripts, tools, or data files that must be installed alongside the skill document.

**Key learning:** From developing `keyword-agnostic-logic-locator` — supporting scripts in `scripts/` must be manually copied to `~/.copilot/skills/scripts/` after skill installation.

---

### `development/add-new-skill-to-repository/SKILL.md` · [framework]
**What it is:** A process guide for adding new skills to Jerry's Agent Skills repository with proper documentation, installation support, and cross-platform verification.

**Use it when:** You want to contribute a new skill to this repository.

**Best for:** Skill creation, documentation standards, installer compatibility testing.


---

### `judgment-and-routing/metacognitive-monitoring-skill.md` · [protocol]
**What it is:** A confidence calibration protocol forcing agents to explicitly decide KEEP or WITHDRAW their output, and BET or decline — based on the Nelson-Narens metacognitive monitoring framework. Tracks "withdraw delta" to distinguish blanket confidence from selective sensitivity.

**Use it when:** You need to know when the agent knows it doesn't know — before committing to high-stakes code changes, for selective prediction, or when overconfidence is the primary failure mode.

**Key technique:** From "The Metacognitive Monitoring Battery" (arXiv:2604.15702) — dual-probe methodology adapted for LLM self-evaluation.

---

### `execution/keyword-agnostic-logic-locator-skill.md` · [protocol]
**What it is:** A neurosymbolic code navigation system that extracts program facts (call graphs, data flows, type hierarchies) into a queryable knowledge graph, then uses Datalog-style logic queries to locate code by structural relationships — not by grepping for names.

**Use it when:** Function names are unclear or misleading, you need to find code by "what it does" not "what it's called," or keyword search returns too much noise.

**Key technique:** From "Neurosymbolic Repo-level Code Localization" (arXiv:2604.16021) — addresses the "Keyword Shortcut" problem with Python scripts for fact extraction and logic query execution.

**Includes:** `scripts/extract_code_facts.py` and `scripts/query_code_facts.py`

---

### `execution/abductive-first-debugging-skill.md` · [protocol]
**What it is:** A debugging protocol that generates multiple competing hypotheses and selects the one providing the *best explanation* for all observed symptoms — inference to best explanation rather than first-plausible-cause or pattern-matching.

**Use it when:** Novel failures with no established pattern, symptoms that could have multiple causes, deductive tracing hits dead ends, or complex multi-system failures.

**Key technique:** From "Wiring the 'Why': A Unified Taxonomy of Abductive Reasoning in LLMs" (arXiv:2604.08016) — separates abduction (hypothesis generation), explanatory coherence evaluation, and inference to best explanation.

---

### `systems-and-architecture/everything-as-code-conceptualizer-skill.md` · [framework]
**What it is:** A conceptual lens that forces viewing any system, process, or problem through a "code lens" — writing pseudocode to represent team dynamics, unclear requirements, deployment issues, or knowledge gaps. The act of codification reveals hidden structure and assumptions.

**Use it when:** Messy human/process problems resist structured analysis, you need to surface hidden assumptions, or "if only we had clear specs" is being said.

**Key technique:** From "Understanding Everything as Code: A Taxonomy and Conceptual Model" (arXiv:2507.05100) — codifying forces precision that natural language obscures.

---

### `output-quality/compression-as-understanding-skill.md` · [protocol]
**What it is:** A verification protocol that tests understanding by compressing knowledge into minimal essential form (≤10 sentences), then testing if that compressed representation can reconstruct key details. High compression ratio = deep understanding.

**Use it when:** After exploring a large codebase to verify understanding, before explaining complex systems, or when you need to distinguish "familiar with" from "understands."

**Key technique:** Based on Kolmogorov complexity — the shortest program that generates output measures true understanding.

---


## 🛠️ Development — skill building

Skills for creating skills, integrating external systems, and development workflows.

### `software-development/verify-before-integrate-skill.md` · [framework]
**What it is:** A verification skill for integrating research paper concepts, API documentation, or external system descriptions into implementations. Verifies actual system behavior rather than assuming terminology alignment — names that sound similar often refer to different implementations.

**Use it when:** Writing a skill that connects to an existing system (Coppermind, Convex, Supabase, etc.), implementing a research paper's algorithm, or mapping abstract concepts to concrete APIs or database schemas.

**Best for:** Integration documentation, skill development, API mapping, system integration where terminology might not match the abstract description.

---

### `software-development/debug-issue.md` · [protocol]
**What it is:** A structured debugging workflow that forces reproduce, isolate, fix, verify steps.

**Use it when:** You need to track down a bug methodically instead of guessing.

**Best for:** Reproducing issues, isolating root cause, verified fixes.

---

### `software-development/explore-codebase.md` · [framework]
**What it is:** A structured exploration skill for understanding unfamiliar codebases through progressive deepening.

**Use it when:** You need to understand a new repo, module, or system before making changes.

**Best for:** Onboarding to new codebases, understanding architecture, mapping dependencies.

---

### `software-development/refactor-safely.md` · [protocol]
**What it is:** A safe refactoring skill built around characterization testing and bounded changes.

**Use it when:** You need to improve code structure without breaking existing behavior.

**Best for:** Incremental refactoring, legacy code improvement, structural cleanup.

---

### `software-development/review-changes.md` · [framework]
**What it is:** A structured code review checklist for reviewing changes systematically.

**Use it when:** You need to review a PR, diff, or set of changes with consistent coverage.

**Best for:** Pull request reviews, change verification, catching missed issues.

---

### `mlops/local-llm-tooling/SKILL.md` · [framework]
**What it is:** A workflow for running, prompting, and extracting structured output from local LLMs (e.g., Ollama, llama.cpp).

**Use it when:** You need to run an LLM locally for agent tasks, data extraction, or generation, and want to avoid API rate limits, costs, or privacy concerns.

**Best for:** Local LLM tooling, structured output extraction, model switching.

---

### `testing/skill-ab-evaluation/SKILL.md` · [protocol]
**What it is:** A/B evaluate any jerrysagentskill against a baseline using isolated subagents, 5 trials each, and an objective rubric.

**Use it when:** You want empirical proof that a skill actually improves outcomes vs. general knowledge.

**Best for:** Skill quality benchmarking, evidence-based skill curation, measuring ROI of structured prompts.
