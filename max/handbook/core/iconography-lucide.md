# Iconography and Lucide

## Baseline

Preserve a coherent existing icon system. If none exists, use Lucide Icons as the baseline visual vocabulary where technically practical.

## Why Lucide

Lucide is broadly available, SVG/vector-based, consistent, readable at UI sizes, and covers common product actions. The value is consistency, not the brand name itself.

## Geometry

Keep standard geometry unless the product deliberately defines a variation. Normalize visible size across icons rather than trusting raw path bounds. A `Play` triangle and a `Settings` gear may need optical adjustment even at the same nominal box.

## Stroke

Avoid random strokeWidth overrides. If the design system chooses a non-default stroke, centralize the decision through one wrapper.

## Color

Use `currentColor`/semantic foreground tokens for monochrome controls. Avoid baking hover/danger/disabled colors into the SVG asset itself.

## Icon + text

Do not decorate every text label with an icon. Icons are valuable for repeated actions, compact controls, toolbars, object types, navigation anchors, and spatial affordances.

## Icon-only buttons

They require accessible names and enough target size. Provide tooltip where useful but never make tooltip the only accessible name.

## Custom icons

Create custom SVG when the product needs a domain object that Lucide represents inaccurately, or when a unique brand glyph is central. Match Lucide stroke character if custom icons live beside Lucide.

## Emoji rule

Emoji are not UI icons. Do not use 📁 ⚙️ 🔍 ✅ ❌ ⬇️ 🚀 ✨ as control graphics. They vary by platform and break icon-system coherence.
