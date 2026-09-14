---
name: crimson-ui-qa
description: Runtime visual QA, accessibility routing, interaction/state verification, and screenshot regression.
---

# Runtime QA

Use after meaningful UI implementation or for explicit UI audit.


## Deep aspect subskills

This parent skill owns the broad domain. For MAX-depth work, load one or more aspect subskills below whenever they materially affect the decision.

MAX mode does **not** impose a one-aspect limit. It is acceptable to load several aspect subskills for a genuinely cross-cutting task, but each loaded aspect must have a clear reason.

| Aspect | Load | Purpose |
|---|---|---|
| Visual Hierarchy Audit | `aspects/visual-hierarchy-audit/SKILL.md` | Audit anchors, action priority, composition, typography, density, surfaces, and product specificity. |
| Interaction State Audit | `aspects/interaction-state-audit/SKILL.md` | Verify hover, focus, pressed, selected, disabled, loading, success, error, and recovery states. |
| Accessibility Audit | `aspects/accessibility-audit/SKILL.md` | Verify semantic, keyboard, focus, contrast, target-size, motion, screen-reader, and adaptive requirements. |
| Responsive and Cross-Platform Audit | `aspects/responsive-cross-platform/SKILL.md` | Verify layout and behavior across widths, input modes, platforms, themes, DPI, and window sizes. |
| Visual Regression | `aspects/visual-regression/SKILL.md` | Use screenshots/diffs responsibly to detect unintended change without treating every pixel difference as a defect. |
| Evidence and QA Reporting | `aspects/evidence-reporting/SKILL.md` | Produce actionable QA reports that distinguish proof, uncertainty, blockers, severity, and next action. |

### Aspect loading rule

Use the parent skill first, then load:
- one aspect for a focused deep problem;
- several aspects when root causes cross boundaries;
- the owner reference(s) when implementation or verification requires more complete detail.

Do not replace an aspect subskill with generic advice if the task clearly belongs to that aspect.

## Owner reference

`../../references/visual-qa.md`

Load it for TIER 1+ work or when any trigger below is true.

### Escalation triggers
- explicit audit;
- post-implementation verification;
- multiple interaction states must be checked;

For TIER 0 local fixes, do not open it unless needed.

## Read budget
Start with `../../references/visual-qa.md`.
Load at most one deeper QA reference unless the task explicitly needs both:
- accessibility/custom controls/forms/mobile/native a11y → `../../references/accessibility-qa.md`
- screenshot/cross-browser/cross-platform regression → `../../references/visual-regression.md`

## Evidence
Use:
`PASS / FAIL / NOT REVIEWED / BLOCKED / N/A / UNKNOWN`

Unrun is not PASS.
Source code alone cannot prove runtime interaction PASS.

## Check
- hierarchy/composition;
- action clarity;
- color harmony;
- responsive state;
- hover/focus/pressed/disabled/loading/error/success;
- SVG icon consistency;
- product specificity;
- support-surface competition;
- background integration;
- accessibility where applicable.

Fix BLOCKER/HIGH issues before decorative polish.
