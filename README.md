# Agent Skills Repository

A curated set of **state-machine-style agent skills** for building more reliable AI workflows.

These skills are not generic advice notes. They are designed as **operational protocols** with:
- explicit phases
- mandatory diagnostic artifacts
- tool-gating by phase
- blast-radius / unknowns handling
- stop conditions
- escalation triggers

The goal is to help an AI agent behave less like a one-shot autocomplete system and more like a bounded, auditable operator.

---

## What This Repository Is For

Use this repository when you want an AI agent to:

- choose the right level of rigor before acting
- avoid premature action
- avoid endless searching or endless refactoring
- make decisions with clearer stopping rules
- handle complex or risky tasks with structured control
- produce outputs that are easier for humans to understand and review
- operate with safer multi-step workflows

This repository is especially useful for:
- agent frameworks
- autonomous coding loops
- research agents
- debugging workflows
- planning/execution systems
- tool-using assistants
- high-risk engineering tasks
- AI systems that need better discipline than “just prompt harder”

---

## Repository Design Principles

All current skills in this repo are the **refactored state-machine versions**.

That means they generally include:

1. **A mandatory pre-action artifact**  
   Example: `etto-preflight.md`, `problem-frame.md`, `failure-map.md`

2. **A recon or analysis phase**  
   The agent must inspect before it acts.

3. **Tool permissions by phase**  
   Read/search/test first; write/execute later.

4. **Unknowns and blast-radius accounting**  
   If the agent cannot see the full impact, it must say so.

5. **A stop condition**  
   The agent is expected to stop after the target objective is completed.

---

# Skill Catalog

## 1) Thoroughness Check (ETTO)
**File:** `thoroughness-check-etto-state-machine-skill.md`

### What it does
Acts as a universal **preflight risk gate**.  
It forces the agent to decide how cautious it should be before it begins.

### Best use-case
Use this before almost any non-trivial task:
- planning
- code changes
- advice with real consequences
- research with uncertain facts
- architecture work
- destructive or risky actions

### Invoke when
You need the agent to answer:
- How risky is this?
- How reversible is this?
- How much evidence do I need before acting?
- Should I move fast, balanced, or very carefully?

### Short summary
**Pick the right rigor before doing anything else.**

---

## 2) Cognitive Load Operator
**File:** `cognitive-load-operator-state-machine-skill.md`

### What it does
Makes outputs easier to understand, scan, remember, and act on.  
It reduces working-memory burden.

### Best use-case
Use this for:
- explanations
- plans
- documentation
- prompts
- instructions
- workflows
- onboarding docs
- dense recommendations

### Invoke when
The output is technically correct but hard to follow, overloaded, branchy, or mentally expensive.

### Short summary
**Make understanding cheap.**

---

## 3) Explore vs Exploit
**File:** `explore-vs-exploit-state-machine-skill.md`

### What it does
Controls whether the agent should keep searching for more information or commit to action.

### Best use-case
Use this for:
- debugging
- research
- model/tool/vendor selection
- ambiguous planning
- deciding whether enough has been learned already

### Invoke when
The agent is at risk of:
- acting too early on weak evidence
- searching forever and never converging

### Short summary
**Search with purpose. Stop deliberately. Act when more searching no longer pays.**

---

## 4) Inversion
**File:** `inversion-mental-model-state-machine-skill.md`

### What it does
Forces the agent to think backward from failure before recommending a path to success.

### Best use-case
Use this for:
- risk reviews
- launch planning
- safety analysis
- reliability planning
- defensive design
- strategy stress-testing

### Invoke when
You want answers to questions like:
- How could this fail?
- What would sabotage this?
- What guardrails would prevent that?

### Short summary
**Map the losing paths before you commit to the winning one.**

---

## 5) Agentic Patterns Orchestrator
**File:** `agentic-design-patterns-orchestrator-state-machine-skill.md`

### What it does
Turns a one-shot agent into a structured workflow system.  
It chooses the minimum useful set of patterns:
- planning
- routing
- tool use
- reflection
- memory
- multi-agent collaboration
- guardrails
- exception handling

### Best use-case
Use this for:
- multi-step tasks
- tool-heavy workflows
- agent loops
- planning-execute-verify systems
- research + action pipelines
- larger autonomous tasks

### Invoke when
A task is too complex to trust to a single-shot answer.

### Short summary
**Workflow control system for real agent operations.**

---

## 6) Thinking in Systems
**File:** `thinking-in-systems-state-machine-skill.md`

### What it does
Forces the agent to map loops, delays, stocks, flows, leverage points, and downstream effects before intervening.

### Best use-case
Use this for:
- incidents
- retry storms
- queue problems
- scaling issues
- cascading failures
- cache or schema side effects
- cross-service behavior problems

### Invoke when
A problem is not isolated to one file or one component, and the real issue may be in system interactions.

### Short summary
**Model the behavior of the system before touching the mechanism.**

---

## 7) Working Effectively with Legacy Code
**File:** `working-effectively-with-legacy-code-state-machine-skill.md`

### What it does
Makes the agent create safety first in brittle or poorly tested systems.

### Best use-case
Use this for:
- risky old code
- weak-test areas
- unclear behavior
- safe refactors in hostile code
- seam creation
- characterization tests

### Invoke when
You need to change something that feels dangerous and poorly understood.

### Short summary
**Make change safe first. Then improve it. Then stop.**

---

## 8) How to Solve It
**File:** `how-to-solve-it-state-machine-skill.md`

### What it does
Forces disciplined problem solving:
- frame the problem
- gather evidence
- rank hypotheses
- plan
- act
- reflect

### Best use-case
Use this for:
- debugging
- unfamiliar repos
- ambiguous failures
- problem diagnosis
- root-cause analysis
- hard engineering questions

### Invoke when
The agent is tempted to start editing before it understands the problem.

### Short summary
**Understand first. Search second. Plan third. Act fourth. Reflect fifth.**

---

## 9) The Pragmatic Programmer
**File:** `pragmatic-programmer-state-machine-skill.md`

### What it does
Helps the agent make a practical, bounded, reversible move in a real system.

### Best use-case
Use this for:
- day-to-day engineering work
- bounded improvements
- avoiding overengineering
- root-cause fixes
- automation opportunities
- blast-radius-aware changes

### Invoke when
You want the agent to behave like a practical senior engineer instead of a theory maximalist.

### Short summary
**Make the smallest correct move, stay honest about risk, and automate repeated toil.**

---

## 10) A Philosophy of Software Design
**File:** `philosophy-of-software-design-state-machine-skill.md`

### What it does
Pushes the agent toward deeper modules and lower change amplification instead of shallow abstraction sprawl.

### Best use-case
Use this for:
- complexity management
- interface design
- reducing shallow wrappers
- boundary design
- simplifying caller burden

### Invoke when
The problem is structural complexity, not just correctness.

### Short summary
**Hide more complexity than you create.**

---

## 11) Refactoring
**File:** `refactoring-state-machine-skill.md`

### What it does
Constrains refactoring into a bounded, testable, non-endless structural cleanup session.

### Best use-case
Use this for:
- one targeted refactor
- reducing one smell family
- small structural improvement passes
- avoiding cleanup drift

### Invoke when
You want to improve structure without turning the session into a rewrite spiral.

### Short summary
**Reduce one meaningful structural problem, verify it, and stop.**

---

# Recommended Default Stacks

These skills are strongest when composed, not used in isolation.

## Universal default
**ETTO -> Agentic Patterns Orchestrator -> one domain skill**

Use this when:
- the task is non-trivial
- you want risk control first
- you want workflow structure second
- you want a specialized mode third

---

## Debugging stack
**ETTO -> How to Solve It -> Explore vs Exploit**

Use this when:
- the issue is unclear
- you need evidence before edits
- you want to avoid both guessing and endless searching

---

## High-risk systems stack
**ETTO -> Thinking in Systems -> Inversion**

Use this when:
- a mistake could create downstream failures
- loops/delays matter
- you want both system mapping and failure stress-testing

---

## Legacy code stack
**ETTO -> Working Effectively with Legacy Code -> Refactoring**

Use this when:
- the code is brittle
- you need seams/tests first
- you want bounded structural improvement after safety exists

---

## Complexity/design stack
**ETTO -> A Philosophy of Software Design -> Pragmatic Programmer**

Use this when:
- the main issue is complexity, shallow abstractions, or bad boundaries
- you want a real design improvement without slipping into theory theater

---

## Documentation / explanation stack
**Cognitive Load Operator -> Inversion**  
or  
**Cognitive Load Operator -> Pragmatic Programmer**

Use this when:
- you want clear operational docs
- you want plans that are both understandable and robust

---

# How to Choose a Skill Quickly

## If the first question is...
### “How careful should I be?”
Use **ETTO**

### “Is the agent thinking clearly enough?”
Use **How to Solve It**

### “Should the agent keep researching or act now?”
Use **Explore vs Exploit**

### “What could go wrong?”
Use **Inversion**

### “This task is multi-step and needs structure.”
Use **Agentic Patterns Orchestrator**

### “This is a systems problem, not a local problem.”
Use **Thinking in Systems**

### “This code is scary to touch.”
Use **Working Effectively with Legacy Code**

### “I need a practical bounded move.”
Use **The Pragmatic Programmer**

### “The design is shallow or overly complex.”
Use **A Philosophy of Software Design**

### “I need one controlled refactor, not endless cleanup.”
Use **Refactoring**

### “The output is too mentally heavy.”
Use **Cognitive Load Operator**

---

# What Makes These Different from Normal Prompt Files

Most prompt files tell the agent to:
- be thoughtful
- consider risks
- avoid mistakes
- reason carefully

That is not enough.

These skills instead try to enforce:
- **what artifact must exist first**
- **what the current phase allows**
- **what evidence is required before action**
- **what must be declared unknown**
- **what ends the run**

That makes them more useful inside real agent loops.

---

# Suggested Repository Layout

```text
skills/
  thoroughness-check-etto-state-machine-skill.md
  cognitive-load-operator-state-machine-skill.md
  explore-vs-exploit-state-machine-skill.md
  inversion-mental-model-state-machine-skill.md
  agentic-design-patterns-orchestrator-state-machine-skill.md
  thinking-in-systems-state-machine-skill.md
  working-effectively-with-legacy-code-state-machine-skill.md
  how-to-solve-it-state-machine-skill.md
  pragmatic-programmer-state-machine-skill.md
  philosophy-of-software-design-state-machine-skill.md
  refactoring-state-machine-skill.md
README.md
```

---

# Recommended Cleanup

If the repo still contains the older non-state-machine versions, remove them so users only see the current protocol versions.

Recommended to delete:
- earlier `*-ai-skill.md` files
- earlier non-state-machine `*-skill.md` files for the same concepts

Keep only the `*-state-machine-skill.md` files for the current set.

---

# Good Usage Advice

- Use **ETTO first** for most serious tasks.
- Use **one main domain skill** at a time unless there is a clear reason to compose more.
- Prefer **bounded runs** over “improve everything.”
- If blast radius is unknown, narrow the scope or declare the risk.
- If the agent is looping, add or strengthen the stop condition.
- If the agent keeps guessing, strengthen the evidence gate.
- If the agent keeps over-explaining, use Cognitive Load Operator.

---

# Final Note

This repository is best thought of as a **control layer for agents**.

Not:
- random prompt templates
- generic philosophy notes
- motivational best practices

But:
- task modes
- operating protocols
- bounded workflows
- evidence gates
- stopping rules

If you want an agent that is faster, safer, and less likely to wander, these skills are meant to provide the control surface.
