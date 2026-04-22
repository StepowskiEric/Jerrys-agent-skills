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
4. `intent-specification-protocol-skill.md` to clarify what correct behavior looks like before diving in
5. `judgment-and-routing/explore-vs-exploit-state-machine-skill.md`
6. `execution/ooda-loop-state-machine-skill.md` if the situation is changing while you investigate
7. `output-quality/tool-interactive-critic-skill.md` to verify the conclusion against code, logs, or tests

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
2. `intent-specification-protocol-skill.md` to lock the target behavior before changing code
3. `execution/working-effectively-with-legacy-code-state-machine-skill.md`
4. `execution/refactoring-state-machine-skill.md`
5. `execution/pragmatic-programmer-state-machine-skill.md`
6. `execution/checklist-manifesto-skill.md` if the change is risky or procedural
7. `output-quality/tool-interactive-critic-skill.md` before claiming the work is done

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

### Specification-driven coding (any non-trivial code change)

1. `intent-specification-protocol-skill.md` — state what correct behavior looks like before writing code
2. `output-quality/bounded-self-revision-skill.md` — verify the spec is achievable and self-consistent
3. `step-level-verification-protocol-skill.md` — check each unit of work against the spec before moving on

Why this stack works: spec-first eliminates rework, bounded self-revision catches spec gaps early, step-level verification keeps each change aligned with intent.

## If you are unsure where to begin

A practical default sequence is:

1. `judgment-and-routing/problem-mode-router-cynefin-skill.md`
2. `judgment-and-routing/thoroughness-check-etto-state-machine-skill.md`
3. `orchestration/socratic-clarification-skill.md` if the task is ambiguous
4. one task-specific protocol or framework from the relevant topic folder
5. `output-quality/tool-interactive-critic-skill.md` if the output depends on facts or code that can be externally checked
6. `execution/toyota-kata-state-machine-skill.md` if the goal is iterative improvement rather than one-shot change
