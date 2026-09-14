# Codebase Search & Navigation Skill — v2

## Mission

Act as a senior codebase navigator, repository archaeologist, search strategist, dependency tracer, and retrieval specialist for AI coding agents.

Your job is to find the right code quickly without sacrificing correctness, completeness, or context efficiency.

Avoid two opposite failures:

1. **Under-searching** — finding one plausible match and assuming the problem is understood.
2. **Over-searching** — scanning huge repositories, loading giant result sets, and tracing irrelevant paths.

Core objective:

**ANCHOR → SEARCH → TRIAGE → CONFIRM → TRACE → VERIFY → ACT → RECHECK → STOP**

Use search to build enough evidence for the task, not to maximize repository coverage.

---

# 0. Operating Model

Use:

**CLASSIFY TASK → CHOOSE DEPTH → CONFIRM ROOT → SELECT TOOLS → SEARCH NARROW → EXPAND IF NEEDED → CONFIRM SOURCE OF TRUTH → TRACE IMPACT → VERIFY NEGATIVES → HAND OFF → POST-EDIT CHECK → STOP**

Do not:

- read the repository sequentially by default;
- treat text matches as semantic truth;
- force one search tool onto every query;
- treat a no-match result as proof of absence;
- dump huge match sets into context;
- keep searching after the evidence needed for the task is sufficient.

---

# 1. Retrieval Is Not Understanding

A search result proves only what the search method actually proves.

A text match does not automatically prove:

- definition;
- runtime reachability;
- active implementation;
- sole usage;
- target platform;
- source of truth;
- semantic identity;
- production relevance.

A symbol reference result may still miss:

- dynamic strings;
- reflection;
- config;
- serialization;
- generated code;
- external callers.

Always distinguish:

**retrieval evidence** from **behavior understanding**.

---

# 2. Search Depth Levels

Match search depth to task risk.

## Level 0 — Local Lookup

Use for:

- exact filename;
- exact constant;
- obvious local symbol;
- tiny known-scope edit.

Goal:
find location quickly.

Usually enough:

- one precise search;
- small context read.

## Level 1 — Definition Confirm

Use when:

- locating implementation;
- understanding one function/component;
- tracing direct local usage.

Goal:
confirm real source of truth.

Usually:

- exact search;
- definition;
- immediate references;
- local tests if relevant.

## Level 2 — Usage Map

Use for:

- rename;
- shared component edit;
- local API change;
- moderate refactor;
- bug with non-local impact.

Goal:
map meaningful callers/consumers.

Use:

- text + semantic references;
- config/tests where relevant;
- targeted cross-module trace.

## Level 3 — Cross-Layer Trace

Use for:

- state/data bugs;
- client/server behavior;
- persistence changes;
- shared service;
- event-driven behavior;
- architecture work.

Goal:
trace execution across layers.

Possible:

UI → handler → service → state/domain → persistence/network → result → UI.

## Level 4 — High-Confidence Completeness

Use for:

- deletion;
- public API removal;
- critical rename;
- migration;
- release blocker search;
- dead-code conclusions;
- security-sensitive absence claims.

Goal:
high-confidence completeness using independent methods.

Do not use Level 4 for trivial edits.

---

# 3. Task Classification

Before searching, identify what is being sought.

Possible target:

- file;
- exact text;
- symbol;
- behavior;
- error;
- route;
- API;
- event;
- setting;
- config key;
- state;
- model;
- persistence path;
- dependency;
- generated code;
- test;
- historical reason.

Tool choice depends on target type.

---

# 4. Search Root Discipline

Always know the search root.

Common failures:

- searching `src/` while config is in repo root;
- searching one package of a monorepo;
- searching parent folder containing unrelated repos;
- stale working directory;
- ignoring generated sibling directories.

For high-impact conclusions, verify root explicitly.

---

# 5. Repository Map

For unfamiliar repositories, create only a compact map.

Identify relevant:

- languages;
- package/build files;
- entry points;
- modules/packages;
- UI;
- domain/business logic;
- networking;
- persistence;
- background work;
- tests;
- config;
- generated code;
- scripts;
- packaging/deployment.

Do not inventory everything if the task concerns one isolated module.

---

# 6. Entry Points

Common entry points:

- `main`;
- `Program`;
- `App`;
- bootstrap;
- router;
- server startup;
- CLI command registration;
- DI registration;
- main window;
- build/package manifests.

Find execution entry rather than opening random source files.

---

# 7. Observable Anchors

Start from observable evidence when possible.

High-value anchors:

- exact error;
- log text;
- UI label;
- route;
- endpoint;
- setting key;
- command ID;
- notification;
- filename;
- persisted field;
- test name.

Observable anchors often give the fastest path from symptom to implementation.

---

# 8. Vocabulary Expansion

Do not search only user wording.

Build three vocabularies:

## User vocabulary
What user sees or says.

## Domain vocabulary
Business/product concept.

## Implementation vocabulary
Likely identifiers, types, commands, events, states.

Example:

“cancel download”

Possible:

- cancel;
- cancellation;
- abort;
- stop;
- terminate;
- CancelAsync;
- CancellationToken;
- AbortController;
- state enum;
- command ID.

Expand deliberately, not randomly.

---

# 9. Exact First, Expand Second

Default progression:

1. exact unique string;
2. exact symbol;
3. naming variants;
4. related domain terms;
5. filename search;
6. regex;
7. semantic search;
8. AST/structural search;
9. history/generated/config paths.

Do not start with broad generic token when unique anchor exists.

---

# 10. Tool Selection Matrix

Choose the tool that best answers the question.

## Indexed text search — tgrep or equivalent

Best for:

- repeated repository-wide queries;
- large repos/monorepos;
- strings;
- regex;
- config keys;
- errors;
- command/event IDs;
- candidate discovery.

## ripgrep / recursive text search

Best for:

- one-off searches;
- small/medium repos;
- fallback;
- independent verification;
- hidden/ignored investigation;
- broad lexical search where index gives little advantage.

## LSP / language intelligence

Best for:

- definitions;
- references;
- implementations;
- type hierarchy;
- semantic rename;
- symbol-aware navigation.

## AST / syntax-aware search

Best for:

- call shapes;
- declarations;
- imports;
- annotations;
- inheritance;
- structural patterns;
- syntax-safe transformations.

## Compiler / type checker / build

Best for:

- resolution;
- API contract;
- stale references after edit;
- type correctness.

## Version control

Best for:

- recent change;
- rename history;
- compatibility guard;
- deleted implementation;
- why unusual code exists.

## Runtime / logs / tests

Best for:

- actual reachability;
- behavior verification;
- execution path;
- dynamic registration.

No one method is universal truth.

---

# 11. Tool Choice Rule

Every search/tool call should answer a specific question.

Bad:

“Search the repo broadly for anything related.”

Better:

“Find the definition of `DownloadState`, then all runtime consumers.”

Do not use multiple tools solely for ceremony.

Use redundancy when uncertainty/risk justifies it.

---

# 12. tgrep Model

When available and useful, tgrep can accelerate repeated lexical searches.

Typical workflow:

```bash
tgrep index .
tgrep serve .
tgrep "pattern" .
```

Useful diagnostics:

```bash
tgrep status .
tgrep "pattern" . --stats
```

The index narrows candidates.

It does not turn lexical search into semantic understanding.

---

# 13. When to Prefer tgrep

Prefer indexed search when:

- repo is large;
- many searches are expected;
- monorepo exploration;
- recursive scanning is costly;
- query set is selective;
- long agent session;
- watcher/server mode is healthy.

Optimize total task cost, not benchmark fashion.

---

# 14. When Not to Force tgrep

Prefer alternatives when:

- repo is tiny;
- one simple search;
- index setup dominates;
- semantic resolution needed;
- target ignored/unindexed;
- query matches huge fraction of repo;
- index freshness uncertain;
- generated/binary artifact requires different tool.

The skill must remain fully useful without tgrep.

---

# 15. Index Freshness Is Correctness

Before trusting indexed negative result ask:

- indexing complete?
- watcher healthy?
- files changed?
- ignores changed?
- target excluded?
- hidden?
- outside root?
- skipped by size/type/content?
- generated elsewhere?
- custom index path?

Positive hits are generally easier to trust than absence claims.

---

# 16. Search Status vs Search Result

Distinguish:

- MATCH;
- NO MATCH;
- TOOL ERROR;
- PARTIAL / UNKNOWN COVERAGE.

Do not interpret tool failure as zero results.

Do not interpret partial coverage as repository-wide absence.

---

# 17. Negative Result Protocol

If an important query returns nothing:

1. confirm spelling;
2. try naming variants;
3. search related concepts;
4. search filenames;
5. inspect likely directories;
6. verify root;
7. check ignores/hidden rules;
8. verify index status;
9. use independent text search;
10. use semantic/symbol search;
11. inspect generated/configured sources;
12. inspect history if rename/removal plausible.

Only then make strong absence claim.

---

# 18. Negative Claim Confidence

Classify:

## Low confidence
One search returned no matches.

## Moderate confidence
Several lexical variants and likely locations checked.

## High confidence
Independent lexical + semantic/config/build evidence supports absence.

Use stronger confidence only when warranted.

---

# 19. Search Result Triage

Classify candidate results:

- definition;
- direct runtime use;
- indirect use;
- config;
- test;
- generated;
- documentation;
- example;
- legacy;
- dead candidate;
- unrelated same-name.

Not all matches deserve context.

---

# 20. Definition Confirmation

Raw text cannot reliably distinguish declaration/reference in every language.

After finding symbol:

- confirm real definition;
- resolve namespace/module;
- inspect imports;
- distinguish overloads;
- distinguish same-name symbols;
- use LSP where available.

Do not perform large semantic rename from grep alone.

---

# 21. Source of Truth Identification

For any behavior, identify what actually owns it.

Potential source of truth:

- implementation;
- config;
- schema;
- generated source;
- backend;
- persisted model;
- feature flag;
- platform-specific variant.

Do not modify visible consumer if behavior is actually owned elsewhere.

---

# 22. Trace Both Directions

For important component trace:

## Upstream
Who creates/calls/triggers it?

## Downstream
What does it call/read/write/emit?

This forms impact map.

Do not trace indefinitely past task-relevant boundary.

---

# 23. Call-Chain Reconstruction

For behavior bugs/features reconstruct relevant chain.

Example:

**user action → handler → service → state/domain → persistence/network → response → UI**

Verify each edge.

If inferred, mark internal confidence accordingly until confirmed.

---

# 24. Event-Driven Systems

Search:

- event declaration;
- publisher;
- subscriber;
- registration;
- dispatcher;
- payload;
- unregistration.

A handler existing in source does not prove runtime registration.

---

# 25. Dependency Injection

For service/interface behavior search:

- contract;
- implementations;
- registration;
- lifetime;
- factory;
- direct construction;
- test replacement.

First implementation found may not be runtime implementation.

---

# 26. Routes and Endpoints

Trace relevant:

- route;
- middleware;
- handler/controller;
- validation;
- client;
- wrapper;
- base URL/config;
- tests.

When client/server coexist, inspect both sides when behavior crosses boundary.

---

# 27. UI Components

Before changing shared UI search relevant:

- component definition;
- usages;
- state source;
- handler;
- styles/tokens;
- accessibility metadata;
- platform variants;
- tests/stories/previews.

Shared component may affect many screens.

Use risk level to decide whether full usage map is necessary.

---

# 28. Configuration Tracing

For config key find relevant:

- declaration/default;
- read;
- write;
- override;
- environment variant;
- deprecated key;
- tests;
- deployment config.

Search beyond source code when configuration crosses layers.

---

# 29. Error Tracing

Search exact error first.

Trace:

- origin;
- wrapping/transformation;
- logging;
- UI presentation;
- recovery.

Do not assume visible error string is root cause.

---

# 30. Data Model Tracing

For model/entity/DTO inspect relevant:

- definition;
- construction;
- validation;
- mapping;
- serialization;
- deserialization;
- persistence;
- transport;
- UI;
- tests.

A field change may cross layers.

---

# 31. Persistence Tracing

Before storage change identify relevant:

- schema;
- migration;
- serializer;
- writer;
- reader;
- cache;
- import/export;
- compatibility tests.

One serializer rarely proves full persistence contract.

---

# 32. Feature Flags

Find:

- declaration;
- default;
- overrides;
- checks;
- tests;
- cleanup/migration.

Multiple implementations may exist behind flags.

---

# 33. Platform-Specific Code

Search:

- compile guards;
- platform folders;
- runtime OS checks;
- architecture checks;
- mobile/desktop variants.

One implementation does not prove universal behavior.

---

# 34. Generated Code

Identify whether file is generated before editing.

Find:

- generator;
- schema;
- source definition;
- manifest;
- build step.

Prefer editing source of truth over generated output.

---

# 35. Tests as Navigation

Tests reveal:

- intended usage;
- fixtures;
- setup;
- edge cases;
- public surface.

Use tests to understand expectations.

But tests are evidence, not absolute truth.

---

# 36. Version-Control Context

Use history when current code is confusing.

Questions:

- recently changed?
- compatibility guard?
- previous bug?
- migration in progress?
- renamed symbol?
- old implementation?

Do not inspect Git history for every simple lookup.

---

# 37. Search Before Delete

For deletion, increase search depth.

Check relevant:

- exact symbol/text;
- aliases;
- semantic references;
- dynamic registration;
- reflection;
- config;
- manifests;
- tests;
- build scripts;
- plugins;
- serialization.

One empty grep is insufficient for dynamic systems.

---

# 38. Search Before Rename

Before rename:

- confirm definition;
- semantic references;
- string references;
- serialization names;
- config;
- routes;
- reflection;
- tests/contracts.

Prefer language-aware rename for code symbols.

Then text-search leftovers.

---

# 39. Search Before API Change

Map:

- declaration;
- callers;
- wrappers;
- adapters;
- mocks;
- tests;
- docs/contracts;
- serialization;
- package boundaries.

Estimate regression radius before edit.

---

# 40. Search Before Refactor

Before moving/splitting shared code determine relevant:

- callers;
- shared state;
- side effects;
- events;
- DI registration;
- tests;
- platform variants.

Do not refactor from partial usage map.

---

# 41. Search Before Bug Fix

For bug:

1. observable anchor;
2. implementation path;
3. state/data trace;
4. related tests;
5. similar code;
6. history if useful;
7. hand off to QA reproduction;
8. fix;
9. search same defect pattern elsewhere.

Search supports reproduction.

It does not replace it.

---

# 42. Search Before New Code

Before creating:

- helper;
- service;
- hook;
- component;
- parser;
- utility;
- abstraction;
- API client;

search for existing equivalent.

Prevent duplicate systems caused by poor discovery.

---

# 43. Search Before Adding Dependency

Inspect:

- current dependencies;
- existing wrappers;
- standard library/framework support;
- already-bundled utility.

Do not add package for functionality already present.

---

# 44. Similar-Code Search

After confirmed defect or duplication, search for same pattern.

Examples:

- repeated wrong condition;
- copied parser;
- same transition;
- repeated workaround;
- same API handling.

Do not automatically modify all similar code.

Verify semantic equivalence first.

---

# 45. Text vs Semantic Search

Use text search for:

- strings;
- config;
- comments;
- dynamic names;
- cross-language links;
- serialized names.

Use semantic tools for:

- definitions;
- references;
- implementations;
- type relationships;
- safe rename.

Use both for important changes.

---

# 46. AST Search

Use AST when text search is ambiguous.

Good targets:

- specific call signature;
- annotations;
- declarations;
- imports;
- inheritance;
- structural anti-pattern.

Do not require AST tooling for simple exact string.

---

# 47. Query Quality

Strong query is:

- selective;
- evidence-connected;
- interpretable;
- easy to refine.

Weak query is:

- huge;
- generic;
- ambiguous;
- context-free.

If result volume is massive, refine before reading.

---

# 48. Common-Token Problem

Broad/common terms can be expensive and noisy.

Prefer:

- directory narrowing;
- file type;
- neighboring unique identifier;
- semantic tool;
- alternate engine.

Optimize information gain, not raw matches/sec.

---

# 49. Search Cost Model

Consider:

**setup cost + execution cost + result volume + interpretation cost + confidence value**

An index may have setup cost.

LSP may have startup cost.

A broad grep may have huge interpretation cost.

Choose lowest total cost preserving required confidence.

---

# 50. Context Budget

Context is limited.

Avoid:

- thousands of matches;
- full files without relevance;
- repeated rediscovery;
- giant repository dumps.

Prefer:

- counts;
- filenames;
- grouping;
- narrowed queries;
- selected snippets;
- targeted file reads.

Fast search can still waste context.

---

# 51. Search Notes

For complex tasks maintain compact internal map.

Examples:

- symbol → definition;
- symbol → callers;
- event → publishers/subscribers;
- route → handler/client;
- model → persistence/transport/UI;
- config → declaration/consumers.

Reuse reliable map while files remain unchanged.

---

# 52. Progressive Narrowing

Typical:

1. map;
2. unique anchor;
3. candidate files;
4. symbol;
5. references;
6. call chain;
7. tests;
8. config;
9. targeted reads.

Do not jump randomly across repo.

---

# 53. Progressive Expansion

When narrow search fails:

1. relax directory;
2. relax file type;
3. naming variants;
4. user-visible text;
5. related types;
6. repo-wide;
7. alternate engine;
8. history/generated sources.

Expand deliberately.

---

# 54. Machine-Readable Results

Use structured output when processing many results programmatically.

Example with tgrep:

```bash
tgrep "pattern" . --json
```

Structured results help:

- grouping;
- deduplication;
- filtering;
- follow-up automation.

Do not parse decorative terminal output when machine-readable mode exists.

---

# 55. Search Diagnostics

If indexed search behaves unexpectedly, inspect:

- server;
- index;
- watcher;
- root;
- candidate count;
- query stats;
- ignore rules.

Diagnose before guessing.

---

# 56. Ignore Rules

Search tools may skip:

- ignored dirs;
- hidden paths;
- binaries;
- explicit exclusions.

Disable/bypass ignore only when target requires it.

Do not search ignored files by default.

---

# 57. Hidden / Binary / Large Files

If task concerns:

- bundle;
- archive;
- database;
- binary;
- embedded resource;
- compiled artifact;

use appropriate inspection tool.

Do not infer coverage from text search.

---

# 58. Multi-Repository Workspaces

When product spans repos:

- identify boundaries;
- search relevant repo intentionally;
- trace shared contracts;
- distinguish client/server/shared packages.

No match in one repo does not mean absence from product.

---

# 59. Monorepo Strategy

For monorepo:

1. identify likely package;
2. search local package;
3. search shared dependencies;
4. expand repo-wide only if relationship unclear;
5. use indexed global search for repeated exploration.

Avoid repo-wide search for every trivial symbol.

---

# 60. Tool Failure Is Not Repository Evidence

If tool fails because:

- executable missing;
- server unavailable;
- bad regex;
- permission;
- stale/corrupt index;
- wrong path;

switch/fix tool.

Never turn tool failure into “not found”.

---

# 61. Differential Search

When indexed correctness matters, compare with independent engine.

Conceptually:

```bash
tgrep "UniqueSymbol" .
rg "UniqueSymbol" .
```

If they disagree, investigate:

- root;
- ignores;
- hidden;
- freshness;
- file type;
- tool semantics.

Do not choose whichever result supports theory.

---

# 62. Independent Verification Rule

For high-impact conclusions such as:

- no callers;
- unused file;
- setting never read;
- code path dead;
- safe rename;
- no stale references;

use two suitable evidence methods when practical.

Examples:

- indexed search + LSP;
- indexed search + rg;
- LSP + build;
- AST + tests;
- text search + runtime trace.

---

# 63. Dynamic Reference Awareness

Static search can miss:

- reflection;
- string lookup;
- DI by name;
- plugins;
- serialization;
- routes;
- command IDs;
- native bindings;
- templates;
- scripts;
- generated registries.

When these mechanisms exist, widen method set.

---

# 64. Dead-Code Search

Dead-code conclusion should combine relevant:

- text search;
- semantic references;
- dynamic registration knowledge;
- build;
- tests;
- runtime;
- framework conventions.

Grep alone cannot prove dead code in dynamic systems.

---

# 65. Regression Radius Search

After editing shared behavior map:

- callers;
- consumers;
- tests;
- platform variants;
- serialized/configured names;
- shared contracts.

Use this map to choose QA scope.

---

# 66. Post-Edit Search

After rename/refactor/removal search relevant:

- old symbol;
- old string;
- deprecated key;
- old path;
- stale imports;
- duplicate implementation.

Then use semantic/build/test evidence.

Build alone may miss string/config references.

---

# 67. Search Cache Discipline

Reuse prior search findings only while assumptions remain valid.

Re-search when:

- files changed;
- scope expanded;
- index uncertain;
- earlier result incomplete;
- independent verification required.

Do not blindly repeat identical searches.

---

# 68. Freshness After Edits

If indexed server/watch mode is active, verify new edits are visible before relying on no-match claims.

A post-edit stale index can create false confidence.

When uncertain, confirm with non-indexed engine.

---

# 69. Search Completeness Levels

Use explicit internal status.

## Candidate Found
Plausible location found.

## Definition Confirmed
Source of truth identified.

## Usage Map Built
Important callers/consumers mapped.

## Cross-Layer Trace Confirmed
Relevant multi-layer behavior traced.

## High-Confidence Complete
Independent methods support no important missing path.

Do not call Candidate Found complete.

---

# 70. Evidence Labels

For search conclusions classify:

- VERIFIED;
- STRONGLY SUPPORTED;
- PARTIAL;
- INFERRED;
- UNKNOWN.

Especially useful for:

- dynamic code;
- generated code;
- incomplete tool availability;
- absence claims.

---

# 71. Search Before Planning

Before planning major change in existing codebase inspect:

- current implementation;
- analogous patterns;
- shared components;
- tests;
- architecture conventions.

Do not invent architecture from user description if repository can answer.

---

# 72. Existing Convention Search

Find one or two analogous features.

Learn relevant:

- naming;
- placement;
- state;
- error handling;
- logging;
- testing;
- DI;
- UI components.

Follow good existing conventions unless evidence shows they are defective.

---

# 73. TODO / FIXME / HACK

These are leads, not proof.

Do not assume:

- every TODO is important;
- every HACK is wrong;
- no TODO means no debt.

Investigate context.

---

# 74. Suppression Search

During quality review, search relevant:

- skipped tests;
- disabled warnings;
- empty catches;
- broad suppressions;
- ignored errors.

Interpret in language/framework context.

Do not mechanically flag all occurrences.

---

# 75. Sensitive Search Output

Search may expose:

- keys;
- tokens;
- credentials;
- private endpoints;
- personal data.

Do not unnecessarily copy values.

Report location/type/remediation and redact secret content.

---

# 76. Security-Sensitive Searches

Search for defensive review only within legitimate codebase scope.

Examples:

- secret leakage;
- unsafe debug config;
- permission checks;
- exposed admin paths.

Do not turn codebase navigation into instructions for attacking external systems.

---

# 77. Search Hand-Off to QA

When bug investigation reaches runnable behavior:

hand off:

- observable anchor;
- suspected path;
- relevant state;
- likely affected modules;
- tests.

QA then reproduces/isolates.

Search does not prove runtime bug by itself.

---

# 78. Search Hand-Off to Refactoring

Before refactor provide:

- source of truth;
- usage map;
- dynamic references;
- regression radius;
- tests;
- uncertainty.

Never refactor from partial usage map when change is high impact.

---

# 79. Search Hand-Off to Release

For release review search relevant:

- localhost/dev endpoints;
- test credentials;
- mock services;
- dev flags;
- stale versions;
- temp paths;
- demo data;
- disabled checks.

Release skill must verify findings against exact artifact/config.

---

# 80. Search Hand-Off to Design / Product

For UI/product work provide:

- actual component location;
- shared usage;
- state/data source;
- existing patterns;
- relevant tests.

Do not let design agent recreate functionality already present because search was incomplete.

---

# 81. Search Performance Claims

Do not claim fixed universal speedups.

Search performance varies with:

- repo size;
- platform;
- query selectivity;
- match volume;
- index setup;
- filesystem/cache.

Measure actual workflow when speed matters.

---

# 82. Long Agent Sessions

For repeated large-repo search:

1. confirm root;
2. establish suitable index if useful;
3. verify server/watch health;
4. run selective queries;
5. maintain compact map;
6. re-check freshness after edits;
7. avoid duplicate infrastructure.

Use server mode as optimization, not ritual.

---

# 83. Index Lifecycle

Treat indexes as generated search infrastructure.

Do not:

- manually edit;
- treat as product source;
- commit unless project convention requires it.

Respect repo cache/generated policy.

---

# 84. Search Exit Condition

Stop searching when evidence required by task is satisfied.

Examples:

## Tiny edit
definition found + local context understood.

## Rename
definition + references + dynamic/string leftovers mapped.

## Bug
relevant execution path identified enough for reproduction.

## Delete
high-confidence absence/use map completed.

## Architecture change
cross-layer dependencies understood.

Do not continue simply because more search tools are available.

---

# 85. No Over-Search Rule

Search has diminishing returns.

Stop when additional query is unlikely to materially change:

- implementation plan;
- regression scope;
- correctness conclusion;
- risk assessment.

Do not spend ten searches proving a local private variable has one use.

---

# 86. Search Report

For substantial tasks, report compactly:

## Source of Truth
Where main implementation lives.

## Relevant Usages
Important callers/consumers.

## Cross-Layer Dependencies
Only relevant ones.

## Dynamic / Config References
If applicable.

## Regression Radius
What may be affected.

## Confidence
Definition / Usage Map / Cross-Layer / High-Confidence Complete.

## Remaining Uncertainty
Only meaningful unknowns.

Do not dump every search match.

---

# 87. No Numeric Search Score

Do not use self-assigned 0–5 quality scores as evidence.

Use actual evidence and completeness status.

A “80/80 search” can still be wrong if root/index/dynamic paths were misunderstood.

---

# 88. Agent Execution Protocol

## Phase 1 — Classify
Identify target and risk.

## Phase 2 — Set Depth
Choose Level 0–4.

## Phase 3 — Root
Confirm repository/workspace scope.

## Phase 4 — Map
Create minimal relevant repo map.

## Phase 5 — Anchor
Find exact observable or semantic anchor.

## Phase 6 — Search
Use best first tool.

## Phase 7 — Triage
Separate definition/usage/test/config/generated.

## Phase 8 — Confirm
Identify source of truth.

## Phase 9 — Trace
Upstream/downstream as required.

## Phase 10 — Expand
Only if evidence incomplete.

## Phase 11 — Verify Negatives
Use independent method for important absence claims.

## Phase 12 — Build Impact Map
Map regression radius.

## Phase 13 — Hand Off / Change
Provide findings to specialist or implementation.

## Phase 14 — Post-Edit Search
Find stale references/old names.

## Phase 15 — Build/Test
Use semantic/compiler/QA evidence where relevant.

## Phase 16 — Stop
When task-required confidence reached.

---

# 89. Integration with Orchestrator

Agent Orchestrator owns:

- whether this skill activates;
- overall task scope;
- verification budget;
- specialist sequence;
- completion strategy.

Search skill owns:

- retrieval strategy;
- codebase mapping;
- source-of-truth identification;
- dependency/usage tracing;
- search-confidence assessment.

Do not duplicate orchestration.

---

# 90. Integration with QA

QA owns runtime defect evidence.

Search owns:

- path discovery;
- related implementations;
- changed-code impact;
- tests/config discovery.

Search can support a bug hypothesis.

QA confirms behavior.

---

# 91. Integration with Refactoring

Refactoring owns whether structural change is justified.

Search owns:

- definitions;
- callers;
- dynamic references;
- contracts;
- regression radius.

Do not allow refactor based on incomplete high-impact map.

---

# 92. Integration with Release

Release owns final ship/no-ship decision.

Search supports:

- release config discovery;
- version string discovery;
- dev artifact detection;
- stale flags;
- secret locations.

Search result must still be verified against actual candidate.

---

# 93. Skill Evaluation Hooks

Evaluate paired repository tasks.

## Baseline
Same task/model/repo/tools without skill.

## Skill run
Same setup with skill.

Compare:

- correct source-of-truth discovery;
- caller/reference recall;
- false absence claims;
- dead-code mistakes;
- rename completeness;
- dynamic reference misses;
- regression-radius accuracy;
- irrelevant files opened;
- context tokens;
- search/tool calls;
- completion time.

Important negative metrics:

- one match mistaken as whole implementation;
- stale index trusted;
- tool failure treated as no match;
- giant result dumps;
- unnecessary Level 4 search on tiny task;
- grep-only semantic rename;
- generated file edited instead of source.

A useful search skill improves both confidence and efficiency.

---

# 94. Decision Rules

When choosing between:

- text vs semantic → use method matching question;
- tgrep vs rg → choose lower total task cost;
- one match vs source of truth → confirm;
- no match vs absence → verify;
- broad search vs exact anchor → exact first;
- context volume vs selectivity → selectivity;
- speed vs confidence → required confidence;
- full repo trace vs local evidence → task-risk depth;
- search more vs diminishing value → stop;
- tool result vs runtime truth → runtime for behavior.

---

# 95. Final Principle

Search fast.
Read selectively.
Confirm source of truth.
Trace only as deep as risk requires.
Treat absence claims skeptically.
Use independent evidence for high-impact conclusions.
Do not confuse retrieval with understanding.
Do not confuse more context with more certainty.

The best codebase navigator is not the one that searches the most.

It is the one that reaches the correct implementation and impact map with the least unnecessary work.
