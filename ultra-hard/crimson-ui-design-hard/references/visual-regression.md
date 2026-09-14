# Visual Regression & Runtime Matrix

## Contents
- Purpose/evidence
- Before/after protocol
- Cross-browser matrix
- Desktop runtime matrix
- Screenshot regression
- Visual diff tolerance
- Component regression
- Nondeterminism control
- Artifact contract

## Purpose

Use this module when visual regression, cross-browser/platform parity, or stable component/screen baselines materially matter.
Do not load it for every tiny UI edit.

## Before/after protocol

For regression-sensitive changes prefer:
- BEFORE artifact;
- AFTER artifact;
- same viewport/window;
- same theme/locale/state/data;
- same font/runtime environment when practical.

Record intentional differences separately from unexpected diffs.

## Cross-browser matrix

For browser products choose a risk-based matrix.
When broad support is expected, normally include Chromium-family, Firefox and Safari/WebKit where product/platform requires it.

Record exact browser/version when available.
Prioritize layout/reflow, focus, forms, sticky/fixed positioning, dialogs/popovers, scrollbars, font rendering, media and input behavior.

One-browser PASS is not cross-browser PASS.

## Desktop runtime matrix

For native/Electron/Tauri choose supported OS targets such as Windows, macOS, Linux.
Record OS/version, DPI/scaling, window size, theme and input method.
If required targets are unavailable, mark them BLOCKED/NOT REVIEWED.

## Automated screenshot regression

For stable, visually important surfaces use screenshot regression when tooling exists.
Pin:
- viewport/window;
- theme;
- locale;
- deterministic data/state;
- font/environment when practical;
- animation disabled/frozen when practical.

Compare baseline, candidate and diff artifact.
Screenshot regression complements interaction/accessibility QA; it does not replace them.

## Visual diff tolerance

Do not use one universal pixel threshold.
Classify diffs:
- expected deterministic change;
- benign rendering noise;
- suspicious regression;
- blocking regression.

If numeric threshold is used:
- calibrate to environment/component;
- mask/freeze known nondeterministic areas;
- inspect semantic/structural impact.

Low pixel diff can hide serious regression; high diff can be correct after intentional redesign.

## Component regression

For stable shared components, capture relevant isolated states: default, hover, focus, pressed, selected, disabled, loading, error, long-content and supported theme/contrast modes.

Component snapshots should pin deterministic content/container/theme/locale/font environment when practical.
Use component regression alongside behavior contract tests.

## Nondeterminism control

Before trusting screenshot diffs control or record:
- timestamps/random IDs;
- async loading;
- animation;
- caret/blink;
- font availability;
- network images;
- GPU/font antialiasing differences.

Do not hide real regressions behind broad masks.

## Artifact contract

A regression run should produce when tooling allows:
```text
runtime.json
before.png
candidate.png
diff.png
check-results.json
notes.md
```

Artifacts must identify benchmark/task, environment and state.
