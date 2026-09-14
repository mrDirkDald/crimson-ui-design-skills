# Crimson UI Design HARD — Exhaustive Index

## Start here

1. Read root `SKILL.md`.
2. Use `READING-MAP.md` to route by task.
3. Load the relevant domain subskill(s).
4. Load nested aspect subskills for the actual failure classes.
5. Load platform + stack + language guides when implementation matters.
6. Load QA chapters before claiming completion.

## High-end website route

```text
SKILL.md
→ references/web-craft-analysis.md
→ references/skills-sh-patterns.md
→ references/web.md
→ references/visual-direction.md
→ references/design-deliberation.md
→ references/anti-neuroslop-layout.md
→ subskills/web/
→ subskills/expressive-web/ when justified
→ handbook/webcraft/* as needed
→ actual framework stack guide
→ language guide
→ references/visual-qa.md
```

## Native/desktop route

```text
SKILL.md
→ references/application.md
→ references/desktop-app.md
→ subskills/application/
→ subskills/visual/ + color/design-system as needed
→ platform guide
→ stack guide
→ language guide
→ QA handbooks
```

## Design-system route

```text
SKILL.md
→ references/design-system.md
→ subskills/design-system/
→ color + visual aspect skills
→ implementation stack
→ component API / accessibility / visual-regression QA
```

## Repository engineering support

Use `handbook/engineering/` only when implementation quality, codebase navigation, profiling, QA, release readiness, orchestration, copy, or product improvement is materially in scope.

## Tooling

Use `subskills/tooling/SKILL.md`. HARD includes tooling guidance but intentionally includes **no self-updater**.

## ULTRA-HARD deep layer

- `ultra/ULTRA-INDEX.md` — full index of deep playbooks.
- `ultra/OPERATING-MANUAL.md` — no-token-economy operating model and deep-read routing.
- `ultra/engineering-deep/` — full high-depth engineering skill references carried into the frozen snapshot.



## ULTRA-HARD deep appendix

When this topic is materially relevant, do not evaluate only the default state. Expand the review across these dimensions:

### State coverage

```text
default
hover / pointer-over (if applicable)
focus-visible
pressed / active
selected / current
disabled / unavailable
loading / pending
empty / zero-data
partial / stale
success / completion
warning / risk
error / failure
offline / disconnected
permission denied / limited
read-only / locked
long content / localization
narrow / constrained
wide / high-density
reduced motion
high contrast / forced colors
```

### Input coverage

Check each relevant input independently: mouse/pointer, keyboard, touch, stylus, controller/remote, assistive technology, and automation/API-driven state. Never assume that a path reachable by hover or precise pointer is reachable by every other input.

### Responsive / adaptive coverage

Record what changes at narrow, standard, wide, ultrawide, high-text-scale, and long-content conditions. Reordering, collapsing, cropping, scroll ownership, navigation model, inspector behavior, command availability, and motion complexity may change independently.

### Evidence standard

Runtime observation outranks inference. A static code path can show intent but not prove visible focus, hit target behavior, animation timing, scroll containment, package/runtime assets, or assistive technology behavior. Report `BLOCKED` when the target environment cannot be exercised.

### Root-cause test

Before adding another local override, ask whether the issue belongs to a governing token, component contract, layout primitive, state model, navigation model, or content structure. Fix the highest stable layer that explains the failure without rewriting unrelated logic.

### Stop condition

Stop when acceptance criteria are met, must-preserve behavior remains correct, high-impact in-scope failures are resolved, and further change would add more churn or decorative novelty than user value.
