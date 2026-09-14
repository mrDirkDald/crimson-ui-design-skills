    # Case Study Web — ULTRA-HARD playbook

    ## Purpose

    Structure case studies around context, problem, constraints, decisions, artifacts, outcomes, and honest attribution.

    This playbook belongs to the **web** layer of Crimson UI Design ULTRA-HARD. It is intentionally detailed. Do not compress the reasoning merely to save tokens when this topic materially governs the requested work. Load it selectively when relevant, but once loaded, use the full decision model rather than cherry-picking decorative rules.

    ## Core dimensions

    - **context** — inspect its role, current behavior, constraints, edge cases, and evidence.
- **problem** — inspect its role, current behavior, constraints, edge cases, and evidence.
- **constraint** — inspect its role, current behavior, constraints, edge cases, and evidence.
- **decision** — inspect its role, current behavior, constraints, edge cases, and evidence.
- **artifact** — inspect its role, current behavior, constraints, edge cases, and evidence.
- **outcome** — inspect its role, current behavior, constraints, edge cases, and evidence.

    ## Operating sequence

    1. **Observe** — Inspect the real rendered surface, code path, content/data, platform, and user workflow.
2. **Frame** — Write the user decision/job, must-preserve behavior, constraints, unknowns, and success evidence.
3. **Model** — Describe the relevant objects, states, actions, relationships, hierarchy, and failure paths.
4. **Diagnose** — Identify root problems and separate structural causes from surface symptoms.
5. **Explore** — When ambiguity is real, compare structurally different directions instead of cosmetic variants.
6. **Choose** — Select one direction and state the strongest alternative, tradeoff, and preservation risk.
7. **Implement** — Map the decision to the actual framework/toolkit without inventing APIs or rewriting unrelated logic.
8. **Verify** — Run the target, exercise relevant states and inputs, inspect the rendered result, and record evidence.
9. **Stop** — Stop when acceptance is met and additional changes would add more churn than value.

    ## Evidence contract

    Separate evidence from inference:

    ```text
    OBSERVED RUNTIME:
    GOVERNING SOURCE / COMPONENT:
    REAL CONTENT / DATA:
    PLATFORM / TOOLKIT RULE:
    REFERENCE SIGNAL:
    INFERENCE:
    UNKNOWN:
    BLOCKED:
    ```

    Use `PASS / FAIL / NOT REVIEWED / BLOCKED / N/A / UNKNOWN`. `PASS` requires observed evidence for behavior. Source inspection can support a hypothesis but cannot prove pointer, keyboard, animation, resize, packaging, or assistive-technology behavior by itself.

    ## Detailed dimension analysis

    ### 1. Context

Treat **context** as a first-class design variable rather than a finishing detail. Determine what the user needs from it, which object or state owns it, how often it changes, and what failure would cost. Inspect both the normal path and at least one adverse path. If the design relies on this dimension for hierarchy, confirm that the signal survives grayscale/value inspection, narrow layout, long content, keyboard focus, and reduced motion where applicable.

Ask:
- What does context communicate before the user interacts?
- What changes when the user acts, waits, fails, retries, resizes, changes theme, or switches input method?
- Can a user understand the same information without relying on color, hover, animation, or precise pointer control?
- Is the current implementation a real semantic/state boundary or merely a visual convention copied from another product?
- What would a simpler implementation lose? What would a more expressive implementation risk?
- Which runtime observation would falsify the proposed solution?
### 2. Problem

Treat **problem** as a first-class design variable rather than a finishing detail. Determine what the user needs from it, which object or state owns it, how often it changes, and what failure would cost. Inspect both the normal path and at least one adverse path. If the design relies on this dimension for hierarchy, confirm that the signal survives grayscale/value inspection, narrow layout, long content, keyboard focus, and reduced motion where applicable.

Ask:
- What does problem communicate before the user interacts?
- What changes when the user acts, waits, fails, retries, resizes, changes theme, or switches input method?
- Can a user understand the same information without relying on color, hover, animation, or precise pointer control?
- Is the current implementation a real semantic/state boundary or merely a visual convention copied from another product?
- What would a simpler implementation lose? What would a more expressive implementation risk?
- Which runtime observation would falsify the proposed solution?
### 3. Constraint

Treat **constraint** as a first-class design variable rather than a finishing detail. Determine what the user needs from it, which object or state owns it, how often it changes, and what failure would cost. Inspect both the normal path and at least one adverse path. If the design relies on this dimension for hierarchy, confirm that the signal survives grayscale/value inspection, narrow layout, long content, keyboard focus, and reduced motion where applicable.

Ask:
- What does constraint communicate before the user interacts?
- What changes when the user acts, waits, fails, retries, resizes, changes theme, or switches input method?
- Can a user understand the same information without relying on color, hover, animation, or precise pointer control?
- Is the current implementation a real semantic/state boundary or merely a visual convention copied from another product?
- What would a simpler implementation lose? What would a more expressive implementation risk?
- Which runtime observation would falsify the proposed solution?
### 4. Decision

Treat **decision** as a first-class design variable rather than a finishing detail. Determine what the user needs from it, which object or state owns it, how often it changes, and what failure would cost. Inspect both the normal path and at least one adverse path. If the design relies on this dimension for hierarchy, confirm that the signal survives grayscale/value inspection, narrow layout, long content, keyboard focus, and reduced motion where applicable.

Ask:
- What does decision communicate before the user interacts?
- What changes when the user acts, waits, fails, retries, resizes, changes theme, or switches input method?
- Can a user understand the same information without relying on color, hover, animation, or precise pointer control?
- Is the current implementation a real semantic/state boundary or merely a visual convention copied from another product?
- What would a simpler implementation lose? What would a more expressive implementation risk?
- Which runtime observation would falsify the proposed solution?
### 5. Artifact

Treat **artifact** as a first-class design variable rather than a finishing detail. Determine what the user needs from it, which object or state owns it, how often it changes, and what failure would cost. Inspect both the normal path and at least one adverse path. If the design relies on this dimension for hierarchy, confirm that the signal survives grayscale/value inspection, narrow layout, long content, keyboard focus, and reduced motion where applicable.

Ask:
- What does artifact communicate before the user interacts?
- What changes when the user acts, waits, fails, retries, resizes, changes theme, or switches input method?
- Can a user understand the same information without relying on color, hover, animation, or precise pointer control?
- Is the current implementation a real semantic/state boundary or merely a visual convention copied from another product?
- What would a simpler implementation lose? What would a more expressive implementation risk?
- Which runtime observation would falsify the proposed solution?
### 6. Outcome

Treat **outcome** as a first-class design variable rather than a finishing detail. Determine what the user needs from it, which object or state owns it, how often it changes, and what failure would cost. Inspect both the normal path and at least one adverse path. If the design relies on this dimension for hierarchy, confirm that the signal survives grayscale/value inspection, narrow layout, long content, keyboard focus, and reduced motion where applicable.

Ask:
- What does outcome communicate before the user interacts?
- What changes when the user acts, waits, fails, retries, resizes, changes theme, or switches input method?
- Can a user understand the same information without relying on color, hover, animation, or precise pointer control?
- Is the current implementation a real semantic/state boundary or merely a visual convention copied from another product?
- What would a simpler implementation lose? What would a more expressive implementation risk?
- Which runtime observation would falsify the proposed solution?


    ## Decision matrix

    | Dimension | Questions | Evidence | Typical failure |
|---|---|---|---|
| context | What must the user understand/do? What changes by state, width, input, or permission? | Runtime, governing source, real content/data | Generic defaults, ambiguous hierarchy, unverified assumption |
| problem | What must the user understand/do? What changes by state, width, input, or permission? | Runtime, governing source, real content/data | Generic defaults, ambiguous hierarchy, unverified assumption |
| constraint | What must the user understand/do? What changes by state, width, input, or permission? | Runtime, governing source, real content/data | Generic defaults, ambiguous hierarchy, unverified assumption |
| decision | What must the user understand/do? What changes by state, width, input, or permission? | Runtime, governing source, real content/data | Generic defaults, ambiguous hierarchy, unverified assumption |
| artifact | What must the user understand/do? What changes by state, width, input, or permission? | Runtime, governing source, real content/data | Generic defaults, ambiguous hierarchy, unverified assumption |
| outcome | What must the user understand/do? What changes by state, width, input, or permission? | Runtime, governing source, real content/data | Generic defaults, ambiguous hierarchy, unverified assumption |

    ## State / condition matrix

    | State or condition | Required design reasoning | Verification note |
    |---|---|---|
    | default | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| hover / pointer-over | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| focus-visible | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| pressed / active | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| selected | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| disabled | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| loading / pending | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| empty | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| partial / stale | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| success | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| warning | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| error | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| offline / disconnected | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| permission denied / limited | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| read-only | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| long-content / localization | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| narrow / compact | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| wide / high-density | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| reduced-motion | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |
| high-contrast / forced-colors | Define what changes, what stays available, and what evidence proves correctness. | Do not infer from default-state styling. |

    ## Responsive and density reasoning

    Do not treat responsiveness as a final CSS pass. For this topic, define what survives, what reorders, what collapses, what becomes scrollable, what changes interaction model, and what is intentionally removed at each meaningful width/density. Test content-driven breakage rather than device-name breakpoints only. High-density desktop, narrow split panes, browser zoom, text scaling, and localization expansion are distinct stresses.

    A valid responsive plan records:

    ```text
    WIDE / EXPANSIVE:
    STANDARD DESKTOP:
    NARROW WINDOW / TABLET:
    MOBILE / COMPACT:
    HIGH TEXT SCALE:
    LONG CONTENT:
    INPUT CHANGE:
    MOTION REDUCTION:
    ```

    ## Accessibility integration

    Accessibility is part of the design model. Preserve semantic name/role/state/value, logical focus order, visible focus, keyboard-equivalent operation, non-color cues, readable contrast, text scaling, reduced motion, and platform assistive-technology expectations. Custom-rendered controls need explicit accessibility bridging; a visually faithful custom control is not equivalent to a semantic control by default.

    ## Performance and implementation integrity

    Prefer the real framework/toolkit primitives and existing project architecture when sound. Avoid adding rendering layers, event loops, global listeners, timers, observers, animation systems, or duplicated state merely to reproduce a screenshot. Measure expensive effects and large media. Preserve cancellation, lifecycle, cleanup, navigation, data contracts, and packaging constraints.

    ## Failure modes

    - Treating a screenshot as proof of the underlying interaction or state model.
- Adding decorative structure before understanding the product task and content model.
- Replacing useful platform conventions with novelty that reduces discoverability.
- Solving hierarchy with borders/cards/chips instead of content order, alignment, type, and spacing.
- Using accent color everywhere so nothing remains visually primary.
- Assuming desktop composition can simply stack vertically on narrow screens.
- Inventing capabilities, customer proof, metrics, reviews, logos, or success states.
- Refactoring unrelated business logic for visual convenience.
- Claiming accessibility, runtime, or performance PASS without observing evidence.
- Optimizing a local visual symptom while preserving the systemic cause.
- Hiding important state behind hover-only interaction.
- Using one component API for semantically different objects just because they look similar.
- Letting loading, empty, disabled, stale, and error states become visually indistinguishable.
- Ignoring long content, localization expansion, zoom, text scaling, and unusual window sizes.
- Continuing polish after acceptance criteria are already met.

    ## Adversarial review

    Before accepting the solution, attempt to disprove it:

    1. Hide the logo and accent color. Does the design still belong to this product?
    2. Replace ideal content with long, missing, partial, or error content. Does hierarchy survive?
    3. Navigate only by keyboard or the relevant non-pointer input. Is every critical action reachable and understandable?
    4. Disable motion. Does spatial/state meaning remain clear?
    5. Resize to a narrow window and then an unusually wide one. Does the composition recompose intentionally?
    6. Switch light/dark/high-contrast or equivalent themes when supported. Do semantic roles remain coherent?
    7. Force a slow/loading/failure path. Does the user know what is happening and what remains safe?
    8. Remove decorative surfaces. Which ones were actually carrying semantics and which were visual habit?
    9. Compare against the strongest plausible alternative. Why is the selected direction still better for this product?
    10. Ask what runtime evidence would make you reverse the decision.

    ## Verification checklist

    - [ ] The user job and primary decision are explicit.
    - [ ] Must-preserve behavior is recorded before implementation.
    - [ ] Governing objects/states/actions are modeled.
    - [ ] Hierarchy works without relying only on accent color.
    - [ ] Default, focus, disabled, pending, error, and recovery states are covered where applicable.
    - [ ] Narrow, wide, long-content, and text-scaling conditions were considered.
    - [ ] Relevant input methods have equivalent critical paths.
    - [ ] Semantic accessibility is preserved or explicitly bridged.
    - [ ] The implementation uses the real framework/toolkit rather than invented abstractions.
    - [ ] Performance-sensitive effects/media have budgets or fallbacks.
    - [ ] Product-specificity survives logo/accent removal.
    - [ ] No fabricated content, proof, metrics, reviews, capabilities, or success states were introduced.
    - [ ] Runtime evidence is separated from inference.
    - [ ] Further changes are stopped once acceptance is met.

    ## Evidence packet / deliverable

    ```text
TOPIC: Case Study Web
USER JOB:
PRIMARY DECISION:
MUST PRESERVE:
CURRENT FAILURE:
ROOT CAUSE:
SELECTED DIRECTION:
STRONGEST ALTERNATIVE:
TRADEOFF ACCEPTED:
RESPONSIVE DIFFERENCE:
ACCESSIBILITY DIFFERENCE:
RUNTIME PROOF:
UNVERIFIED / BLOCKED:
```

    ## ULTRA-HARD rule

    Do not shorten this playbook into a tiny generic checklist when **case study web** is central to the task. The purpose of ULTRA-HARD is to keep the deeper reasoning available: state behavior, failure recovery, responsive changes, accessibility, implementation constraints, alternatives, and runtime proof—not merely the polished default screenshot.
