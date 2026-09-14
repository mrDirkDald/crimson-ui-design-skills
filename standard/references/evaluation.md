# Skill Evaluation Suite

## Contents
- Goal
- Paired protocol
- Benchmark matrix
- Scoring rubric
- Failure weights
- Acceptance thresholds
- Repeated runs
- Golden expectations
- Regression dataset
- Version comparison
- Report format

## Goal

Measure whether the skill improves real outcomes enough to justify its context/tool cost.

Do not infer quality from prose, length, self-rating, or one successful demo.

## Paired protocol

Compare:
- baseline (no skill or previous stable skill);
- candidate skill.

Hold constant where practical:
- repository;
- task;
- starting commit/state;
- model;
- tools;
- permissions;
- time/token budget;
- runtime availability.

Run the same task independently.

## Benchmark matrix

Maintain tasks across these categories.

### A. Tiny refine / negative control
Example:
“Remove three redundant labels from this screen and preserve everything else.”

Expected:
- REFINE;
- no broad redesign;
- tiny diff;
- preserved functionality.

### B. Desktop queue utility
Example:
“Improve downloader queue hierarchy, progress state, long paths, and many-item behavior.”

Expected:
- Application;
- no marketing hero;
- many-item test;
- progress/cancel state;
- screenshot evidence.

### C. Native editor
Example:
“Improve a multi-document editor with selection, inspector, shortcuts, undo/autosave.”

Expected:
- editor pattern;
- command model;
- dirty/save state;
- no cardification.

### D. Mobile native
Example:
“Fix form flow under software keyboard, permissions, Back, safe area, process restoration.”

Expected:
- mobile-specific rules;
- no desktop-compressed solution.

### E. Browser SaaS auth
Example:
“Design session-expiry/reauth flow preserving unsaved work and intended route.”

Expected:
- Web auth/session;
- 401/403 distinction;
- route restoration.

### F. Dashboard/chart
Example:
“Improve dense chart/table dashboard without misleading axes or losing accessibility.”

Expected:
- honest scales;
- data alternative;
- filtering/table semantics.

### G. E-commerce
Example:
“Improve variant/stock/cart/checkout failure states.”

Expected:
- truthful price/stock;
- duplicate-submit protection;
- recovery.

### H. Docs/developer
Example:
“Improve long API docs page with TOC, anchors, code blocks and search.”

Expected:
- docs module;
- technical readability.

### I. Tauri UI integration
Example:
“Implement typed download progress/cancel with Rust↔TS IPC.”

Expected:
- Tauri UI ref;
- stable IDs;
- typed wrapper;
- real cancellation.

### J. Tauri native/security
Example:
“Add folder access and updater without broad capabilities.”

Expected:
- least privilege;
- input/path validation;
- integrity preserved.

### K. Electron
Example:
“Add secure preload IPC for file operation and window restore.”

Expected:
- Electron ref;
- renderer privilege minimized.

### L. Visual QA only
Example:
“Audit rendered UI at multiple sizes and inputs without changing code.”

Expected:
- REVIEW;
- evidence/severity;
- BLOCKED where runtime absent.

### M. Expressive consumer UI
Example:
“Refine a media/launcher UI while preserving strong brand motion/identity.”

Expected:
- anti-polish does not flatten expression.

## Scoring rubric — 100 points

### Request adherence — 20
- 20: acceptance criteria satisfied, no material scope drift
- 10: partial completion or unnecessary extra work
- 0: misses request

### Functional preservation/correctness — 20
- 20: no relevant regression
- 10: minor regression/recovery issue
- 0: major breakage

### UX/workflow quality — 15
- 15: clear workflow/state/navigation
- 8: mixed
- 0: structurally poor

### Visual/design quality — 10
- 10: intentional, product-appropriate, non-generic
- 5: safe/generic
- 0: materially harmful

### Accessibility — 10
- 10: relevant requirements preserved/verified
- 5: partial
- 0: major in-scope failure

### Verification evidence — 10
- 10: observed, environment recorded, BLOCKED honest
- 5: partial/static inference
- 0: fabricated PASS

### Routing/context discipline — 5
- 5: only relevant references loaded
- 2: unnecessary references
- 0: wrong specialist causes failure

### Change-set discipline — 5
- 5: coherent minimal scope
- 2: unnecessary churn
- 0: broad unrelated rewrite

### Efficiency — 5
Relative to baseline: token/tool/time cost with outcome quality.

## Failure weights

Apply penalties:
- unresolved BLOCKER: candidate fails regardless of score
- unresolved in-scope HIGH: -15 each
- functional regression: -20
- fabricated runtime PASS: -20
- major scope violation: -15
- unnecessary redesign on negative control: -10
- wrong routing with material impact: -10

Do not double-penalize the same root defect excessively.

## Acceptance thresholds

Candidate is eligible to replace current stable version only if:

1. no benchmark has unresolved BLOCKER caused by the skill;
2. mean score ≥ 85/100;
3. median score ≥ 85/100;
4. no category average < 75;
5. negative-control scope discipline ≥ 90%;
6. fabricated-PASS rate = 0%;
7. regression rate does not increase;
8. weighted quality gain exceeds context-cost increase.

## Repeated runs

For stochastic models:
- minimum 3 runs per high-variance benchmark when practical;
- report mean, median, min/max;
- do not promote a version based on one lucky run.

For expensive suites, run:
- smoke set every edit;
- full set before release.

## Golden expectations

Do not require one exact visual output.

Goldens should specify:
- required behaviors;
- forbidden regressions;
- expected routing;
- evidence requirements;
- critical structural properties.

Example:
```text
TASK: tiny label cleanup
MUST:
- remove only specified noise
- preserve queue/actions
- no redesign
- verify rendered result if runtime available
MUST NOT:
- add sidebar/cards
- rewrite layout
```

## Regression dataset

Maintain per released skill version:
- task prompt;
- repo fixture/commit;
- screenshots;
- runtime notes;
- baseline score;
- accepted candidate score;
- known tricky failure mode.

Add every discovered real-world failure as a regression case.

## Version comparison

For candidate C vs stable S:

```text
quality_delta = mean_score(C) - mean_score(S)
cost_delta = normalized_cost(C) - normalized_cost(S)
regression_delta = regression_rate(C) - regression_rate(S)
scope_delta = scope_violation_rate(C) - scope_violation_rate(S)
```

Promote when:
- `quality_delta > 0` materially;
- regression/scope do not worsen materially;
- extra cost is justified by quality gain;
- all acceptance thresholds pass.

Do not use a single scalar formula to hide a BLOCKER/regression.

## Report format

```text
VERSION:
BASELINE:
TASKS:
RUNS:

MEAN:
MEDIAN:
MIN:
MAX:

CATEGORY SCORES:
- tiny refine:
- desktop:
- mobile:
- web:
- stack integration:
- QA:

REGRESSIONS:
SCOPE VIOLATIONS:
FABRICATED PASS:
ROUTING ERRORS:
TOKEN/TOOL/TIME COST:

PROMOTE: YES / NO
REASONS:
```


## Executable infrastructure

This skill ships machine-readable benchmark specs in:

`evaluation/benchmarks/*.json`

Validate them with:

`scripts/validate_benchmarks.py`

Score a completed run record with:

`scripts/score_benchmark_run.py RUN.json`

Use:

`evaluation/score-template.json`

for run artifacts.

The shipped specs provide task contracts and assertions, but **do not pretend to contain real baseline/candidate outcomes**.

Real promotion evidence requires actual runs against repositories/fixtures and stored run artifacts.

## Fixture policy

A benchmark becomes a full regression fixture only when it has:
- a concrete repository or reproducible project fixture;
- pinned starting commit/archive;
- deterministic seed/data where practical;
- required runtime environment;
- expected evidence artifacts;
- at least one accepted baseline/candidate run.

Until then it is a **benchmark specification**, not a completed regression fixture.

Do not label synthetic prompt-only specs as empirical evidence.


## Executable fixture corpus

Each benchmark category now has a reproducible fixture in:
`evaluation/fixtures/<id>/`

Each fixture contains:
- `baseline/` — intentionally broken starting state;
- `golden/` — evaluator-only contract-satisfying reference state;
- `checks.json` — executable good-state assertions.

Candidate agents must not be shown `golden/` during a benchmark run.

Run machine checks with:
`scripts/run_fixture_checks.py FIXTURE WORKSPACE`

Validate the entire fixture corpus with:
`scripts/validate_fixture_corpus.py`

Corpus validation requires:
- at least 4 executable checks per fixture;
- at least 50 machine-check weight per fixture;
- baseline fails at least 2 checks;
- golden passes every check.

## Scoring split

Benchmark score is no longer fully hand-entered.

- machine assertions: normalized to `60/100`;
- manual expert rubric: `40/100` total:
  - UX/workflow: 15;
  - visual design: 10;
  - platform fit: 5;
  - evidence quality: 10.

Use `scripts/score_benchmark_run.py` to combine machine result + manual rubric + penalties.

Machine checks do not pretend to measure all design quality. They lock behavior/security/scope contracts while expert scoring covers inherently qualitative visual/UX judgment.

## Empirical promotion evidence

A fixture corpus is infrastructure, not proof that the current skill outperforms another model or skill revision.
A true release comparison still requires repeated baseline-vs-candidate agent runs stored as run artifacts.
Do not fabricate those results.

## Repeated-run aggregator

Store empirical run records as JSON conforming to:
`evaluation/run.schema.json`

Aggregate and compare versions with:
`scripts/aggregate_evaluation.py RUNS_DIR --candidate VERSION [--baseline VERSION]`

The aggregator reports:
- mean/median/min/max;
- category means;
- run count per benchmark;
- regressions;
- scope violations;
- fabricated PASS count;
- blockers;
- token/tool/time averages;
- promotion decision using the suite thresholds.

For high-variance benchmarks, fewer than 3 candidate runs is reported as insufficient promotion evidence.


## Trigger discrimination evaluation

Evaluate activation quality separately from design-output quality.

Maintain both:
- positive trigger prompts that require UI/UX judgment;
- near-neighbor negative prompts that should not activate the skill.

Track false positives such as backend-only work, ordinary data/API logic, and implementation that follows a complete design with no material UI decision.

## Process determinism evaluation

The desired invariant is a repeatable decision process, not visually identical output.

Across equivalent runs, check whether the agent consistently:
- establishes scope/contract;
- inspects the real product;
- diagnoses evidence-backed problems;
- selects direction from the brief;
- preserves required behavior;
- verifies in bounded passes.

Do not reward identical palettes/layouts across unrelated briefs.
