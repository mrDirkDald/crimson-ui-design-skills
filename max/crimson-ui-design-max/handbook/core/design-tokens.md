# Design Tokens

## Layers

A robust token architecture often separates:

```text
primitive palette / raw scales
→ semantic tokens
→ component tokens (only where necessary)
```

## Examples

Raw `blue-600` should not directly mean “primary button” everywhere. A semantic `action-primary-bg` can point to a raw color and change by theme.

## Spacing

Centralize a small useful scale but allow exceptional values when the visual system genuinely needs them.

## Radius

Too many nearly identical radii create drift. Define a purposeful family.

## Theme

Theme tokens should cover text, surfaces, borders, interaction, focus, selection, and status—not only background colors.
