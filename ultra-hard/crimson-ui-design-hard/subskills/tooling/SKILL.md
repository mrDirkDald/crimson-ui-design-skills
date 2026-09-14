---
name: crimson-ui-tooling
description: Optional tooling workflow for evidence gathering, UI/runtime verification, skill validation, package safety, performance, accessibility, and developer diagnostics. Load only when external/local developer tools can materially improve correctness.
---

# Crimson UI Tooling

## Purpose

Use tools to obtain evidence, not to create the appearance of rigor.

Do not run every available tool on every task.

Choose the smallest set that can answer a concrete question such as:
- Does the project build?
- Did the visual change actually render?
- Are all important states reachable?
- Is the dependency safe enough to install?
- Did performance regress?
- Is the skill itself structurally valid?
- Is a runtime failure caused by code, environment, process state, or UI?

## Tool-selection contract

Before invoking a nontrivial tool:

```text
QUESTION:
TOOL:
WHY THIS TOOL:
WHAT IT MAY EXECUTE / MODIFY:
EXPECTED EVIDENCE:
STOP CONDITION:
```

Do not add tools merely because they are fashionable.

---

# 1. fchek — broad developer / AI toolbox

`fchek` is a broad CLI toolbox with commands for project context, conventions, tests, secrets, dependency checks, linting, coverage, profiling, fuzzing, ports, Docker, SQLite, Windows integration and more.

Treat it as **optional**, not a mandatory dependency.

Important: broad developer toolboxes can execute project code, shell commands, database queries, process actions, registry operations, or other sensitive operations depending on the subcommand.

Never equate “fchek is installed” with permission to use every command.

## Good uses

Useful candidates include:
- `fchek context <dir>` — understand symbols before creating duplicates;
- `fchek convention <dir>` — inspect project conventions;
- `fchek doctor` — diagnose local tooling/environment;
- `fchek test <dir>` — run the project's tests when executing project code is appropriate;
- `fchek secrets <path>` — look for accidentally committed credentials;
- `fchek vuln <dir>` — dependency vulnerability/typosquatting check;
- `fchek coverage <dir>` — coverage evidence;
- `fchek bench ...` — compare performance before/after;
- `fchek deps <dir>` — dead/circular dependency analysis;
- `fchek port <port>` — diagnose port conflicts;
- `fchek screenshot` — useful when the environment supports Windows runtime visual verification.

## Caution / explicit-purpose commands

Commands such as these require a concrete need and environment/user permission:

```text
run
git stage / commit / other mutating git actions
db query
docker logs / actions
registry modification
process management
launch
watch
race
fuzz
profile
```

Reasons:
- they may execute project code;
- mutate state;
- expose logs/data;
- consume significant resources;
- affect processes/system configuration.

## Supply-chain rule for fchek

Do not automatically install `fchek` just because this skill mentions it.

Before first installation:
1. verify the current package/repository and version;
2. pin the version;
3. run a package safety check where available;
4. inspect lifecycle scripts and dependencies;
5. only then install if it materially helps.

Because tooling changes over time, verify current documentation rather than trusting commands/versions frozen in this skill.

---

# 2. skill-check — agent-skill validation

Use `skill-check` when validating the structure/quality/security posture of an Agent Skill.

Useful workflows:
- check a local skill;
- compare two skill trees;
- produce reports;
- use GitHub annotations in CI;
- run security scanning when the required scanner is available.

Prefer pinned versions in CI.

For safety-sensitive/offline use, prefer options that prevent implicit dependency installation.

Example intent:

```text
validate this skill's structure
→ skill-check
```

Do not replace the skill's own validators with one external linter. Use both when their evidence is complementary.

---

# 3. npm-safe — scan npm packages before installation

For Node/Electron/web tooling, use a supply-chain check before introducing unfamiliar npm dependencies.

`npm-safe` is designed for package metadata and optional deep tarball analysis.

Good use:
- inspect a package before adding it;
- inspect a lockfile;
- deep-scan package contents without executing the package;
- investigate install scripts, obfuscation, suspicious process/network combinations, typosquatting, and related signals.

A favorable scanner result is evidence, not a guarantee of safety.

Do not bypass project lockfiles or pinning discipline just because a scanner returns a good score.

---

# 4. Playwright

Use Playwright when browser/Electron renderer behavior needs runtime proof.

Good for:
- viewport matrix;
- keyboard interaction;
- navigation;
- hover/focus/pressed states;
- forms;
- screenshot capture;
- regression states;
- reduced-motion emulation;
- color-scheme checks.

Do not use screenshot-only automation as proof of semantic accessibility.

---

# 5. axe-core / accessibility tooling

Use axe-based automation for machine-detectable accessibility failures.

It can help detect:
- missing accessible names;
- invalid ARIA;
- some contrast/structure failures;
- landmark/form issues.

Automated accessibility tests are incomplete.

Still verify:
- keyboard flow;
- focus order/restoration;
- screen-reader semantics where required;
- error recovery;
- zoom/text scaling;
- touch/controller alternatives where relevant.

---

# 6. Lighthouse / browser performance tooling

Use Lighthouse or equivalent browser performance tooling when the product is browser-rendered and performance is in scope.

Treat lab metrics as one evidence source.

Do not redesign a repeated-use desktop utility around marketing-site Lighthouse scores that are irrelevant to the actual runtime.

---

# 7. Storybook / isolated component states

Use Storybook or equivalent component harnesses when:
- the project already uses it;
- shared component states need exhaustive review;
- design-system work spans many variants.

Do not introduce Storybook to a tiny project solely to test one button.

Isolated component PASS does not prove integrated product PASS.

---

# 8. Native project test/build tools

Prefer the project's own ecosystem:
- `dotnet build/test`;
- `cargo test/clippy`;
- `cmake` / project test runner;
- `go test`;
- `pytest`;
- `gradle test`;
- Xcode test tooling;
- framework-native linters/type checkers.

Do not replace a mature project workflow with a generic meta-tool without reason.

---

# 9. Visual regression

Use screenshot regression when:
- repeated states must remain stable;
- shared components have high blast radius;
- cross-browser/platform appearance matters;
- a redesign must prove no accidental regressions outside scope.

Always compare equivalent:
- viewport/window size;
- theme;
- content;
- platform;
- state;
- font availability.

Do not treat every pixel diff as a defect.

---

# 10. Tool trust tiers

## Tier A — inspect only
Usually safe to use when relevant:
- source search;
- static symbol inspection;
- project convention inspection;
- read-only metadata;
- local diff;
- screenshots of the user's own target app;
- existing build artifacts.

## Tier B — executes project/tool code
Use after source trust is adequate:
- builds;
- tests;
- lint with plugins;
- Playwright;
- coverage;
- profiling.

## Tier C — mutates project/system/external state
Use only with a clear task need and within environment permissions:
- package installation;
- git commit/push;
- registry/process changes;
- DB writes;
- release publishing;
- destructive cleanup.

Never silently escalate from A → B → C.

---

# 11. Before installing a new tool

Ask:

```text
DOES THE PROJECT ALREADY HAVE AN EQUIVALENT?
IS THIS TOOL NEEDED FOR ACCEPTANCE?
CAN IT BE RUN WITHOUT GLOBAL INSTALL?
IS THE VERSION PINNED?
HAS THE PACKAGE/REPO BEEN CHECKED?
DOES IT RUN INSTALL SCRIPTS?
WHAT FILES / NETWORK / PROCESS ACCESS DOES IT GET?
```

Prefer existing project dependencies.

Avoid toolchain bloat.

---

# 12. Evidence reporting

After using a tool:

```text
TOOL:
COMMAND / MODE:
OBSERVED:
PASS / FAIL / BLOCKED:
WHAT THIS PROVES:
WHAT IT DOES NOT PROVE:
```

A linter PASS does not prove good design.
A screenshot PASS does not prove keyboard accessibility.
A package scanner PASS does not prove a dependency is harmless.
A unit-test PASS does not prove the rendered state is correct.


## Source / freshness notes

For the public source links used when this catalog was authored, read:

`../../references/tooling-sources.md`

Do not treat the recorded package version as permanently current. Verify current upstream documentation before installation or use of version-sensitive flags.


## skills.sh discovery rule

skills.sh can be used to discover public agent skills and inspect their summaries, source repositories, install commands and audit signals.

Use it as a discovery/catalog source, not an automatic trust root.

Do not automatically run `npx skills add ...` from a listing. Inspect the source, permissions/scripts and current audit context first, then install only if the task materially benefits.
