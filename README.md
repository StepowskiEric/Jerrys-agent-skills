# Jerry's Agent Skills

A catalog of agent skills for making AI systems more reliable, disciplined, and useful in real work.

This repository contains **two kinds of skills**:

1. **Operational protocols** — skills that act like procedures or control systems.
   These often benefit from a state-machine structure because the value is in gating behavior, forcing evidence collection, and preventing premature action.

2. **Conceptual frameworks** — skills that act more like lenses, heuristics, or architectural principles.
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

## Operational Protocols / State-Machine Skills

### 1) `agentic-design-patterns-orchestrator-state-machine-skill.md`
**What it is:** A workflow-control skill for tasks that need classification, planning, routing, evidence gathering, execution, reflection, verification, and stopping.

**Use it when:** The agent should behave like an orchestrated system, not a one-shot responder.

**Best for:** Multi-step tasks, sub-agent coordination, tool-using workflows, bounded execution.

---

### 2) `cognitive-load-operator-state-machine-skill.md`
**What it is:** A protocol for making outputs easier to understand, retain, and act on.

**Use it when:** An answer is technically correct but mentally expensive.

**Best for:** Documentation, workflows, instructions, prompts, onboarding, dense explanations.

---

### 3) `explore-vs-exploit-state-machine-skill.md`
**What it is:** A control system for deciding whether to keep gathering information or commit to action.

**Use it when:** The agent risks either acting too early or searching forever.

**Best for:** Research, debugging, planning, decision support, ambiguous tasks.

---

### 4) `how-to-solve-it-state-machine-skill.md`
**What it is:** A disciplined problem-solving protocol that forces problem framing, evidence gathering, planning, execution, and reflection.

**Use it when:** The task is hard, uncertain, or likely to tempt premature coding.

**Best for:** Debugging, algorithmic reasoning, difficult implementation tasks, root-cause work.

---

### 5) `inversion-mental-model-state-machine-skill.md`
**What it is:** A protocol for reasoning from failure backward: define the opposite of success, enumerate failure paths, rank them, and turn them into guardrails.

**Use it when:** Risk, blind spots, defensive design, or failure modes matter.

**Best for:** Safety checks, architecture review, incident prevention, rollout planning.

---

### 6) `philosophy-of-software-design-state-machine-skill.md`
**What it is:** A protocol for managing complexity, building deeper modules, and avoiding shallow abstraction sprawl.

**Use it when:** The agent is changing shared interfaces or making design decisions that can spread complexity.

**Best for:** API design, module boundaries, simplification, architecture cleanup.

---

### 7) `pragmatic-programmer-state-machine-skill.md`
**What it is:** A practical engineering protocol focused on bounded changes, reversible decisions, automation, and root-cause fixes.

**Use it when:** The agent needs to work like a senior pragmatist instead of an idealist or cleanup maximalist.

**Best for:** Day-to-day engineering work, tooling, repetitive toil reduction, incremental improvements.

---

### 8) `refactoring-state-machine-skill.md`
**What it is:** A bounded refactoring protocol that defines a target, accounts for shared surfaces, limits the transformation budget, and stops cleanly.

**Use it when:** Structure needs improvement but the task could spiral into endless cleanup.

**Best for:** Safe refactors, complexity reduction, targeted cleanup, anti-slop work.

---

### 9) `thinking-in-systems-state-machine-skill.md`
**What it is:** A protocol for mapping system boundaries, stocks, flows, loops, delays, leverage points, and blast radius before changing anything.

**Use it when:** The problem involves feedback loops, delayed effects, or second-order consequences.

**Best for:** Architecture, workflows, scaling problems, process failures, policy changes.

---

### 10) `thoroughness-check-etto-state-machine-skill.md`
**What it is:** A universal preflight gate based on the efficiency–thoroughness trade-off.

**Use it when:** The agent should decide how much evidence, validation, and caution are required before acting.

**Best for:** Almost any non-trivial task, especially when risk or irreversibility is involved.

---

### 11) `working-effectively-with-legacy-code-state-machine-skill.md`
**What it is:** A protocol for making brittle code safe to change before trying to improve it.

**Use it when:** The system has weak tests, unclear behavior, tight coupling, or rewrite temptation.

**Best for:** Characterization testing, seam creation, change safety, legacy modernization.

---

## Conceptual / Framework Skills

### 12) `accelerate-ai-skill.md`
**What it is:** A delivery and reliability lens inspired by Accelerate-style thinking.

**Use it when:** The agent must improve engineering throughput, feedback loops, reliability, or team productivity using evidence rather than folklore.

**Best for:** Delivery metrics, operational improvement, recovery time reduction, batch-size reduction.

---

### 13) `agentic-design-patterns-orchestrator-skill.md`
**What it is:** A conceptual version of the orchestration skill focused on planning, routing, deliberate tool use, reflection, memory, sub-agents, and human-in-the-loop behavior.

**Use it when:** You want the agent to reason with agentic patterns without necessarily enforcing a strict protocol.

**Best for:** Strategy design, agent architecture thinking, early-stage workflow design.

---

### 14) `designing-data-intensive-applications-ai-skill.md`
**What it is:** A data-systems reasoning lens inspired by DDIA.

**Use it when:** The agent must reason about storage, distributed systems, consistency, replication, partitioning, messaging, or reliability tradeoffs.

**Best for:** Backends, data architecture, infra design, state management, event-driven systems.

---

### 15) `explore-vs-exploit-skill.md`
**What it is:** A conceptual version of the exploration-vs-commitment tradeoff.

**Use it when:** You want the agent to think clearly about search breadth versus action, without a rigid execution protocol.

**Best for:** Planning, ideation, research strategy, lightweight debugging decisions.

---

### 16) `inversion-mental-model-skill.md`
**What it is:** A conceptual version of inversion as a reasoning tool for risks, blind spots, and failure modes.

**Use it when:** The agent needs a better strategic lens rather than a formal failure-mapping workflow.

**Best for:** Strategy, critique, planning, pre-mortems, anti-goal analysis.

---

### 17) `kahneman-thinking-fast-slow-software-agent-skill.md`
**What it is:** A judgment skill based on fast versus slow thinking for software engineering work.

**Use it when:** The agent needs to decide when cheap pattern recognition is fine and when slow, careful reasoning is mandatory.

**Best for:** Coding, debugging, estimation, review, ambiguous architecture decisions.

---

### 18) `team-topologies-ai-skill.md`
**What it is:** A coordination and ownership lens for multi-agent or multi-team systems.

**Use it when:** The problem is less about one task and more about how work should be split, owned, and coordinated.

**Best for:** Multi-agent systems, platform teams, ownership design, reducing coordination chaos.

---

### 19) `the-goal-theory-of-constraints-ai-skill.md`
**What it is:** A throughput and bottleneck lens based on Theory of Constraints.

**Use it when:** The agent must improve performance or delivery by finding the real limiting factor rather than optimizing everything.

**Best for:** Performance tuning, workflow optimization, queue reduction, system throughput improvement.

---

### 20) `thoroughness-check-etto-skill.md`
**What it is:** A conceptual version of the ETTO principle for deciding the right rigor level before work begins.

**Use it when:** You want the judgment of ETTO without a formal gate.

**Best for:** Prompting style, advisory workflows, lightweight preflight reasoning.

---

# Recommended Ways to Use This Repo

## If you want execution discipline
Start with the protocol skills, especially:

- `thoroughness-check-etto-state-machine-skill.md`
- `how-to-solve-it-state-machine-skill.md`
- `refactoring-state-machine-skill.md`
- `working-effectively-with-legacy-code-state-machine-skill.md`
- `thinking-in-systems-state-machine-skill.md`

## If you want better judgment and taste
Start with the framework skills, especially:

- `accelerate-ai-skill.md`
- `designing-data-intensive-applications-ai-skill.md`
- `kahneman-thinking-fast-slow-software-agent-skill.md`
- `team-topologies-ai-skill.md`
- `the-goal-theory-of-constraints-ai-skill.md`

## If you want both
A strong pattern is:

1. Use a **framework skill** to decide how to see the problem.
2. Use a **protocol skill** to control how the agent executes.

Example combinations:

- **Kahneman + ETTO** → pick the right speed and rigor
- **Thinking in Systems + Refactoring** → understand system effects before changing code
- **The Goal + Explore vs Exploit** → find the bottleneck, then decide whether to keep searching or act
- **Team Topologies + Agentic Orchestrator** → design multi-agent boundaries and execution patterns together
- **DDIA + Legacy Code** → modernize data-heavy systems without rewrite gambling

---

# Suggested Next Improvement to the Repo

The repo already has useful content, but it currently mixes:

- conceptual skills
- protocol/state-machine skills
- duplicate concepts in two different formats

That is not inherently bad. In fact, it can be a strength.

The improvement is not “convert everything into a state machine.”
The improvement is:

- make the README explicit about the two formats
- explain when each format should be used
- mark pairs that cover the same concept in different ways
- add new skills only in the format that best matches their job

In other words: **use state machines where enforcement matters, and use flexible guides where judgment matters.**
