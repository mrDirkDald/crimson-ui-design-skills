---
name: crimson-ui-color-palette-generation
description: Deep aspect subskill for palette generation and selection within the Crimson UI Design MAX system.
---

# Palette Generation and Selection

## Purpose

Generate concrete palettes from the brief while avoiding AI-default color clichés.

This is a **deep aspect subskill**. Use it after loading the parent `color` skill when this aspect materially affects the result.

MAX edition rule: do not optimize this subskill for brevity. Prefer a complete design decision, explicit evidence, real implementation mapping, and runtime verification.

## When to use

Use this subskill when:
- the aspect is central to acceptance criteria;
- the parent skill identifies this area as a root cause;
- implementation crosses several components or states;
- a local fix would otherwise rely on guesswork;
- the user explicitly asks for a deep audit or redesign of this area.

Do not invoke it just because the file exists. A deep subskill should change the decision, implementation, or verification plan.

## Evidence to collect

Before changing anything, identify as many of these as are available:

```text
TARGET SURFACE:
CURRENT RUNTIME STATE:
GOVERNING COMPONENT / VIEW:
GOVERNING TOKENS / STYLES:
PLATFORM / VIEWPORT:
INPUT METHOD:
THEME:
REAL CONTENT / DATA:
KNOWN CONSTRAINTS:
MUST PRESERVE:
UNKNOWN:
BLOCKED:
```

Do not replace missing evidence with confident assumptions.

## Decision contract

Write a compact contract:

```text
PROBLEM:
WHY IT MATTERS:
ROOT CAUSE:
DESIRED OUTCOME:
MUST PRESERVE:
ALLOWED TO CHANGE:
SUCCESS EVIDENCE:
```

## Detailed rules

### Rule 1

Start from subject, audience, materials, environment, cultural context, and workflow before choosing hue.

Apply this rule to the **real governing surface**, not to isolated demo markup. When code and runtime disagree, treat the rendered/runtime behavior as the stronger signal and trace back to the layer that owns it.

When a local exception is necessary, document why it is semantically different instead of creating silent visual drift.
### Rule 2

Select a dominant family first, then supporting and accent roles.

Apply this rule to the **real governing surface**, not to isolated demo markup. When code and runtime disagree, treat the rendered/runtime behavior as the stronger signal and trace back to the layer that owns it.

When a local exception is necessary, document why it is semantically different instead of creating silent visual drift.
### Rule 3

Use the 2-color, 3-color, or 4+ catalog as a starting recipe, not as a mandatory brand palette.

Apply this rule to the **real governing surface**, not to isolated demo markup. When code and runtime disagree, treat the rendered/runtime behavior as the stronger signal and trace back to the layer that owns it.

When a local exception is necessary, document why it is semantically different instead of creating silent visual drift.
### Rule 4

Reject palettes that could be pasted into five unrelated products with no loss of meaning unless generic neutrality is intended.

Apply this rule to the **real governing surface**, not to isolated demo markup. When code and runtime disagree, treat the rendered/runtime behavior as the stronger signal and trace back to the layer that owns it.

When a local exception is necessary, document why it is semantically different instead of creating silent visual drift.
### Rule 5

Remove colors whose absence does not harm meaning or identity.

Apply this rule to the **real governing surface**, not to isolated demo markup. When code and runtime disagree, treat the rendered/runtime behavior as the stronger signal and trace back to the layer that owns it.

When a local exception is necessary, document why it is semantically different instead of creating silent visual drift.


## Implementation workflow

1. Reproduce or inspect the current state.
2. Trace the code/style/token path that governs the observed behavior.
3. Identify whether the problem is local, component-level, system-level, or platform-level.
4. Choose the smallest coherent governing layer that can solve it.
5. Define the intended behavior/visual rule before editing.
6. Implement without rewriting unrelated business logic.
7. Run relevant build/type/lint/tests.
8. Inspect the runtime in equivalent state.
9. Verify the specific checklist below.
10. Fix root causes exposed by verification.
11. Stop when acceptance is satisfied and further change would mainly add churn.

## Anti-patterns

Avoid:
- screenshot-only pixel patching with no governing rule;
- solving every issue by adding another card, border, shadow, color, or animation;
- replacing working behavior to make visual implementation easier;
- treating a code path as authoritative without proving it reaches the target UI;
- marking untested behavior as PASS;
- inventing data, metrics, states, or product semantics;
- broad refactors unrelated to this aspect;
- adding new dependencies when the existing stack already supports the required result;
- introducing platform-inappropriate conventions merely for visual consistency.

## Verification checklist

- [ ] brief grounding documented
- [ ] catalog choice justified
- [ ] dominance assigned
- [ ] AI-default clichés challenged
- [ ] unnecessary hues removed

Also verify:
- [ ] functionality still works;
- [ ] keyboard/focus behavior was not accidentally degraded where relevant;
- [ ] responsive/adaptive states affected by the change still work;
- [ ] dark/light theme behavior remains coherent if supported;
- [ ] no new emoji UI icons were introduced;
- [ ] Lucide or the existing coherent icon system remains consistent where icons are involved;
- [ ] accessibility is not worse than before;
- [ ] unresolved runtime limitations are reported as BLOCKED/NOT REVIEWED.

## Severity guidance

Use:
- `BLOCKER` — prevents core task, threatens data/safety, or makes essential UI unusable;
- `HIGH` — causes major workflow ambiguity, inaccessible primary action, or serious state failure;
- `MEDIUM` — recurring friction, hierarchy/consistency degradation, or meaningful polish defect;
- `LOW` — minor visual drift with limited user impact.

Do not inflate severity to make a design preference appear mandatory.

## Deliverable format

For a review:

```text
FINDING:
EVIDENCE:
SEVERITY:
ROOT CAUSE:
RECOMMENDED CHANGE:
MUST PRESERVE:
VERIFICATION:
```

For implementation:

```text
CHANGED:
WHY:
GOVERNING LAYER:
PRESERVED:
VERIFIED:
BLOCKED:
REMAINING RISK:
```

## Related deep reading

- `../../../../references/color-pairs.md`
- `../../../../references/color-trios.md`
- `../../../../references/color-palettes-4plus.md`

Read only what is relevant to this aspect, but in MAX mode it is acceptable to load multiple related references when they materially improve correctness.
