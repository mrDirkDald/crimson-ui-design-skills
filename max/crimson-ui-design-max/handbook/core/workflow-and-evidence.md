# Workflow and Evidence

## Why this exists

UI work fails when the agent jumps from a screenshot or a component name directly to styling. The correct process is to identify the real target surface, the real governing code, the user's actual acceptance criteria, and the state transitions that matter before changing appearance.

## Repository reconnaissance

Inspect the project shape before editing. Determine entry points, routes/windows/screens, component hierarchy, styling system, theme/token source, assets, state/store layer, API/data sources, tests, build scripts, and platform shell. Do not read unrelated modules merely because they are nearby.

Create a trace:

```text
USER SURFACE
→ route/window/screen
→ top-level component/view
→ child components
→ styling/token sources
→ state/data sources
→ platform shell/integration
```

For a web page, verify which stylesheet or utility classes actually win in the cascade. For WPF/WinUI/Avalonia, trace ResourceDictionary/ThemeResource/Style application. For Qt/QML, trace component imports, properties, palette/theme objects, and style. For SwiftUI/Compose/Flutter, trace environment/theme providers and modifiers. For immediate-mode UI, trace the render function and shared style constants.

## Evidence-backed diagnosis

Separate observation from interpretation.

```text
OBSERVATION: primary button, copy button and navigation login all use equally saturated accent fills.
INTERPRETATION: action hierarchy is ambiguous.
IMPACT: user cannot immediately identify the next action.
ROOT CAUSE: accent tokens are not semantically separated.
FIX LEVEL: token/component system, not one local button.
```

Do not call a design “bad” because it differs from personal taste. Tie criticism to hierarchy, comprehension, task completion, consistency, accessibility, platform fit, or product identity.

## Before/after equivalence

When comparing visual changes, keep state and viewport equivalent where possible. A new screenshot at a different content state cannot reliably prove improvement.

## Runtime limitations

If the app cannot run, mark appearance/interaction conclusions as limited. Static source can establish architecture and likely styling but cannot prove exact rendering, focus order, animation timing, pixel clipping, hover behavior, or OS-specific details.
