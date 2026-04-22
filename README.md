# Jerry's Agent Skills

A catalog of agent skills for making AI systems more reliable, disciplined, and useful in real work.

## Quick Install

```bash
# Interactive picker — choose agent and skills
npx jerry-skills install

# Install all skills to a specific agent
npx jerry-skills install --agent copilot
npx jerry-skills install --agent codex
npx jerry-skills install --agent hermes
npx jerry-skills install --agent claude

# List available skills without installing
npx jerry-skills list
```

See [docs/installation.md](docs/installation.md) for full details including all agents, custom destinations, and VS Code Copilot setup.

## Documentation

| Document | What's in it |
|----------|-------------|
| [Find by Use Case](docs/find-by-use-case.md) | "I need a skill for..." — tables matching situations to the best skill |
| [Skill Catalog](docs/skill-catalog.md) | Detailed per-skill entries: what it is, when to use it, best for |
| [Recommended Combinations](docs/recommended-combinations.md) | Skill stacks for common scenarios (debugging, architecture, refactoring...) |
| [Quick Reference](docs/quick-reference.md) | Compact tables of all protocol and framework skills |
| [Installation Guide](docs/installation.md) | Detailed install instructions for each agent |

## Two Kinds of Skills

This repository contains **two kinds of skills**:

1. **Operational protocols** — skills that act like procedures or control systems.
   These benefit from a state-machine structure because the value is in gating behavior, forcing evidence collection, and preventing premature action.

2. **Conceptual frameworks** — skills that act like lenses, heuristics, routing models, or architectural principles.
   These do **not** always need to be state machines. In many cases, forcing them into a rigid protocol makes them worse: more ceremonial, less adaptable, and less readable.

### When to use which

Use a **state-machine/protocol** when the agent should:
- follow a repeatable sequence
- respect tool-gating by phase
- create mandatory diagnostic artifacts
- stop when a condition is met
- avoid looping, over-searching, or reckless execution

Use a **framework** when the agent should:
- adopt a way of seeing a problem
- reason about tradeoffs
- borrow principles from a book or framework
- improve judgment rather than enforce a workflow
- adapt ideas fluidly to many contexts

The strongest setups use **both**: protocols for execution discipline, frameworks for better judgment.

## Skill Categories

| Category | What it covers |
|----------|---------------|
| 🔧 Execution | Problem-solving protocols (debugging, refactoring, improvement) |
| 🧭 Judgment & Routing | Decision-making frameworks (routing, triage, risk analysis) |
| 🎛️ Orchestration | Workflow control (multi-agent, coordination, memory) |
| ✨ Output Quality | Self-improvement (revision, verification, clarity) |
| 🏗️ Systems & Architecture | Design principles (data, teams, reliability) |
| 🛠️ Development | Skill building and development workflows |
| 🐛 Debugging | Root-cause analysis and log correlation |
| 🧠 Reasoning | Faithfulness and reasoning verification |

## Philosophy

This repo should not force one format onto every idea.

The goal is not to make everything look uniform.
The goal is to make each skill **more executable and more useful**.

Some skills become dramatically better when turned into state machines.
Others become worse.

A good agent-skill repository should preserve both:

- **control** where behavior must be constrained
- **judgment** where thinking quality matters more than workflow ceremony
