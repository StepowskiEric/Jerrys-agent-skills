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

# Recommended Ways to Use This Repo

## If you want execution discipline
Start with the protocol skills, especially:

- `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md`
- `execution/how-to-solve-it-state-machine-skill.md`
- `execution/refactoring-state-machine-skill.md`
- `execution/working-effectively-with-legacy-code-state-machine-skill.md`
- `execution/toyota-kata-state-machine-skill.md`

## If you want better judgment or routing
Start with the framework skills, especially:

- `judgment-and-routing/problem-mode-router-cynefin-skill.md`
- `judgment-and-routing/recognition-primed-triage-skill.md`
- `judgment-and-routing/unsafe-control-actions-hazard-analysis-skill.md`
- `systems-and-architecture/thinking-in-systems-state-machine-skill.md`
- `systems-and-architecture/the-goal-theory-of-constraints-ai-skill.md`
- `judgment-and-routing/kahneman-thinking-fast-slow-software-agent-skill.md`

## If you want better output quality
These skills refine the agent's own work:

- `output-quality/bounded-self-revision-skill.md` — structured self-improvement with stop rules
- `output-quality/tool-interactive-critic-skill.md` — tool-grounded post-generation verification
- `output-quality/cognitive-load-operator-state-machine-skill.md` — reduce mental burden in any output

## If you are building higher-quality agent workflows
Strong combinations include:

- **ETTO + Problem-Mode Router** → decide rigor level and response mode first
- **Recognition-Primed Triage + Unsafe Control Actions** → move fast, but with guardrails
- **How to Solve It + Pragmatic Programmer** → disciplined diagnosis plus grounded execution
- **Working Effectively with Legacy Code + Refactoring** → make change safe, then improve structure
- **Thinking in Systems + Theory of Constraints** → understand the system, then find the true bottleneck
- **Toyota Kata + Cognitive Load Operator** → iterative improvement plus communication clarity
- **Bounded Self-Revision + Tool-Interactive Critic** → self-refine first, then verify with external tools

## If you are unsure where to begin
A practical default sequence is:

1. `judgment-and-routing/problem-mode-router-cynefin-skill.md`
2. `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md`
3. one task-specific protocol or framework from the relevant topic folder
4. `output-quality/tool-interactive-critic-skill.md` if the output depends on facts or code that can be externally checked
5. `execution/toyota-kata-state-machine-skill.md` if the goal is iterative improvement rather than one-shot change

---

# Installation

Install all skills directly to your agent's configuration directory using `npx`:

```bash
npx jerry-skills install --all
```

Or target a specific agent:

```bash
npx jerry-skills install --agent codex       # → ~/.codex/skills/
npx jerry-skills install --agent hermes      # → ~/.hermes/skills/
npx jerry-skills install --agent claude      # → ~/.claude/skills/
npx jerry-skills install --agent antigravity # → ~/.antigravity/skills/
```

Use a custom destination:

```bash
npx jerry-skills install --agent codex --dest /path/to/custom/dir
```

List skills without installing:

```bash
npx jerry-skills list
```

Each command copies all `.md` skill files from this repository into the target directory. From there you can reference or load them in your agent's system prompt or skill loader.

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
