# Crimson UI Design MAX

This is the intentionally exhaustive edition of Crimson UI Design.

It is for agents and teams that prefer maximum design guidance over token efficiency. It contains the compact rules, deeper design theory, implementation notes for many programming languages and UI toolkits, product-pattern guidance, QA checklists, platform conventions, and fallback rules for unknown stacks.

Use the compact `CRIMSON-UI-DESIGN-SKILL` when context cost matters. Use this MAX package when the expected value of deeper analysis is higher than the token cost.

## Philosophy

MAX does not mean “add more effects” or “make every answer longer”. It means the agent is allowed and expected to inspect enough design context to make a high-confidence decision, trace the real implementation, preserve product behavior, and verify the rendered result.

The package deliberately repeats some critical rules in several places so that important constraints survive partial loading and platform-specific work.

## Baseline icon rule

1. Preserve an existing coherent project icon system.
2. Otherwise use Lucide Icons as the baseline where technically suitable.
3. Use compatible custom SVG/vector icons for brand-specific or domain-specific concepts.
4. Do not use emoji as UI icons.

## Universal language rule

No programming language is excluded. If a language or toolkit is not explicitly documented, classify its UI architecture first: web/document, retained-mode native, immediate-mode, canvas/scene graph, terminal/TUI, embedded, or game-engine UI. Then apply the matching design rules and map them to the toolkit's real primitives.


## Nested aspect subskills

Every top-level domain skill now contains six deep aspect subskills.

Current hierarchy contains **66 nested aspect skills** across **11 parent domain skills**.

A parent skill explains the domain as a whole; its aspect skills go much deeper into one problem class. For example:

- `visual` splits into composition, typography, imagery, identity, motion, and iconography;
- `color` splits into harmony theory, semantic tokens, themes, accessibility, data color, and palette generation;
- `web` splits into responsive layout, navigation, forms, data-dense UI, async state, and performance;
- `application` splits into workflow, commands, selection/focus, persistence/recovery, density/inspectors, and desktop/mobile adaptation;
- `qa` splits into visual hierarchy, interaction states, accessibility, responsive/cross-platform, visual regression, and evidence reporting.

This is deliberately verbose. The nested structure is meant to give an agent a specialized playbook for each important design concern rather than one enormous undifferentiated checklist.
