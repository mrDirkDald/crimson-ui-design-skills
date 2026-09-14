# Color Palettes — 4+ Color Harmony Recipes

## Contents
- Purpose
- Multi-color architecture
- Curated 4-Color Palettes
- Curated 5-Color Palettes
- Curated 6-Color Palettes
- Sequential Data Palette
- Diverging Data Palette
- Categorical data rules
- 4+ color role strategies
- Light theme
- Dark theme
- Color-blind / accessibility safety
- Multi-color selection algorithm
- AI-generated rainbow guard

## Purpose

Use when a product genuinely needs **four or more principal chromatic colors**.

Common reasons:
- rich brand systems;
- entertainment/media;
- games and launchers;
- festivals/cultural products;
- data visualization;
- category coding;
- illustration-led identity.

Most utilities and productivity apps do not need 4+ chromatic families. If removing a color does not hurt meaning or identity, remove it.

## Do not confuse hue families with tonal variants

A UI may contain many hex values but still have only one brand hue family.

Example:

```text
blue accent
blue hover
blue pressed
blue tint
green success
yellow warning
red danger
```

This is not a six-color brand palette.

## Multi-color architecture

Assign roles first:

```text
DOMINANT:
SUPPORT-1:
SUPPORT-2:
ACCENT:
SEMANTIC:
NEUTRALS:
```

or:

```text
BRAND:
CATEGORY-A:
CATEGORY-B:
CATEGORY-C:
HIGHLIGHT:
NEUTRALS:
```

Do not distribute all colors evenly.

# Curated 4-Color Palettes

## 01 — Technical Signal
- `#0F172A` Navy
- `#1D4ED8` Blue
- `#06B6D4` Cyan
- `#F59E0B` Amber

Navy = structure, blue = primary action, cyan = information/live state, amber = rare emphasis.

## 02 — Deep Ocean
- `#082F49`
- `#0E7490`
- `#38BDF8`
- `#A3E635`

Use lime sparingly.

## 03 — Forest Workshop
- `#1B4332`
- `#52796F`
- `#DDA15E`
- `#E76F51`

Outdoor, craft, sustainability.

## 04 — Editorial Earth
- `#432818`
- `#99582A`
- `#DDA15E`
- `#6B7F82`

Muted, mature, architectural/editorial.

## 05 — Digital Studio
- `#312E81`
- `#7C3AED`
- `#DB2777`
- `#22D3EE`

Do not show all four at maximum saturation at once.

## 06 — Game Energy
- `#111827`
- `#EF4444`
- `#F59E0B`
- `#22D3EE`

If red is brand, keep semantic danger distinguishable by more than hue.

## 07 — Night Festival
- `#160F29`
- `#6D28D9`
- `#E11D48`
- `#FDE047`

Expressive/event use.

## 08 — Soft Culture
- `#4A4453`
- `#9A8C98`
- `#C9ADA7`
- `#F2E9E4`

Needs strong text contrast support.

## 09 — Modern Heritage
- `#1D3557`
- `#457B9D`
- `#E9C46A`
- `#E76F51`

Culture, travel, storytelling.

## 10 — Hospitality
- `#3D2C2E`
- `#A44A3F`
- `#D4A373`
- `#6A994E`

Warm and grounded.

## 11 — Wellness Spectrum
- `#264653`
- `#2A9D8F`
- `#E9C46A`
- `#F4A261`

Keep warm hues subordinate unless they are the chosen CTA family.

## 12 — Creative Contrast
- `#2E1065`
- `#2563EB`
- `#F43F5E`
- `#FACC15`

High-energy; requires strict dominance control.

# Curated 5-Color Palettes

## 13 — Product Spectrum
- `#172554`
- `#1D4ED8`
- `#0F766E`
- `#D97706`
- `#BE123C`

Useful for brand + support + semantic states. Do not display all state colors constantly.

## 14 — Natural Material
- `#283618`
- `#606C38`
- `#DDA15E`
- `#BC6C25`
- `#7F5539`

Outdoor, food, craft.

## 15 — Coastal Editorial
- `#003049`
- `#669BBC`
- `#FDF0D5`
- `#C1121F`
- `#780000`

Strong editorial identity.

## 16 — Contemporary Art
- `#1C1917`
- `#7C3AED`
- `#EC4899`
- `#F59E0B`
- `#14B8A6`

Ink/neutral should dominate.

## 17 — Playful Consumer
- `#2563EB`
- `#14B8A6`
- `#FACC15`
- `#FB7185`
- `#A78BFA`

Friendly/education/social. Maintain adult-level accessibility.

## 18 — Retro Digital
- `#101820`
- `#00A6A6`
- `#F2C14E`
- `#F78154`
- `#D81E5B`

Strong personality; avoid equal saturation everywhere.

# Curated 6-Color Palettes

## 19 — Data Categorical
- `#2563EB`
- `#0D9488`
- `#65A30D`
- `#D97706`
- `#DC2626`
- `#7C3AED`

For peer categories only. Do not accidentally imply semantic red/green meanings.

## 20 — Muted Data Categorical
- `#4C78A8`
- `#72B7B2`
- `#54A24B`
- `#ECA82C`
- `#E45756`
- `#B279A2`

Better for dense charts than rainbow-neon palettes.

## 21 — Media / Entertainment
- `#09090B`
- `#7C3AED`
- `#2563EB`
- `#E11D48`
- `#F97316`
- `#FACC15`

Use black/neutral as the dominant field.

## 22 — Botanical
- `#1B4332`
- `#2D6A4F`
- `#74C69D`
- `#DDA15E`
- `#BC6C25`
- `#E9EDC9`

## 23 — Luxury Warm/Cool
- `#171717`
- `#5B4636`
- `#B08968`
- `#DDB892`
- `#355070`
- `#6D597A`

A luxury option without default black/gold cliché.

## 24 — Experimental Web
- `#0A0A0A`
- `#F5F5F4`
- `#2563EB`
- `#E11D48`
- `#FACC15`
- `#10B981`

Spend chroma in one place at a time.

# Sequential Data Palette

Use one hue family with monotonic lightness/chroma.

```text
#EFF6FF
#BFDBFE
#60A5FA
#2563EB
#1E40AF
#172554
```

Do not use categorical rainbow hues for ordered magnitude.

# Diverging Data Palette

Use only when data has a meaningful center such as zero, target, neutral sentiment, or baseline.

```text
#1D4ED8
#60A5FA
#DBEAFE
#F8FAFC
#FFEDD5
#FB923C
#C2410C
```

# Categorical data rules

For many categories:
- direct-label when possible;
- use marker/line-style differences;
- highlight selected series and mute others;
- avoid 10+ equally saturated colors;
- test color-vision simulation.

For 8+ categories, consider grouping, small multiples, interactive isolation, or pattern/shape differences.

# 4+ color role strategies

### Brand + semantic/support hues
Best for product software.

### Dominant + editorial accents
Best for cultural/media products. Only one accent should dominate each section.

### Category system
Best for data/content. Each color must have stable category meaning.

### Illustration palette
Keep UI chrome restrained while illustrations/media use the richer palette. This is often better than applying every illustration color to controls.

# Light theme

- use tints for large areas;
- reserve saturated values for accents/indicators;
- keep body text neutral and readable;
- do not create a wall of pastel surfaces.

# Dark theme

- keep most chromatic families below maximum saturation;
- choose one brightest accent;
- lower chroma of secondary colors;
- avoid neon halo effects;
- preserve semantic state meanings.

# Color-blind / accessibility safety

- do not rely on hue alone;
- preserve meaningful lightness differences;
- pair state color with icon/text;
- test common color-vision deficiencies;
- verify contrast for each actual foreground/background pair.

# Multi-color selection algorithm

1. identify why 4+ chromatic families are necessary;
2. assign a semantic/job role to every hue;
3. choose one dominant family;
4. choose one strongest accent;
5. make remaining hues supporting or contextual;
6. build neutral scaffold;
7. derive theme variants;
8. test grayscale hierarchy;
9. test color-vision simulation;
10. verify text/UI contrast;
11. remove any color whose removal does not harm meaning or identity.

More colors require more semantic discipline, not less.

# AI-generated rainbow guard

Reject palettes that exist only because every section received its own color, the agent wanted “energy”, a gradient generator returned many stops, a dashboard needed visually different cards, or “creative” was interpreted as rainbow.
