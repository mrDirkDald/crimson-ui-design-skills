---
name: crimson-ui-qa
description: Runtime visual QA, accessibility routing, interaction/state verification, and screenshot regression.
---

# Runtime QA

Use after meaningful UI implementation or for explicit UI audit.


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
