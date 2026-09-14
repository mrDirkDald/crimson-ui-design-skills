# Typography

## Typography is architecture

Type communicates hierarchy, density, voice, and scanning order before users read words.

## Role system

Define named roles instead of ad-hoc font sizes. Example:

```text
Display / Brand
Hero / Page Title
Section Title
Subsection Title
Body Strong
Body
Control Label
Metadata
Caption
Code / Monospace
Numeric / Tabular
```

Each role should define family, size, line-height, weight, tracking if needed, and typical context.

## Display typography

Large display type should earn its space. Marketing, editorial, cultural, and expressive work can support extreme scale. Repeated-use utilities, settings, file managers, and dense editors rarely benefit from giant headings consuming the working viewport.

## Line length

Body copy needs readable measure. Do not stretch paragraphs across ultrawide containers. Dense metadata and technical tables may legitimately use shorter or more compact text.

## Numeric alignment

Use tabular numerals for changing metrics, timers, finance, or aligned tables when supported. Preserve unit hierarchy.

## Font loading

On web, avoid blocking or unstable font behavior. On native platforms, prefer system typography unless brand type materially improves identity and is technically safe. Provide fallback stacks.
