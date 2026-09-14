# Master Exhaustive Checklist

This checklist is intentionally redundant. Use the relevant parts; MAX edition prioritizes completeness over brevity.

## Product understanding
- [ ] primary user: inspect, verify, and record evidence rather than assuming.
- [ ] primary job: inspect, verify, and record evidence rather than assuming.
- [ ] frequency: inspect, verify, and record evidence rather than assuming.
- [ ] environment: inspect, verify, and record evidence rather than assuming.
- [ ] constraints: inspect, verify, and record evidence rather than assuming.
- [ ] real data: inspect, verify, and record evidence rather than assuming.
- [ ] success criteria: inspect, verify, and record evidence rather than assuming.

## Hierarchy
- [ ] first anchor: inspect, verify, and record evidence rather than assuming.
- [ ] primary action: inspect, verify, and record evidence rather than assuming.
- [ ] primary content: inspect, verify, and record evidence rather than assuming.
- [ ] state visibility: inspect, verify, and record evidence rather than assuming.
- [ ] secondary controls: inspect, verify, and record evidence rather than assuming.
- [ ] metadata: inspect, verify, and record evidence rather than assuming.

## Layout
- [ ] alignment: inspect, verify, and record evidence rather than assuming.
- [ ] grid/constraints: inspect, verify, and record evidence rather than assuming.
- [ ] density: inspect, verify, and record evidence rather than assuming.
- [ ] scroll ownership: inspect, verify, and record evidence rather than assuming.
- [ ] empty space: inspect, verify, and record evidence rather than assuming.
- [ ] viewport use: inspect, verify, and record evidence rather than assuming.

## Typography
- [ ] roles: inspect, verify, and record evidence rather than assuming.
- [ ] line height: inspect, verify, and record evidence rather than assuming.
- [ ] line length: inspect, verify, and record evidence rather than assuming.
- [ ] weights: inspect, verify, and record evidence rather than assuming.
- [ ] numeric alignment: inspect, verify, and record evidence rather than assuming.
- [ ] fallback fonts: inspect, verify, and record evidence rather than assuming.

## Color
- [ ] semantic roles: inspect, verify, and record evidence rather than assuming.
- [ ] dominance: inspect, verify, and record evidence rather than assuming.
- [ ] contrast: inspect, verify, and record evidence rather than assuming.
- [ ] theme parity: inspect, verify, and record evidence rather than assuming.
- [ ] grayscale: inspect, verify, and record evidence rather than assuming.
- [ ] color-blind safety: inspect, verify, and record evidence rather than assuming.

## Icons
- [ ] Lucide/existing system: inspect, verify, and record evidence rather than assuming.
- [ ] SVG/vector: inspect, verify, and record evidence rather than assuming.
- [ ] optical size: inspect, verify, and record evidence rather than assuming.
- [ ] stroke: inspect, verify, and record evidence rather than assuming.
- [ ] accessible name: inspect, verify, and record evidence rather than assuming.
- [ ] no emoji controls: inspect, verify, and record evidence rather than assuming.

## States
- [ ] default: inspect, verify, and record evidence rather than assuming.
- [ ] hover: inspect, verify, and record evidence rather than assuming.
- [ ] focus: inspect, verify, and record evidence rather than assuming.
- [ ] pressed: inspect, verify, and record evidence rather than assuming.
- [ ] selected: inspect, verify, and record evidence rather than assuming.
- [ ] disabled: inspect, verify, and record evidence rather than assuming.
- [ ] loading: inspect, verify, and record evidence rather than assuming.
- [ ] success: inspect, verify, and record evidence rather than assuming.
- [ ] warning: inspect, verify, and record evidence rather than assuming.
- [ ] error: inspect, verify, and record evidence rather than assuming.
- [ ] empty: inspect, verify, and record evidence rather than assuming.
- [ ] offline: inspect, verify, and record evidence rather than assuming.

## Navigation
- [ ] orientation: inspect, verify, and record evidence rather than assuming.
- [ ] back/up: inspect, verify, and record evidence rather than assuming.
- [ ] deep links: inspect, verify, and record evidence rather than assuming.
- [ ] history: inspect, verify, and record evidence rather than assuming.
- [ ] current location: inspect, verify, and record evidence rather than assuming.
- [ ] context actions: inspect, verify, and record evidence rather than assuming.

## Forms
- [ ] labels: inspect, verify, and record evidence rather than assuming.
- [ ] validation timing: inspect, verify, and record evidence rather than assuming.
- [ ] preserve input: inspect, verify, and record evidence rather than assuming.
- [ ] errors: inspect, verify, and record evidence rather than assuming.
- [ ] submit state: inspect, verify, and record evidence rather than assuming.
- [ ] dependencies: inspect, verify, and record evidence rather than assuming.
- [ ] unsaved state: inspect, verify, and record evidence rather than assuming.

## Responsive
- [ ] wide: inspect, verify, and record evidence rather than assuming.
- [ ] normal: inspect, verify, and record evidence rather than assuming.
- [ ] narrow: inspect, verify, and record evidence rather than assuming.
- [ ] mobile: inspect, verify, and record evidence rather than assuming.
- [ ] large text: inspect, verify, and record evidence rather than assuming.
- [ ] orientation: inspect, verify, and record evidence rather than assuming.
- [ ] split view: inspect, verify, and record evidence rather than assuming.

## Accessibility
- [ ] semantics: inspect, verify, and record evidence rather than assuming.
- [ ] keyboard: inspect, verify, and record evidence rather than assuming.
- [ ] screen reader: inspect, verify, and record evidence rather than assuming.
- [ ] focus: inspect, verify, and record evidence rather than assuming.
- [ ] target size: inspect, verify, and record evidence rather than assuming.
- [ ] contrast: inspect, verify, and record evidence rather than assuming.
- [ ] reduced motion: inspect, verify, and record evidence rather than assuming.
- [ ] non-color cues: inspect, verify, and record evidence rather than assuming.

## Performance
- [ ] images: inspect, verify, and record evidence rather than assuming.
- [ ] fonts: inspect, verify, and record evidence rather than assuming.
- [ ] effects: inspect, verify, and record evidence rather than assuming.
- [ ] lists: inspect, verify, and record evidence rather than assuming.
- [ ] layout: inspect, verify, and record evidence rather than assuming.
- [ ] animation: inspect, verify, and record evidence rather than assuming.
- [ ] network: inspect, verify, and record evidence rather than assuming.
- [ ] startup: inspect, verify, and record evidence rather than assuming.

## Localization
- [ ] expansion: inspect, verify, and record evidence rather than assuming.
- [ ] RTL: inspect, verify, and record evidence rather than assuming.
- [ ] numbers: inspect, verify, and record evidence rather than assuming.
- [ ] dates: inspect, verify, and record evidence rather than assuming.
- [ ] pluralization: inspect, verify, and record evidence rather than assuming.
- [ ] font coverage: inspect, verify, and record evidence rather than assuming.
- [ ] mixed direction: inspect, verify, and record evidence rather than assuming.

## Quality
- [ ] build: inspect, verify, and record evidence rather than assuming.
- [ ] typecheck: inspect, verify, and record evidence rather than assuming.
- [ ] lint: inspect, verify, and record evidence rather than assuming.
- [ ] tests: inspect, verify, and record evidence rather than assuming.
- [ ] runtime screenshot: inspect, verify, and record evidence rather than assuming.
- [ ] non-happy state: inspect, verify, and record evidence rather than assuming.
- [ ] stop condition: inspect, verify, and record evidence rather than assuming.


## HARD expansion — evidence and implementation protocol

Before changing this area, record the actual product behavior, governing components/styles, user frequency, platform conventions, and failure/recovery states. Distinguish a visual preference from an observable usability or coherence problem.

### Decision procedure

1. Identify the user job and current state.
2. Identify what information/action must be recognized first.
3. Trace the code/style/state owner that actually governs the surface.
4. Separate structural, visual, interaction, accessibility, and content issues.
5. Choose the smallest coherent change unless several governing layers are failing together.
6. Implement with the real toolkit rather than screenshot-specific hacks.
7. Verify normal, edge, loading, error, disabled, keyboard/focus, scaling/responsive, and recovery states where relevant.
8. Report observed evidence and remaining unknowns.

### Cross-cutting constraints

- Preserve working behavior and useful platform conventions.
- Do not hide critical state behind color, hover, animation, or decorative media alone.
- Do not introduce generic cards/containers unless they represent a real semantic/interaction boundary.
- Keep product-specific objects and workflow visually stronger than support chrome.
- Respect localization expansion, high-DPI/text scaling, reduced motion, and assistive technology where applicable.
- Avoid unrelated refactors and dependency churn.
- Do not claim PASS for behavior that was not run or observed.

### Runtime checklist

- [ ] Primary job remains discoverable.
- [ ] Primary and destructive actions are distinguishable.
- [ ] Empty/loading/error/disabled/recovery behavior is intentional.
- [ ] Focus/keyboard/input behavior is preserved.
- [ ] Overflow and scaling are handled.
- [ ] Theme and semantic color behavior remain coherent.
- [ ] No fake content, proof, metric, control, or success state was introduced.
- [ ] The rendered result was inspected when the environment permits it.
