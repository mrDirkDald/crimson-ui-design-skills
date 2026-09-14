# Color Pairs — 2-Color Harmony Recipes

## Contents
- Purpose
- Core structure
- Harmony families
- Curated Pair Recipes
- Role patterns
- Light theme adaptation
- Dark theme adaptation
- Color-blind safety
- Pair generation algorithm
- AI-default palette guard

## Purpose

Use this reference when the design needs **two principal chromatic colors**.

It is neither possible nor useful to list every compatible RGB pair. Instead, this file provides harmony families, curated recipes, role guidance, theme adaptation, accessibility checks, and a method for generating additional pairs.

Neutral scaffold colors such as black, white, gray, warm gray, or near-black may be added for canvas, text, borders, disabled states, and accessibility. Do not force body text to use one of the two chromatic colors.

## Core structure

```text
COLOR A = dominant / brand / large-area family
COLOR B = accent / action / contrast family
NEUTRALS = canvas / text / borders
```

Avoid 50/50 chromatic competition unless the product intentionally communicates duality.

## Harmony families

### Analogous
Hue distance roughly 20°–50°. Best for calm, cohesive, atmospheric products.

### Complementary
Hue distance roughly 160°–200°. Best for strong action hierarchy, sports, gaming, entertainment. Do not use both at maximum saturation across large areas.

### Near-complementary
A softer alternative to direct complements.

### Warm + cool
One warm family and one cool family. Useful when one color represents energy/action and the other stability/structure.

### Monochromatic split
Same hue family with clearly different lightness/chroma. Useful for productivity, utilities, restrained software.

### Muted dominant + vivid accent
One dark/muted chromatic color behaves almost like a neutral; the second carries identity. This is one of the safest production UI patterns.

# Curated Pair Recipes

| # | Color A | Color B | Character / fit |
|---|---|---|---|
| 01 | `#0F172A` Deep Navy | `#22D3EE` Cyan | developer tools, technical |
| 02 | `#102A43` Deep Blue | `#2DD4BF` Teal | fintech, productivity |
| 03 | `#1E3A8A` Royal Blue | `#67E8F9` Ice Cyan | games, digital products |
| 04 | `#164E63` Petrol | `#06B6D4` Cyan | infrastructure, data |
| 05 | `#14213D` Navy | `#FCA311` Amber | communities, utilities |
| 06 | `#1D3557` Blue | `#E76F51` Coral | editorial, cultural |
| 07 | `#243B53` Slate Blue | `#FFB703` Gold | server UI, education |
| 08 | `#003049` Ink Blue | `#F77F00` Tangerine | sports, campaigns |
| 09 | `#173F35` Forest | `#A78BFA` Lavender | wellness, creative |
| 10 | `#064E3B` Emerald Deep | `#8B5CF6` Violet | creative tools |
| 11 | `#163020` Forest | `#F2C14E` Mustard | outdoor, food |
| 12 | `#31572C` Moss | `#FFB4A2` Peach | wellness, home |
| 13 | `#2E1065` Deep Purple | `#FACC15` Yellow | entertainment, events |
| 14 | `#312E81` Indigo | `#F9E2AF` Soft Gold | luxury, editorial |
| 15 | `#7F1D1D` Deep Red | `#2DD4BF` Teal | dramatic media |
| 16 | `#9F1239` Raspberry | `#14B8A6` Teal | consumer apps |
| 17 | `#9D174D` Magenta | `#2563EB` Blue | creator/social |
| 18 | `#831843` Wine Pink | `#60A5FA` Soft Blue | beauty/editorial |
| 19 | `#5C4033` Cocoa | `#3A6B66` Muted Teal | hospitality |
| 20 | `#6D597A` Dusty Plum | `#52796F` Sage Teal | cultured/editorial |
| 21 | `#172554` Navy | `#3B82F6` Blue | productivity |
| 22 | `#134E4A` Deep Teal | `#2DD4BF` Teal | health/data |
| 23 | `#3F1D5A` Deep Violet | `#A855F7` Purple | branded creative |
| 24 | `#422006` Brown Deep | `#F59E0B` Amber | craft/food |
| 25 | `#0A0A0A` Black | `#F5F5F4` Warm White | strict editorial |
| 26 | `#0D0D0D` Black | `#FFB000` Amber | industrial |
| 27 | `#07130B` Green-Black | `#B7FF3C` Lime | experimental |
| 28 | `#090B14` Indigo-Black | `#8AB4FF` Soft Blue | technical |

## Role patterns

### Quiet product
```text
70–85% neutral/base
10–20% dominant chromatic support
5–10% accent
```

### Bold brand
Use one chromatic family for identity and one for action/contrast. Keep one visually dominant.

### Dual system
Use two large-area colors only if the product truly has two meaningful modes, teams, environments, or sides.

## Light theme adaptation

- large areas: high-lightness, low-chroma tints;
- accent text/icons: darker accessible variants;
- borders: more neutral than brand surfaces;
- do not use pastel text on white.

Example:
```text
brand: #2563EB
tint: #EFF6FF
hover: #1D4ED8
pressed: #1E40AF
```

## Dark theme adaptation

- reduce accidental neon saturation;
- distinguish dark surfaces by lightness as well as hue;
- use vivid accent in controlled doses;
- avoid full-area glowing fills.

Example:
```text
brand: #38BDF8
base: #07111A
surface: #0D1C29
subtle-tint: #102A3A
```

## Color-blind safety

Do not rely only on red vs green, green vs brown, blue vs purple, or cyan vs light gray. For critical states, add label/icon/shape/pattern/position differences.

## Pair generation algorithm

1. identify subject, audience, and emotional tone;
2. choose the dominant hue from the subject, not from a trend;
3. select relationship: calm → analogous; strong action → complementary/near-complementary; technical → cool base + controlled warm accent; organic → muted green/earth + warm support;
4. reduce saturation of the less important color;
5. assign semantic roles;
6. build the neutral scaffold;
7. verify grayscale hierarchy;
8. verify actual foreground/background contrast;
9. test supported themes;
10. reject the pair if it could be dropped into five unrelated products with no loss of meaning.

## AI-default palette guard

Do not automatically fall back to cream + terracotta, near-black + acid green, near-black + vermilion, generic indigo + cyan, or black + neon purple. All are valid when grounded in the brief; they are weak when chosen only because they look “premium”, “AI”, “cyber”, or “modern”.
