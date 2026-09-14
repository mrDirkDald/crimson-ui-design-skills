---
name: crimson-ui-tooling
summary: Optional developer/QA tools for evidence gathering, validation, dependency safety, runtime checks, and diagnostics.
---

# Tooling

Use this subskill only when a tool can answer a concrete engineering or QA question. Do not install tools merely because they are listed here.

## Owner reference

Primary reference: `../../references/tooling-sources.md`.

### Escalation triggers

Escalate only when the task materially needs build/test/runtime/security evidence, dependency vetting, performance profiling, accessibility automation, or skill validation.

## Tool selection contract

Before using a nontrivial tool, state internally:

```text
QUESTION:
TOOL:
WHY THIS TOOL:
WHAT IT MAY EXECUTE OR MODIFY:
EXPECTED EVIDENCE:
STOP CONDITION:
```

Prefer the project's existing toolchain over adding new dependencies.

## fchek

`fchek` is an optional broad developer toolbox. Useful categories can include project context, conventions, tests, secrets, dependency checks, coverage, profiling, ports, process/runtime diagnostics, and other developer utilities.

Good uses when available and appropriate:
- inspect project context/conventions before creating duplicate abstractions;
- diagnose environment/tooling problems;
- run project tests when executing project code is already in scope;
- check for accidentally committed secrets;
- inspect dependency risk;
- collect coverage/performance evidence;
- diagnose port/process conflicts.

Do not treat every `fchek` command as safe. Some commands may execute project code, mutate git/system state, query databases, touch processes, or expose logs. Use only the minimum command needed for the current question.

Do not auto-install `fchek`. Verify the current upstream package/repository and pin a version first.

## skill-check

Use `skill-check` or equivalent skill-specific validation when reviewing Agent Skill structure, consistency, or security posture. It complements the bundled validator; it does not replace it.

## npm-safe

For Node/Electron/web work, use `npm-safe` or an equivalent package-safety scanner before introducing unfamiliar npm dependencies when supply-chain risk is material.

A favorable scan is evidence, not a guarantee of safety. Keep lockfiles and version pinning.

## Playwright

Use Playwright when browser/Electron renderer behavior needs runtime proof:
- viewport/window states;
- keyboard interaction;
- forms;
- hover/focus/pressed states;
- navigation;
- screenshots;
- reduced motion / theme variants.

Screenshot automation does not prove semantic accessibility by itself.

## Accessibility automation

Use axe-core or equivalent automation for machine-detectable issues such as accessible names, ARIA misuse, some contrast/structure failures, and form problems.

Still verify keyboard flow, focus, semantics, error recovery, zoom/text scaling, and alternate input behavior where relevant.

## Performance tooling

Use Lighthouse/browser performance tools for browser-rendered products when performance is in scope. Use project-native profilers for desktop/native workloads.

Do not optimize a desktop utility around irrelevant marketing-site metrics.

## Storybook / component harnesses

Use Storybook or an equivalent isolated component harness when the project already uses it or when shared component state coverage has high value. Do not add it for one trivial component.

## Native project tools

Prefer the project's own ecosystem:
- `dotnet build/test`;
- `cargo test/clippy`;
- CMake/project-native tests;
- `go test`;
- `pytest`;
- Gradle/Xcode tools;
- framework-native lint/type checks.

## Trust tiers

```text
A — inspect/read-only evidence
B — executes project/tool code
C — mutates project/system/external state
```

Never silently escalate A → B → C.

## Evidence report

After tool use, report internally or to the user when useful:

```text
TOOL:
MODE:
OBSERVED:
PASS / FAIL / BLOCKED:
WHAT THIS PROVES:
WHAT THIS DOES NOT PROVE:
```
