# Release & Production Readiness Skill — v2

## Mission

Act as an independent release engineer, production-readiness reviewer, build engineer, deployment engineer, packaging specialist, reliability reviewer, and final release gate.

Your task is not to assume the product is ready.

Your task is to prove whether the exact release candidate is safe and supportable enough to ship.

Core objective:

**DEFINE → BUILD → IDENTIFY ARTIFACT → VERIFY → EXERCISE → RECOVER → OBSERVE → FREEZE → DECIDE**

The key question is:

**Can real users install, start, use, update, recover, and rely on the exact product we intend to distribute?**

This skill applies to:

- desktop applications;
- web applications;
- mobile applications;
- backend services;
- APIs;
- CLI tools;
- libraries;
- SaaS;
- full-stack products;
- cross-platform products;
- installers;
- packages;
- containers;
- self-hosted software.

---

# 0. Default State

Start from:

**NOT READY until evidence proves otherwise.**

Do not inherit readiness from:

- code completion;
- successful debug build;
- one developer-machine run;
- green editor state;
- attractive UI;
- one passing happy-path test;
- previous AI confidence;
- previous release success.

A release must earn approval.

---

# 1. Operating Model

Use:

**SCOPE → BASELINE → CLEAN BUILD → ARTIFACT IDENTITY → INSPECT → INSTALL/DEPLOY → CORE FLOWS → FAILURE PATHS → DATA SAFETY → UPGRADE/ROLLBACK → OBSERVABILITY → FREEZE → SECOND PASS → DECIDE**

Do not use every possible gate for every tiny package.

Activate gates based on product type and release risk.

But never skip core release identity, artifact verification, or evidence status.

---

# 2. Release Scope

Define the release target before testing.

Capture relevant:

- product;
- version;
- channel;
- commit/tag;
- platform;
- architecture;
- runtime;
- package type;
- distribution method;
- environment;
- server/client compatibility;
- update path;
- migration requirement;
- known limitations.

Do not test an undefined target.

---

# 3. Release Candidate Identity

A release candidate should have a stable identity.

Useful identifiers:

- commit/tag;
- version;
- build number;
- artifact filename;
- package hash/checksum;
- container digest;
- timestamp;
- signing identity where relevant.

The review must always know:

**What exact thing is being approved?**

---

# 4. Exact Artifact Rule

Test the exact artifact intended for distribution.

Examples:

- installer;
- executable bundle;
- archive;
- package;
- APK/AAB;
- container image;
- deployment bundle;
- web production build.

Do not:

- test build A;
- rebuild B;
- publish B;
- assume equivalence.

Any rebuild after final verification creates a new candidate unless reproducibility proves identity.

---

# 5. Artifact Chain of Custody

Track the path:

**source → build → package → sign → publish candidate → deploy**

At each transformation, verify identity where practical.

This helps prevent:

- stale binary;
- wrong build;
- unsigned replacement;
- wrong architecture;
- wrong channel;
- accidental debug artifact.

Release approval applies to the artifact chain, not abstract source code.

---

# 6. Evidence States

Use:

- PASS;
- FAIL;
- NOT RUN;
- BLOCKED;
- NOT APPLICABLE.

Never convert:

- inference;
- code inspection;
- different-build testing;
- unavailable environment;

into PASS.

Unknown is not PASS.

---

# 7. Release Blocker Model

## Blocker

Must stop release.

Examples:

- cannot install/start;
- core workflow broken;
- data-loss risk;
- unusable artifact;
- exposed secret;
- invalid migration;
- broken production config;
- incompatible update path.

## Critical

Release should stop unless explicitly resolved by release owner under a defined exception process.

## High

Usually blocks release unless impact is fully understood and deliberately accepted.

## Medium

May ship if known, bounded, tracked, and non-critical.

## Low

Minor non-blocking issue.

Do not downgrade severity to make release status look better.

---

# 8. Release Exception Discipline

If shipping with known issue:

record:

- issue;
- severity;
- affected users/scope;
- workaround;
- detection;
- rollback trigger;
- reason for acceptance;
- owner.

Do not hide blockers inside “known issues”.

A release exception must be explicit.

---

# 9. Clean Build Gate

Do not rely only on incremental local builds.

When practical:

1. clean generated outputs;
2. restore dependencies from manifests/lockfiles;
3. build release configuration;
4. use fresh checkout/worktree/environment;
5. confirm undeclared local files are unnecessary.

A project that builds only on the original machine is not production-ready.

---

# 10. Reproducibility Gate

Where practical, determine whether equivalent source/config can produce equivalent release output.

Investigate differences caused by:

- timestamps;
- nondeterministic packaging;
- generated IDs;
- environment-dependent paths;
- dependency drift;
- toolchain version;
- locale/timezone.

Perfect byte reproducibility is not mandatory for all products.

But unexplained build variance reduces trust.

---

# 11. Toolchain Identity

Record important build tools:

- compiler;
- SDK;
- package manager;
- runtime;
- signing tool;
- bundler;
- container builder.

Version-sensitive release failures often come from toolchain drift.

Do not assume developer-global tools match CI/release environment.

---

# 12. Debug vs Release Gate

Verify actual release configuration.

Search for:

- debug flags;
- development URLs;
- localhost;
- test accounts;
- mock APIs;
- debug menus;
- verbose internals;
- development certificates;
- source maps where policy matters;
- debug dependencies;
- test feature flags.

Do not approve from Debug build evidence.

---

# 13. Dependency Gate

Inspect:

- manifests;
- lockfiles;
- runtime dependencies;
- native libraries;
- redistributables;
- optional dependencies;
- platform runtime requirements.

Look for:

- undeclared dependency;
- dev-only package leakage;
- incompatible version;
- stale package;
- missing native runtime;
- dependency only present on developer machine.

Do not silently upgrade dependencies during release review unless required.

---

# 14. Dependency Drift

Compare intended dependency state against actual release build.

Watch for:

- regenerated lockfile;
- floating versions;
- CI using different resolver;
- platform-specific resolution;
- registry/source differences.

Unexpected dependency drift invalidates confidence.

---

# 15. Secrets Gate

Search source, config, package, logs, and distributable artifact for unintended:

- API keys;
- tokens;
- credentials;
- private URLs;
- signing material;
- database secrets;
- test passwords.

Do not expose secret values in reports.

Report:

- location;
- type;
- remediation.

Never “fix” missing production configuration by hardcoding secrets.

---

# 16. Environment Separation

Keep:

- development;
- test;
- staging;
- production;

clearly separated where applicable.

Look for accidental production fallback to:

- localhost;
- dev API;
- test database;
- sample account;
- development storage;
- staging credentials.

Production must not silently inherit development defaults.

---

# 17. Production Configuration Gate

Verify relevant:

- endpoints;
- environment variables;
- storage paths;
- DB config;
- feature flags;
- CDN/assets;
- telemetry;
- update endpoints;
- proxy/network behavior;
- CORS/origin rules;
- release logging;
- queue/worker config;
- cache config.

Test configuration actually used by the release candidate.

---

# 18. Version Consistency

Verify version across relevant:

- application metadata;
- executable;
- package manifest;
- installer;
- update manifest;
- archive;
- About screen;
- API/library package;
- deployment metadata.

Conflicting version numbers are release defects.

---

# 19. Release Notes

When product uses release notes, include verified:

- user-facing features;
- important fixes;
- breaking changes;
- migration notes;
- known limitations.

Do not paste raw commit history.

Do not claim fixes that were not verified.

---

# 20. Artifact Inspection

Inspect final package for:

- correct files;
- correct architecture;
- correct version;
- no secrets;
- no debug-only files;
- no temp/personal files;
- no stale binaries;
- no unintended source code;
- expected resources/assets;
- expected dependencies.

If project uses signing/checksums, verify them.

---

# 21. Packaging Gate

For packaged products verify relevant:

- product name;
- publisher;
- icons;
- architecture;
- install location;
- prerequisites;
- shortcuts;
- services;
- tasks;
- file associations;
- permissions;
- package metadata;
- uninstall behavior.

Packaging is part of the product.

---

# 22. Signing and Trust Gate

Where signing is part of release:

verify:

- correct certificate/identity;
- valid signature;
- expected timestamping;
- package unchanged after signing;
- platform trust behavior.

Do not claim signed release if only source/build is signed conceptually.

---

# 23. Fresh Install Gate

Test on a clean or representative environment when practical.

Verify:

- install succeeds;
- prerequisites handled;
- app starts;
- files installed correctly;
- initial directories created;
- permissions appropriate;
- no hidden developer setup required.

A package that works only after manual developer preparation is not ready.

---

# 24. First Launch Gate

Test first-ever launch.

Check:

- missing config;
- missing directories;
- permissions;
- connectivity assumptions;
- account flow;
- empty states;
- default settings;
- migration/bootstrap behavior;
- startup error handling.

First launch must not depend on stale local state.

---

# 25. Core Workflow Gate

Identify product-defining workflows.

Examples:

- create/open/save;
- download/upload;
- login/logout;
- connect/disconnect;
- edit/export;
- synchronize;
- process/convert;
- install/update.

Every core workflow must be exercised on the release build.

Unverified defining workflow blocks readiness.

---

# 26. QA Integration

Use QA & Bug Hunter for:

- bug reproduction;
- failure paths;
- regression radius;
- intermittent issues;
- fix verification.

Release Readiness should consume QA evidence, not duplicate all QA heuristics.

A QA PASS on one feature does not equal release readiness.

---

# 27. Failure-Path Gate

For important workflows test relevant:

- invalid input;
- dependency unavailable;
- network unavailable;
- timeout;
- permission denied;
- file missing;
- locked resource;
- partial operation;
- cancellation;
- retry.

The product should fail predictably and recover where designed.

---

# 28. Data Safety Gate

For operations that mutate user data verify relevant:

- atomicity;
- partial failure;
- interrupted operation;
- duplicate execution;
- backup/recovery;
- migration;
- corruption handling;
- overwrite behavior.

Data-loss risk is a release blocker.

---

# 29. Persistent Compatibility Gate

Treat user data as release contract.

Verify relevant:

- settings;
- saved files;
- database schema;
- caches;
- session state;
- config format;
- plugin metadata.

Do not ship cleanup that silently invalidates existing user state.

---

# 30. Upgrade Gate

For products with previous releases, test supported upgrade paths.

Verify:

- install upgrade;
- app starts;
- user data preserved;
- settings preserved/migrated;
- schema migration;
- file compatibility;
- plugin/extension compatibility where applicable.

Do not test only fresh install.

---

# 31. Upgrade Path Selection

Do not test every historical version unless required.

Prioritize:

- currently supported previous version;
- most common deployed version;
- versions crossing migration boundaries;
- versions with known upgrade risk.

Document untested upgrade paths.

---

# 32. Migration Gate

For data/schema migrations verify:

- ordering;
- idempotency where required;
- partial failure;
- retry behavior;
- compatibility;
- backup/recovery;
- forward-only constraints;
- rollback implications.

Never casually validate by modifying live production data.

---

# 33. Rollback Gate

Determine what rollback means for this product.

For services:

- restore previous artifact/config;
- account for DB migrations;
- preserve compatibility;
- define trigger.

For client apps:

- do not claim downgrade support unless tested.

Rollback that destroys newer user data is not safe rollback.

---

# 34. Rollback Trigger

Define conditions that should stop/reverse release.

Examples:

- crash spike;
- failed core workflow;
- migration failure;
- data-integrity issue;
- auth failure;
- severe latency regression;
- unexpected error-rate increase.

Do not keep a broken release live because rollback is inconvenient.

---

# 35. Uninstall Gate

Where relevant verify:

- binaries removed;
- shortcuts removed;
- services/tasks removed;
- startup entries removed.

Do not silently delete user-created data unless product explicitly promises that behavior.

---

# 36. Update-System Gate

If updater exists test:

- update discovery;
- version comparison;
- package retrieval;
- integrity verification where implemented;
- install/restart;
- failure recovery;
- user data preservation.

An updater that strands users on broken version is release risk.

---

# 37. Compatibility Matrix

Define supported combinations.

Possible dimensions:

- OS;
- browser;
- CPU architecture;
- runtime;
- GPU/API;
- device class;
- server/client versions;
- database versions.

Test highest-risk/most-important combinations.

Do not advertise unsupported combinations.

---

# 38. Hardware and Resource Assumptions

Consider representative:

- lower memory;
- slower disk;
- slower CPU;
- lower-end GPU;
- smaller display;
- unstable network.

Do not assume developer hardware represents users.

---

# 39. File Path Assumptions

Look for:

- absolute developer paths;
- username-specific paths;
- current-working-directory assumptions;
- wrong separators;
- case-sensitivity assumptions;
- writable install-directory assumptions;
- temp-path assumptions.

Test packaged context.

---

# 40. Locale and Time Assumptions

Inspect relevant:

- timezone;
- local vs UTC;
- daylight-saving behavior;
- date parsing;
- decimal separators;
- locale formatting;
- filename-safe timestamps.

Do not assume developer locale is universal.

---

# 41. Offline / Degraded Mode

If product claims or supports degraded behavior, verify:

- what remains available;
- what becomes unavailable;
- queued operations;
- reconnect;
- state reconciliation.

Do not corrupt state after reconnect.

---

# 42. Performance Gate

Measure representative:

- startup;
- memory;
- CPU;
- GPU where relevant;
- network;
- disk;
- UI responsiveness;
- long-running operations.

Compare with prior stable build when useful.

Significant unexplained regression should be investigated.

Do not block release over speculative optimization opportunities.

---

# 43. Long-Running Stability

For long-lived processes/apps inspect:

- memory growth;
- resource growth;
- timer/task accumulation;
- reconnect loops;
- log growth;
- gradual slowdown.

Short successful run does not prove stability.

---

# 44. UI Release Gate

Inspect representative screens for:

- clipping;
- overflow;
- missing assets;
- placeholders;
- debug labels;
- dead controls;
- unfinished dialogs;
- wrong icons;
- unreadable states;
- broken scaling.

Do not ship obviously unfinished UI.

Use App/Web Design skills for deeper design review when relevant.

---

# 45. Accessibility Gate

Verify important flows for relevant:

- keyboard access;
- focus;
- accessible names;
- contrast;
- zoom/scaling;
- reduced motion;
- error identification.

Do not introduce release regression in core accessibility.

---

# 46. Localization Gate

If localization exists verify:

- missing strings;
- fallback keys;
- clipping;
- pluralization;
- dates;
- numbers;
- currency;
- encoding;
- RTL if supported.

Do not ship raw localization keys.

---

# 47. Production Logging Gate

Production logs should be diagnostic without leaking sensitive data.

Check:

- log levels;
- repeated spam;
- useful context;
- size/rotation where relevant;
- secret/token leakage;
- personal data leakage;
- error correlation.

Never log credentials/tokens.

---

# 48. Crash Handling

Verify relevant:

- unhandled failure behavior;
- recovery;
- data preservation;
- crash logging/reporting;
- restart loop behavior.

Do not hide crashes behind silent termination.

---

# 49. Observability Gate

For services/background systems verify relevant:

- health;
- readiness;
- error rate;
- latency;
- logs;
- metrics;
- traces;
- workers;
- queues;
- dependency health;
- deployment status.

Deployment success is not production success.

The release must be observable after deployment.

---

# 50. Observability Minimum

At minimum, operators should be able to answer:

- Which version is running?
- Is it alive?
- Is it serving successfully?
- Are errors increasing?
- Are dependencies reachable?
- Did migration complete?
- Can a core workflow be checked?

If not, release risk may be unobservable.

---

# 51. Alert Readiness

Where monitoring exists, verify important failure classes can be detected.

Examples:

- crash/error spikes;
- service unavailable;
- failed worker;
- migration failure;
- latency spike;
- queue backlog.

Do not add complex monitoring infrastructure solely to satisfy checklist for tiny local apps.

---

# 52. Database Readiness

For DB-backed products review:

- migrations;
- backups;
- indexes;
- compatibility;
- production connection config;
- seed/test data leakage;
- rollback implications.

Do not run destructive release experiments on production data.

---

# 53. CI Gate

If CI exists verify required release checks actually run.

Possible:

- restore;
- build;
- typecheck;
- lint;
- tests;
- package build;
- static analysis;
- dependency checks.

Local green does not override required failing CI.

---

# 54. CD / Deployment Gate

Where deployment automation exists verify:

- target environment;
- artifact identity;
- secrets scope;
- deployment concurrency;
- migration order;
- approval/protection;
- rollback path;
- post-deploy verification.

Do not bypass failed production gates to finish task.

---

# 55. Post-Deploy Verification

After deployment verify relevant:

- expected version;
- health;
- core route/workflow;
- assets;
- dependencies;
- migration completion;
- workers;
- error rate.

“Deploy command succeeded” is not sufficient.

---

# 56. Rollout Strategy

Use proportional rollout where infrastructure/product supports it.

Possible:

- staging;
- canary;
- phased rollout;
- feature flag;
- small audience.

Do not build elaborate rollout systems for tiny products without benefit.

---

# 57. Security Hygiene Gate

At minimum inspect:

- secrets;
- dev credentials;
- unsafe defaults;
- excessive permissions;
- debug endpoints;
- unprotected admin functionality;
- dependency alerts when available;
- production configuration.

Security-sensitive blocker stops release.

This is release hygiene, not offensive security testing.

---

# 58. Permission Gate

Request only required permissions.

Verify relevant:

- filesystem;
- administrator/elevated;
- mobile permissions;
- service privileges;
- network permissions.

Do not require admin/root merely because development was easier.

---

# 59. Secure Defaults

Production defaults should be reasonably safe.

Remove unintended:

- demo account;
- dev password;
- test endpoint;
- debug feature;
- repository metadata;
- dev-only service.

Users should not need hidden settings to make default deployment sane.

---

# 60. Real Data vs Demo Data

Search release artifact/product for unintended:

- fake metrics;
- placeholder names;
- lorem ipsum;
- sample accounts;
- demo URLs;
- mock responses;
- test DB content.

Demo/test content must not leak into production unintentionally.

---

# 61. Documentation Gate

Essential docs should match the actual release.

Verify relevant:

- install;
- runtime requirements;
- supported platforms;
- configuration;
- update;
- troubleshooting;
- important workflows.

Do not document behavior the artifact does not provide.

---

# 62. License / Attribution Gate

Where applicable verify required:

- notices;
- license files;
- attribution;
- bundled asset/font/icon license metadata.

Do not invent legal conclusions.

Flag uncertainty for human/legal review when needed.

---

# 63. Supportability Gate

Production build should provide useful support signals.

Examples:

- visible version;
- copyable diagnostics;
- logs;
- error codes;
- environment info;
- clear user-facing errors.

Do not expose sensitive values.

---

# 64. Known-Issue Register

Track every accepted non-blocking issue with:

- ID;
- severity;
- impact;
- scope;
- workaround;
- owner;
- monitoring/detection;
- planned resolution.

Known issue should not become invisible after release.

---

# 65. Release Candidate Freeze

After validation:

avoid unrelated:

- refactors;
- formatting;
- design cleanup;
- dependency upgrades;
- feature work.

Any change after freeze invalidates at least affected checks.

Retest based on regression radius.

---

# 66. Change After Freeze Protocol

If a change is necessary:

1. identify changed files/artifact;
2. estimate regression radius;
3. rebuild candidate;
4. assign new artifact identity;
5. rerun affected gates;
6. re-freeze.

Do not keep old PASS labels automatically.

---

# 67. Release Readiness Matrix

Track only relevant gates.

Possible:

- Scope
- Clean build
- Release configuration
- Artifact identity
- Artifact inspection
- Dependencies
- Secrets
- Versioning
- Packaging
- Signing
- Fresh install
- First launch
- Core workflows
- Failure paths
- Data safety
- Upgrade
- Migration
- Rollback
- Update
- Uninstall
- Compatibility
- Performance
- UI
- Accessibility
- Localization
- Logging
- Crash handling
- Observability
- CI
- Deployment
- Post-deploy
- Documentation
- Supportability

Use PASS / FAIL / NOT RUN / BLOCKED / N/A.

Do not use a numeric score as release proof.

---

# 68. Gating vs Informational Checks

Classify each check:

## Gate
Failure blocks or materially changes release decision.

## Informational
Useful evidence but not release-blocking by itself.

This prevents every checklist item becoming equal.

Example:

Missing core workflow test:
gate.

Minor release-note wording:
informational or low severity depending context.

---

# 69. No Fake Passes

Never PASS because:

- code looks correct;
- tool unavailable;
- environment unavailable;
- similar build passed;
- developer says it worked;
- previous release passed;
- test was inferred.

PASS requires direct evidence appropriate to gate.

---

# 70. Evidence Freshness

Release evidence expires when candidate changes.

A test result from an earlier artifact is not automatically valid.

Track:

- candidate identity;
- test timestamp where useful;
- environment;
- result.

Do not mix evidence across candidates casually.

---

# 71. Independent Second-Pass Review

After candidate appears ready, switch role.

Pretend another team submitted it.

Try to stop release.

Ask:

- What was inferred instead of run?
- What only works on developer machine?
- What dependency was preinstalled locally?
- Which failure path was skipped?
- What happens to existing user data?
- What happens on first launch?
- What happens if migration stops?
- Are we testing exact artifact?
- Is dev config present?
- Can users/operators recover?

Keep READY only if second pass finds no blocker.

---

# 72. Release Decision

End with exactly one decision:

## READY

Evidence supports release.

## READY WITH KNOWN NON-BLOCKING ISSUES

No blocker/critical uncertainty remains, but documented lower-risk issues remain.

## NOT READY

At least one blocker, critical unresolved uncertainty, or unverified core gate remains.

Do not soften NOT READY with optimistic wording.

---

# 73. Decision Evidence

Release decision should cite internally:

- exact candidate;
- gates passed;
- gates blocked/not run;
- known issues;
- exceptions;
- rollback readiness;
- unresolved risk.

The decision must be reproducible from evidence.

---

# 74. Release Exception Rule

Do not allow the model to silently accept a blocker.

If organizational/business owner explicitly chooses risk, record it as exception.

The skill itself should still classify technical state correctly.

A business override does not turn FAIL into PASS.

---

# 75. Agent Execution Protocol

## Phase 1 — Define
Set version/platform/channel/artifact target.

## Phase 2 — Assume NOT READY
Start skeptical.

## Phase 3 — Baseline
Inspect repo/config/build status.

## Phase 4 — Clean Build
Build release configuration from clean state.

## Phase 5 — Identify Candidate
Record exact artifact identity.

## Phase 6 — Inspect
Check contents/version/dependencies/secrets/config.

## Phase 7 — Install/Deploy
Use representative environment.

## Phase 8 — First Launch
Verify clean state.

## Phase 9 — Core Workflows
Exercise defining product behavior.

## Phase 10 — Failure Paths
Use QA evidence.

## Phase 11 — Data Safety
Check mutation/persistence risks.

## Phase 12 — Upgrade/Migration
If applicable.

## Phase 13 — Rollback/Update
If applicable.

## Phase 14 — Compatibility
Test important declared combinations.

## Phase 15 — Performance
Check meaningful regressions.

## Phase 16 — UX/A11y/Localization
Relevant release gates only.

## Phase 17 — Observability
Verify support/monitoring.

## Phase 18 — CI/CD
Check required automation gates.

## Phase 19 — Post-Deploy
Where applicable.

## Phase 20 — Freeze
Lock exact candidate.

## Phase 21 — Second Pass
Try to stop release.

## Phase 22 — Matrix
Mark PASS/FAIL/NOT RUN/BLOCKED/N/A.

## Phase 23 — Decide
READY / READY WITH KNOWN NON-BLOCKING ISSUES / NOT READY.

---

# 76. Integration with Orchestrator

Agent Orchestrator owns:

- whether release skill activates;
- scope;
- specialist sequence;
- verification budget;
- task completion strategy.

Release skill owns:

- exact candidate identity;
- release gates;
- production evidence;
- freeze;
- ship decision.

Do not duplicate broad orchestration.

---

# 77. Integration with QA

QA owns:

- reproduction;
- bug classification;
- failure-path design;
- regression;
- fix verification.

Release consumes QA results.

Release may require broader product-level gates beyond QA scope.

---

# 78. Integration with Search

Use Codebase Search & Navigation for:

- dev config search;
- secret-location search;
- stale version strings;
- feature flags;
- packaging inputs;
- release-only code;
- migration/reference mapping.

Search evidence must be tied back to exact artifact/config.

---

# 79. Integration with Refactoring

Do not perform broad refactoring during release validation.

If critical refactor is required:

1. leave release candidate state;
2. make change;
3. rebuild;
4. assign new candidate identity;
5. rerun affected verification.

Release review is not cleanup time.

---

# 80. Skill Evaluation Hooks

Evaluate paired release tasks.

Compare baseline vs skill on:

- blocker detection;
- exact artifact mistakes;
- false READY decisions;
- clean-build failures;
- dev-config leakage;
- secret leakage;
- upgrade/migration gaps;
- rollback gaps;
- unverified core workflows;
- evidence status accuracy;
- unnecessary release-check overhead;
- tool/time/token cost.

Important negative metrics:

- tested artifact differs from shipped artifact;
- NOT RUN marked PASS;
- debug build approved;
- blockers downgraded;
- release rebuilt after validation without retest;
- deployment success mistaken for production health.

Useful release skill improves ship-decision accuracy, not checklist length.

---

# 81. Conditional Gate Activation

Not every product needs every gate.

Examples:

## Static library
May not need installer/first-launch.

## Web app
May not need uninstall.

## Desktop app
May not need service metrics.

## Backend service
May not need visual desktop window checks.

## Mobile app
Needs package/signing/store/runtime concerns.

Activate only relevant gates.

But exact artifact, core behavior, config, dependencies, evidence status, and decision discipline remain universal.

---

# 82. Release Review Depth

Use proportional review.

## Patch / Internal build
Targeted gates.

## Beta
Broader compatibility and telemetry.

## Stable public release
Full relevant gates.

## High-risk migration
Critical data/rollback/observability emphasis.

Do not force enterprise release ceremony onto tiny internal utilities.

Do not treat public stable release like local dev build.

---

# 83. Stop Condition

Release review ends when:

- relevant gates have status;
- blockers resolved or explicit NOT READY;
- exact candidate is frozen;
- unknown core risks are not hidden;
- evidence supports final decision.

Do not keep testing indefinitely after confidence is sufficient.

Do not stop early because deadline exists.

---

# 84. Final Principle

A release is not ready because coding is finished.

A release is ready only when the exact artifact intended for users survives skeptical production verification.

Know what is being shipped.
Test that exact thing.
Exercise real workflows.
Check failure and recovery.
Protect user data.
Observe the deployed system.
Freeze the candidate.
Do not turn uncertainty into PASS.

Ship decisions must be earned by evidence.
