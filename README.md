# Jerry's Agent Skills

A catalog of agent skills for making AI systems more reliable, disciplined, and useful in real work.

## Quick Install

Install all skills directly to your agent's configuration directory:

```bash
# Install to all supported agents
npx jerry-skills install --all

# Install to a specific agent
npx jerry-skills install --agent codex
npx jerry-skills install --agent hermes
npx jerry-skills install --agent claude
npx jerry-skills install --agent antigravity

# List available skills without installing
npx jerry-skills list
```

See [Installation](#installation) for full details.

---

This repository contains **two kinds of skills**:

1. **Operational protocols** — skills that act like procedures or control systems.
   These often benefit from a state-machine structure because the value is in gating behavior, forcing evidence collection, and preventing premature action.

2. **Conceptual frameworks** — skills that act more like lenses, heuristics, routing models, or architectural principles.
   These do **not** always need to be state machines. In many cases, forcing them into a rigid protocol makes them worse: more ceremonial, less adaptable, and less readable.

## Not every skill should be a state machine

A state-machine format makes sense when you want the agent to:

- follow a repeatable sequence
- respect tool-gating by phase
- create mandatory diagnostic artifacts
- stop when a condition is met
- avoid looping, over-searching, or reckless execution
- behave consistently on risky or multi-step tasks

A non-state-machine format makes sense when you want the agent to:

- adopt a way of seeing a problem
- reason about tradeoffs
- borrow principles from a book or framework
- improve judgment rather than enforce a workflow
- route the task into the correct response mode
- adapt the ideas fluidly to many contexts

The strongest repositories usually have **both**:

- **protocol skills** for execution discipline
- **framework skills** for better judgment

## How to choose between versions

Some concepts in this repo have both a classic/conceptual version and a state-machine version.

Use the **conceptual version** when:

- you want the idea as a reasoning lens
- the task is exploratory or educational
- the agent needs flexibility more than strict gating

Use the **state-machine version** when:

- the task is risky, expensive, or multi-step
- you need predictable behavior
- you want mandatory artifacts, stop conditions, and clearer auditability

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

### `execution/how-to-solve-it-analogy-skill.md` · [framework]
**What it is:** A transfer-reasoning skill based on Polya's analogy technique from *How to Solve It*. Finds structural analogs to the current problem, makes the mapping explicit, identifies what transfers and what does not, and adapts the imported solution structure.

**Use it when:** The problem resembles a previously solved one and importing the solution structure would accelerate the work — but only after verifying the mapping holds.

**Best for:** Design decisions, algorithm selection, architecture patterns, any problem where a known solution from another domain is structurally applicable.

---

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

## 🏗️ Systems & Architecture — thinking about structure and scale

Skills for reasoning about how systems, teams, and data fit together.

### `systems-and-architecture/thinking-in-systems-state-machine-skill.md` · [protocol]
**What it is:** A protocol for mapping system boundaries, stocks, flows, loops, delays, leverage points, and blast radius before changing anything.

**Use it when:** The problem involves feedback loops, delayed effects, or second-order consequences.

**Best for:** Architecture, workflows, scaling problems, process failures, policy changes.

---

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


### `orchestration/monte-carlo-tree-search-skill.md` · [framework]
**What it is:** A branch-allocation skill based on Monte Carlo Tree Search (MCTS). Generates distinct candidate branches, spends more effort on branches that earn it through evidence, preserves limited exploration to avoid early lock-in, and uses bounded probes instead of full commitment too early.

**Use it when:** Multiple plausible strategies exist and the agent needs a disciplined way to decide which branch deserves more reasoning, testing, or tool budget.

**Best for:** Hard debugging, refactor-path selection, architecture tradeoffs, repo-scale investigations, and tool-using agents with measurable feedback.

---

- **Tree of Thoughts + Monte Carlo Tree Search** → generate diverse branches first, then allocate deeper effort to the branches that earn it through evidence rather than equal exploration or first-branch lock-in

---

# Recommended Ways to Use This Repo

## If you want execution discipline
Start with the protocol skills, especially:

- `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md`
- `execution/how-to-solve-it-state-machine-skill.md`
- `execution/refactoring-state-machine-skill.md`
- `execution/working-effectively-with-legacy-code-state-machine-skill.md`
- `execution/toyota-kata-state-machine-skill.md`
- `execution/checklist-manifesto-skill.md`
- `execution/ooda-loop-state-machine-skill.md`

## If you want better judgment or routing
Start with the framework skills, especially:

- `judgment-and-routing/problem-mode-router-cynefin-skill.md`
- `judgment-and-routing/recognition-primed-triage-skill.md`
- `judgment-and-routing/unsafe-control-actions-hazard-analysis-skill.md`
- `judgment-and-routing/first-principles-skill.md`
- `judgment-and-routing/second-order-thinking-skill.md`
- `systems-and-architecture/thinking-in-systems-state-machine-skill.md`
- `systems-and-architecture/the-goal-theory-of-constraints-ai-skill.md`
- `judgment-and-routing/kahneman-thinking-fast-slow-software-agent-skill.md`

## If you want better output quality
These skills refine the agent's own work:

- `output-quality/bounded-self-revision-skill.md` — structured self-improvement with stop rules
- `output-quality/tool-interactive-critic-skill.md` — tool-grounded post-generation verification
- `output-quality/cognitive-load-operator-state-machine-skill.md` — reduce mental burden in any output
- `output-quality/feynman-technique-skill.md` — verify understanding by explaining simply
- `output-quality/mece-pyramid-principle-skill.md` — structure outputs to be complete and non-redundant
- `output-quality/tree-of-thoughts-skill.md` — explore multiple reasoning paths before committing
- `output-quality/self-consistency-skill.md` — triangulate conclusions across independent reasoning chains

## If you are building higher-quality agent workflows
Strong combinations include:

- **ETTO + Problem-Mode Router** → decide rigor level and response mode first
- **Cynefin State Machine + Recognition-Primed Triage State Machine** → classify the domain, then apply the correct triage protocol
- **Recognition-Primed Triage + Unsafe Control Actions** → move fast, but with guardrails
- **How to Solve It + Pragmatic Programmer** → disciplined diagnosis plus grounded execution
- **How to Solve It + Analogy Transfer** → problem-framing with analog import when a prior solution exists
- **Working Effectively with Legacy Code + Refactoring** → make change safe, then improve structure
- **Thinking in Systems + Theory of Constraints** → understand the system, then find the true bottleneck
- **Toyota Kata + PDCA** → discover the obstacle, then verify the improvement with measurement discipline
- **OODA Loop + Checklist Manifesto** → dynamic tempo in fast-moving situations, procedural discipline in high-stakes steps
- **Pre-Mortem + Inversion** → vivid failure stories plus abstract failure-mode analysis, before committing to a plan
- **Six Thinking Hats + Steelmanning** → multi-perspective analysis plus genuine challenge of the leading recommendation
- **Kahneman Fast/Slow + Cognitive Bias Checklist** → switch to slow mode, then verify the slow-mode output is bias-corrected
- **DDD + Team Topologies** → align domain boundaries to team structures
- **Release It! + SRE Error Budget** → implement stability patterns, then govern the reliability-velocity tradeoff
- **Socratic Clarification + Pre-Mortem** → surface the key assumption before planning, then validate the plan against failure
- **Bounded Self-Revision + Tool-Interactive Critic** → self-refine first, then verify with external tools
- **Feynman Technique + MECE / Pyramid Principle** → verify the reasoning is sound, then structure the output clearly

## Practical skill flows
Use these as default stacks when the task matches the scenario.

### Extremely difficult debugging
1. `judgment-and-routing/problem-mode-router-cynefin-skill.md`
2. `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md`
3. `execution/how-to-solve-it-state-machine-skill.md`
4. `judgment-and-routing/explore-vs-exploit-state-machine-skill.md`
5. `execution/ooda-loop-state-machine-skill.md` if the situation is changing while you investigate
6. `output-quality/tool-interactive-critic-skill.md` to verify the conclusion against code, logs, or tests

Why this stack works: classify the problem first, set the rigor bar, force disciplined diagnosis, then keep evidence and action in a tight loop.

### New architecture or major design decisions
1. `judgment-and-routing/problem-mode-router-cynefin-skill.md`
2. `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md`
3. `judgment-and-routing/first-principles-skill.md`
4. `systems-and-architecture/thinking-in-systems-state-machine-skill.md`
5. `systems-and-architecture/domain-driven-design-skill.md`
6. `systems-and-architecture/team-topologies-ai-skill.md`
7. `judgment-and-routing/pre-mortem-skill.md`
8. `judgment-and-routing/inversion-mental-model-skill.md`

Why this stack works: it separates problem classification from design, then forces boundary, coupling, and failure-mode analysis before committing.

### Large refactor or cleanup of bad code
1. `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md`
2. `execution/working-effectively-with-legacy-code-state-machine-skill.md`
3. `execution/refactoring-state-machine-skill.md`
4. `execution/pragmatic-programmer-state-machine-skill.md`
5. `execution/checklist-manifesto-skill.md` if the change is risky or procedural
6. `output-quality/tool-interactive-critic-skill.md` before claiming the work is done

Why this stack works: stabilize first, refactor in bounded slices, keep the blast radius explicit, and verify before closure.

### Following strong principles while deciding
1. `judgment-and-routing/first-principles-skill.md`
2. `judgment-and-routing/second-order-thinking-skill.md`
3. `judgment-and-routing/kahneman-thinking-fast-slow-software-agent-skill.md`
4. `judgment-and-routing/cognitive-bias-checklist-skill.md`
5. `output-quality/mece-pyramid-principle-skill.md`
6. `output-quality/feynman-technique-skill.md`

Why this stack works: it pushes the agent to reason from basics, check downstream effects, slow down when needed, and present the result clearly.

### Fast-moving incident or urgent operational work
1. `judgment-and-routing/problem-mode-router-cynefin-skill.md`
2. `judgment-and-routing/recognition-primed-triage-skill.md`
3. `execution/ooda-loop-state-machine-skill.md`
4. `judgment-and-routing/unsafe-control-actions-hazard-analysis-skill.md`
5. `execution/checklist-manifesto-skill.md`

Why this stack works: classify the situation, take the first plausible strong move, then stay disciplined about timing, sequence, and safeguards.

### Better output quality or sharper reasoning
1. `output-quality/tree-of-thoughts-skill.md`
2. `output-quality/self-consistency-skill.md`
3. `output-quality/bounded-self-revision-skill.md`
4. `output-quality/tool-interactive-critic-skill.md`
5. `output-quality/mece-pyramid-principle-skill.md`
6. `output-quality/feynman-technique-skill.md`

Why this stack works: it broadens the search space, triangulates conclusions, then tightens the result into a clear and testable answer.

## If you are unsure where to begin
A practical default sequence is:

1. `judgment-and-routing/problem-mode-router-cynefin-skill.md`
2. `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md`
3. `orchestration/socratic-clarification-skill.md` if the task is ambiguous
4. one task-specific protocol or framework from the relevant topic folder
5. `output-quality/tool-interactive-critic-skill.md` if the output depends on facts or code that can be externally checked
6. `execution/toyota-kata-state-machine-skill.md` if the goal is iterative improvement rather than one-shot change

---

# Installation

Install all skills directly to your agent's configuration directory using `npx`:

```bash
npx jerry-skills install --all
```

Or target a specific agent:

```bash
npx jerry-skills install --agent codex       # → ~/.agents/skills/
npx jerry-skills install --agent hermes      # → ~/.hermes/skills/
npx jerry-skills install --agent claude      # → ~/.claude/skills/
npx jerry-skills install --agent antigravity # → ~/.antigravity/skills/
```

To make the skills show up in a Codex repository workspace, install them into the repo-local Team Config path:

```bash
npx jerry-skills install --agent codex --dest .agents/skills
```

Use a custom destination:

```bash
npx jerry-skills install --agent codex --dest /path/to/custom/dir
```

List skills without installing:

```bash
npx jerry-skills list
```

Each command copies every skill into a folder bundle with a `SKILL.md` file, and Codex bundles include `name` and `description` frontmatter so they are discoverable in the skills picker. For example, `execution/how-to-solve-it-state-machine-skill.md` installs to `execution/how-to-solve-it-state-machine-skill/SKILL.md` under the target directory.

---

# Philosophy of the Repo

This repo should not force one format onto every idea.

The goal is not to make everything look uniform.
The goal is to make each skill **more executable and more useful**.

Some skills become dramatically better when turned into state machines.
Others become worse.

A good agent-skill repository should preserve both:

- **control** where behavior must be constrained
- **judgment** where thinking quality matters more than workflow ceremony

That is the design principle behind this README.
