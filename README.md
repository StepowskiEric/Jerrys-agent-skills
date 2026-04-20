# Jerry's Agent Skills

A catalog of agent skills for making AI systems more reliable, disciplined, and useful in real work.

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

## Operational Protocols / State-Machine Skills

### 1) `agentic-design-patterns-orchestrator-state-machine-skill.md`
**What it is:** A workflow-control skill for tasks that need classification, planning, routing, evidence gathering, execution, reflection, verification, and stopping.

**Use it when:** The agent should behave like an orchestrated system, not a one-shot responder.

**Best for:** Multi-step tasks, sub-agent coordination, tool-using workflows, bounded execution.

---

### 2) `checklist-manifesto-state-machine-skill.md`
**What it is:** A protocol for turning omission-sensitive work into short, usable checklists with explicit pause points, verification steps, and abort triggers.

**Use it when:** The main risk is not inventing the answer but forgetting, skipping, or misordering critical steps.

**Best for:** Deploys, migrations, release prep, incident runbooks, handoffs, production changes, and other repeatable high-consequence workflows.

---

### 3) `cognitive-load-operator-state-machine-skill.md`
**What it is:** A protocol for making outputs easier to understand, retain, and act on.

**Use it when:** An answer is technically correct but mentally expensive.

**Best for:** Documentation, workflows, instructions, prompts, onboarding, dense explanations.

---

### 4) `explore-vs-exploit-state-machine-skill.md`
**What it is:** A control system for deciding whether to keep gathering information or commit to action.

**Use it when:** The agent risks either acting too early or searching forever.

**Best for:** Research, debugging, planning, decision support, ambiguous tasks.

---

### 5) `how-to-solve-it-state-machine-skill.md`
**What it is:** A disciplined problem-solving protocol that forces problem framing, evidence gathering, planning, execution, and reflection.

**Use it when:** The task is hard, uncertain, or likely to tempt premature coding.

**Best for:** Debugging, algorithmic reasoning, difficult implementation tasks, root-cause work.

---

### 6) `inversion-mental-model-state-machine-skill.md`
**What it is:** A protocol for reasoning from failure backward: define the opposite of success, enumerate failure paths, rank them, and turn them into guardrails.

**Use it when:** Risk, blind spots, defensive design, or failure modes matter.

**Best for:** Safety checks, architecture review, incident prevention, rollout planning.

---

### 7) `philosophy-of-software-design-state-machine-skill.md`
**What it is:** A protocol for managing complexity, building deeper modules, and avoiding shallow abstraction sprawl.

**Use it when:** The agent is changing shared interfaces or making design decisions that can spread complexity.

**Best for:** API design, module boundaries, simplification, architecture cleanup.

---

### 8) `pragmatic-programmer-state-machine-skill.md`
**What it is:** A practical engineering protocol focused on bounded changes, reversible decisions, automation, and root-cause fixes.

**Use it when:** The agent needs to work like a senior pragmatist instead of an idealist or cleanup maximalist.

**Best for:** Day-to-day engineering work, tooling, repetitive toil reduction, incremental improvements.

---

### 9) `refactoring-state-machine-skill.md`
**What it is:** A bounded refactoring protocol that defines a target, accounts for shared surfaces, limits the transformation budget, and stops cleanly.

**Use it when:** Structure needs improvement but the task could spiral into endless cleanup.

**Best for:** Safe refactors, complexity reduction, targeted cleanup, anti-slop work.

---

### 10) `thinking-in-systems-state-machine-skill.md`
**What it is:** A protocol for mapping system boundaries, stocks, flows, loops, delays, leverage points, and blast radius before changing anything.

**Use it when:** The problem involves feedback loops, delayed effects, or second-order consequences.

**Best for:** Architecture, workflows, scaling problems, process failures, policy changes.

---

### 11) `thoroughness-check-etto-state-machine-skill.md`
**What it is:** A universal preflight gate based on the efficiency–thoroughness trade-off.

**Use it when:** The agent should decide how much evidence, validation, and caution are required before acting.

**Best for:** Almost any non-trivial task, especially when risk or irreversibility is involved.

---

### 12) `toyota-kata-state-machine-skill.md`
**What it is:** A continuous-improvement protocol that forces the agent to define the current condition, set the next target condition, isolate one obstacle, and run one bounded experiment at a time.

**Use it when:** The path forward is uncertain and progress should be discovered iteratively rather than through one large redesign.

**Best for:** Optimization, process improvement, performance tuning, workflow refinement, developer-experience improvements, and safe iterative experimentation.

---

### 13) `working-effectively-with-legacy-code-state-machine-skill.md`
**What it is:** A protocol for making brittle code safe to change before trying to improve it.

**Use it when:** The system has weak tests, unclear behavior, tight coupling, or rewrite temptation.

**Best for:** Characterization testing, seam creation, change safety, legacy modernization.

---

## Conceptual / Framework Skills

### 14) `accelerate-ai-skill.md`
**What it is:** A delivery and reliability lens inspired by Accelerate-style thinking.

**Use it when:** The agent must improve engineering throughput, feedback loops, reliability, or team productivity using evidence rather than folklore.

**Best for:** Delivery metrics, operational improvement, recovery time reduction, batch-size reduction.

---

### 15) `agentic-design-patterns-orchestrator-skill.md`
**What it is:** A conceptual version of the orchestration skill focused on planning, routing, deliberate tool use, reflection, memory, sub-agents, and human-in-the-loop behavior.

**Use it when:** You want the agent to reason with agentic patterns without necessarily enforcing a strict protocol.

**Best for:** Strategy design, agent architecture thinking, early-stage workflow design.

---

### 16) `designing-data-intensive-applications-ai-skill.md`
**What it is:** A data-systems reasoning lens inspired by DDIA.

**Use it when:** The agent must reason about storage, distributed systems, consistency, replication, partitioning, messaging, or reliability tradeoffs.

**Best for:** Backends, data architecture, infra design, state management, event-driven systems.

---

### 17) `explore-vs-exploit-skill.md`
**What it is:** A conceptual version of the exploration-vs-commitment tradeoff.

**Use it when:** You want the agent to think clearly about search breadth versus action, without a rigid execution protocol.

**Best for:** Planning, ideation, research strategy, lightweight debugging decisions.

---

### 18) `inversion-mental-model-skill.md`
**What it is:** A conceptual version of inversion as a reasoning tool for risks, blind spots, and failure modes.

**Use it when:** The agent needs a better strategic lens rather than a formal failure-mapping workflow.

**Best for:** Strategy, critique, planning, pre-mortems, anti-goal analysis.

---

### 19) `kahneman-thinking-fast-slow-software-agent-skill.md`
**What it is:** A judgment skill based on fast versus slow thinking for software engineering work.

**Use it when:** The agent needs to decide when cheap pattern recognition is fine and when slow, careful reasoning is mandatory.

**Best for:** Coding, debugging, estimation, review, ambiguous architecture decisions.

---

### 20) `problem-mode-router-cynefin-skill.md`
**What it is:** A routing skill based on Cynefin-style problem classification that helps the agent decide whether the situation is obvious, complicated, complex, chaotic, or still disordered.

**Use it when:** The first question is not “what do I do?” but “what kind of problem is this, and what response style fits it?”

**Best for:** Task routing, incident routing, skill-stack selection, project kickoff diagnosis, and preventing the wrong reasoning mode from dominating the task.

---

### 21) `recognition-primed-triage-skill.md`
**What it is:** A fast-judgment skill for urgent situations that tells the agent to recognize the pattern, choose the first plausible strong move, mentally simulate it, and then reassess.

**Use it when:** Delay is costly, information is incomplete, and the agent needs a high-quality first move rather than exhaustive comparison.

**Best for:** Incident triage, outage response, urgent debugging, ops escalation, and fast prioritization under pressure.

---

### 22) `team-topologies-ai-skill.md`
**What it is:** A coordination and ownership lens for multi-agent or multi-team systems.

**Use it when:** The problem is less about one task and more about how work should be split, owned, and coordinated.

**Best for:** Multi-agent systems, platform teams, ownership design, reducing coordination chaos.

---

### 23) `the-goal-theory-of-constraints-ai-skill.md`
**What it is:** A throughput and bottleneck lens based on Theory of Constraints.

**Use it when:** The agent must improve performance or delivery by finding the real limiting factor rather than optimizing everything.

**Best for:** Performance tuning, workflow optimization, queue reduction, system throughput improvement.

---

### 24) `thoroughness-check-etto-skill.md`
**What it is:** A conceptual version of the ETTO principle for deciding the right rigor level before work begins.

**Use it when:** You want the judgment of ETTO without a formal gate.

**Best for:** Prompting style, advisory workflows, lightweight preflight reasoning.

---

### 25) `unsafe-control-actions-hazard-analysis-skill.md`
**What it is:** A hazard-analysis skill for checking whether a consequential action becomes unsafe if it is omitted, applied incorrectly, mistimed, misordered, or left in place too long.

**Use it when:** The agent is about to recommend or perform a high-consequence action where timing, sequencing, constraints, and safeguards matter.

**Best for:** Risky automations, infra changes, migrations, data mutations, security-sensitive operations, rollout decisions, and any tool action that changes external state.

---

# Recommended Ways to Use This Repo

## If you want execution discipline
Start with the protocol skills, especially:

- `thoroughness-check-etto-state-machine-skill.md`
- `how-to-solve-it-state-machine-skill.md`
- `refactoring-state-machine-skill.md`
- `working-effectively-with-legacy-code-state-machine-skill.md`
- `checklist-manifesto-state-machine-skill.md`
- `toyota-kata-state-machine-skill.md`

## If you want better judgment or routing
Start with the framework skills, especially:

- `problem-mode-router-cynefin-skill.md`
- `recognition-primed-triage-skill.md`
- `unsafe-control-actions-hazard-analysis-skill.md`
- `thinking-in-systems-state-machine-skill.md`
- `the-goal-theory-of-constraints-ai-skill.md`
- `kahneman-thinking-fast-slow-software-agent-skill.md`

## If you are building higher-quality agent workflows
Strong combinations include:

- **ETTO + Problem-Mode Router** → decide rigor level and response mode first
- **Recognition-Primed Triage + Unsafe Control Actions** → move fast, but with guardrails
- **How to Solve It + Pragmatic Programmer** → disciplined diagnosis plus grounded execution
- **Working Effectively with Legacy Code + Refactoring** → make change safe, then improve structure
- **Thinking in Systems + Theory of Constraints** → understand the system, then find the true bottleneck
- **Toyota Kata + Checklist Manifesto** → iterative improvement plus omission-resistant execution

## If you are unsure where to begin
A practical default sequence is:

1. `problem-mode-router-cynefin-skill.md`
2. `thoroughness-check-etto-state-machine-skill.md`
3. one task-specific protocol or framework
4. `checklist-manifesto-state-machine-skill.md` if the workflow is omission-sensitive
5. `toyota-kata-state-machine-skill.md` if the goal is iterative improvement rather than one-shot change

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
