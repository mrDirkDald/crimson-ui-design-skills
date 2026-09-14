# Color Trios — 3-Color Harmony Recipes

## Purpose

Use when the visual system genuinely needs **three principal chromatic colors**.

Typical hierarchy:

```text
COLOR A = dominant
COLOR B = supporting
COLOR C = accent
NEUTRALS = canvas / text / borders
```

Avoid three equally saturated colors unless the product intentionally needs high visual energy.

## Harmony models

### Analogous trio
Three neighboring hues. Cohesive and atmospheric.

### Split-complementary
One dominant hue plus two hues around its complement. Strong but more controllable than a hard triad.

### Restrained triadic
Three separated hue families, but only one gets maximum chroma.

### Warm / cool / bridge
One warm hue, one cool hue, and one muted bridge color.

### Neutral-chromatic trio
Two muted chromatic colors plus one vivid accent. Excellent for production UI.

# Curated Trio Recipes

| # | Dominant | Support | Accent | Character |
|---|---|---|---|---|
| 01 | `#0F172A` Navy | `#155E75` Petrol | `#22D3EE` Cyan | technical |
| 02 | `#102A43` Deep Blue | `#0F766E` Teal | `#F59E0B` Amber | trustworthy + active |
| 03 | `#1E293B` Slate | `#1D4ED8` Blue | `#2DD4BF` Teal | product/SaaS |
| 04 | `#111827` Blue-Black | `#4338CA` Indigo | `#38BDF8` Sky | developer |
| 05 | `#172554` Navy | `#0E7490` Cyan Deep | `#A3E635` Lime | technical-organic |
| 06 | `#4A2C2A` Cocoa | `#B45309` Ochre | `#F5E6CC` Cream | crafted |
| 07 | `#7C2D12` Rust | `#C2410C` Orange | `#1D4ED8` Blue | editorial tension |
| 08 | `#6B3E2E` Umber | `#D97706` Amber | `#355070` Dusty Blue | mature |
| 09 | `#7F1D1D` Wine Red | `#D97757` Clay | `#264653` Deep Teal | cultural |
| 10 | `#5C4033` Brown | `#CA8A04` Mustard | `#52796F` Sage | artisan |
| 11 | `#1B4332` Pine | `#74C69D` Sage Mint | `#F2C14E` Warm Yellow | natural |
| 12 | `#31572C` Moss | `#90A955` Olive | `#EC9A29` Ochre | earthy |
| 13 | `#134E4A` Deep Teal | `#5EEAD4` Mint | `#FB7185` Coral | wellness/consumer |
| 14 | `#2E1065` Deep Purple | `#7C3AED` Violet | `#FACC15` Yellow | creative |
| 15 | `#4C1D95` Violet | `#DB2777` Magenta | `#22D3EE` Cyan | digital |
| 16 | `#312E81` Indigo | `#E11D48` Rose | `#F59E0B` Amber | energetic |
| 17 | `#581C87` Purple | `#2563EB` Blue | `#F97316` Orange | entertainment |
| 18 | `#701A75` Fuchsia Deep | `#0F766E` Teal | `#FDE047` Lemon | playful |
| 19 | `#1D4ED8` Blue | `#F97316` Orange | `#EAB308` Yellow | split-complementary |
| 20 | `#0F766E` Teal | `#E11D48` Rose | `#F59E0B` Amber | lively |
| 21 | `#7C3AED` Violet | `#22C55E` Green | `#EAB308` Yellow | expressive |
| 22 | `#DC2626` Red | `#06B6D4` Cyan | `#2563EB` Blue | strong |
| 23 | `#334155` Slate | `#0F766E` Teal | `#F59E0B` Amber | balanced product |
| 24 | `#3F3F46` Zinc | `#2563EB` Blue | `#E11D48` Rose | modern |
| 25 | `#292524` Warm Black | `#78716C` Taupe | `#EA580C` Orange | architectural |
| 26 | `#1F2937` Charcoal | `#6D28D9` Purple | `#10B981` Emerald | creative tool |
| 27 | `#172554` Navy | `#64748B` Blue Gray | `#FB7185` Coral | refined |
| 28 | `#3B0764` Aubergine | `#64748B` Slate | `#38BDF8` Sky | premium-tech |

## Distribution patterns

### 60 / 30 / 10
Useful for expressive brand systems.

### 80 / 15 / 5
Better for productivity and repeated-use software.

In actual UI, neutrals often occupy most pixels. Do not interpret percentages as literal screen coverage if it harms hierarchy.

## Light theme

- dominant chromatic family can become a tint/surface;
- support can carry secondary selection;
- accent can carry primary CTA;
- body text normally stays dark neutral.

## Dark theme

- pick one brightest chromatic color;
- lower luminance/chroma of the other two;
- avoid three simultaneous glows;
- keep semantic states separate.

## Color-blind safety

Trios should differ in more than hue. Use lightness/chroma differences too. For charts and critical states, add shape, label, pattern, or line-style differences.

## Trio generation algorithm

1. choose dominant hue from subject/product;
2. choose visual intensity;
3. choose harmony: cohesive → analogous; lively → split-complementary; expressive → restrained triad; product UI → muted dominant + muted support + vivid accent;
4. assign dominance;
5. reduce chroma on non-primary hues;
6. add neutral scaffold;
7. verify contrast independently;
8. test grayscale;
9. test color-vision robustness;
10. remove any hue that has no semantic or identity job.

## Anti-patterns

Do not create blue + purple + cyan merely because it looks “tech”, purple + pink + orange merely because it looks “creative”, three neon colors on black, three low-contrast pastels, or one hue per component section. Every hue must have a role.
