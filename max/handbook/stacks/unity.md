# Unity C# UI Toolkit / uGUI

## Implementation lens

Use scalable canvases/panels, layout systems, input-system navigation, focus/gamepad states, safe areas, localization, and performance. Prefer UI Toolkit for maintainable editor/runtime interfaces when suitable; understand uGUI anchoring when used.

## Design-system mapping

Map the shared design concepts into the toolkit's real primitives: semantic color roles, typography roles, spacing, radius, component states, focus, disabled, selection, error, loading, and theme. Do not copy CSS concepts literally into a toolkit that has different architecture.

## Layout

Prefer the toolkit's responsive/constraint/layout system over hardcoded coordinates. Use fixed positioning only for genuinely spatial or overlay content.

## Iconography

Preserve an existing coherent vector icon system. Otherwise use Lucide when a maintained implementation exists, or compatible SVG/vector assets. Do not use emoji as controls.

## Accessibility

Use the toolkit's semantic/accessibility APIs, not visual labels alone. Verify keyboard/focus or platform input where relevant.

## Verification

Build/run the actual target. Check at least default, interaction/focus, long-content, error/empty/loading where applicable, and a second size/theme when supported.

## Detailed implementation checklist

When implementing a design in this toolkit, do not treat visual work as a one-file skin change. Trace the complete view path and verify how the toolkit represents state, layout, styling, input, accessibility, and lifecycle. Identify which layer owns each decision before editing. A local component should not override a shared token merely because it is faster to type. A shared token should not be changed globally when the problem belongs only to one semantic role.

### Structure and ownership

Map the screen or window into primary regions, reusable components, local state, shared state, and platform shell. Keep business/domain behavior separate from purely visual concerns where the architecture allows it. Reuse existing components when their behavior and semantics are sound; do not preserve a visually broken component contract just because it already exists. If the same visual fix is repeated at several call sites, look for a governing style, theme, component, or token layer.

### Tokens and theming

Define semantic roles for background, surfaces, primary/secondary text, borders, primary action, selection, focus, success, warning, danger, and informational states. Map those roles to the toolkit's real theme mechanism. Test the alternate theme when the product supports one. Do not implement dark mode as mechanical inversion. Ensure disabled, hover, selected, and focus states remain distinguishable in every supported theme.

### Layout and scaling

Prefer the toolkit's intended layout system over manual coordinates. Test narrow and wide states, long labels, dynamic content, font scaling, DPI/device scale, and empty/overflow states. Fixed sizes are acceptable for genuinely fixed visual primitives such as icon glyph boxes, but should not lock whole screens to one machine or language.

### Interaction and state

Every important control should have a clear default, focus, pressed/active, disabled, and loading/error state when applicable. Repeated actions must remain stable in placement unless context changes the action itself. Avoid visual-only state that is not connected to the real state model. Do not leave mock controls or click handlers that do nothing.

### Icons

Preserve an existing coherent vector icon system. Otherwise use Lucide or Lucide-compatible SVG/vector assets when technically practical. Use one semantic glyph for the same action across the product. Keep icon sizing and stroke treatment coherent. Emoji are content, not an icon library. Icon-only controls need an accessible name even when a tooltip is present.

### Accessibility

Use the toolkit's semantic/accessibility APIs instead of painting a control that only looks correct. Verify focus order, visible focus, labels, states, keyboard or platform navigation, text scaling, contrast, and non-color cues. When the toolkit has accessibility limitations, document the limitation rather than pretending the visual design alone solves it.

### Performance

Avoid expensive effects that do not materially improve hierarchy or product identity. Watch large media decoding, continuous animation, layout thrashing, overdraw, excessive widget/view count, unnecessary re-renders, and unbounded lists. If the product is a repeated-use utility, responsiveness usually matters more than decorative spectacle.

### Verification

Run the real target. Inspect the happy path and at least one non-happy state. Resize or rotate where relevant. Test keyboard/touch/controller according to the platform. Verify theme and scaling. Run the project's normal build, type, lint, unit, snapshot, or UI checks when available. Record anything that could not be run as BLOCKED or NOT REVIEWED rather than PASS.

### Common failure modes

- copying web CSS assumptions into a native toolkit without mapping them to real primitives;
- hardcoding local colors instead of semantic theme roles;
- absolute positioning that breaks on text expansion or DPI changes;
- replacing native behavior with fake painted controls;
- mixing icon families or falling back to emoji;
- polishing only the default state;
- creating a generic card dashboard regardless of product workflow;
- refactoring unrelated logic during a visual change;
- claiming success without running the actual target.

