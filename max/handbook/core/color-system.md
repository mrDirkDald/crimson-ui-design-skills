# Color System

## Color is semantic infrastructure

Choose palette after understanding product subject, environment, audience, and repeated task frequency.

## Dominance

Most production UI should have one dominant accent family. Supporting colors either create identity, category distinction, or semantic states. If every control receives a different vivid color, hierarchy collapses.

## Semantic tokens

Separate raw palette from semantic role. Example:

```text
palette.blue.500 → action.primary.bg
palette.blue.600 → action.primary.hover
palette.slate.900 → text.primary
```

Components should consume semantic tokens where possible.

## Theme parity

Light and dark themes should feel like the same product, not inverse screenshots. Preserve semantic hierarchy while adjusting luminance, chroma, surface separation, and contrast.

## Grayscale test

If every important region collapses when desaturated, the design relies too heavily on hue. Hierarchy should still exist through lightness, weight, position, and shape.

## Saturation budget

Reserve the strongest saturation for the highest-value action or identity moment. Status colors should not overpower normal workflow unless urgency is the message.

## Catalogs

Use the existing `references/color-pairs.md`, `references/color-trios.md`, and `references/color-palettes-4plus.md` for concrete recipes. Adapt them rather than copying blindly.
