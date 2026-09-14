# Web UI

## Contents
- Browser baseline
- Positive patterns
- Marketing
- Web apps and authenticated SaaS
- Offline/PWA
- Dashboards and charts
- E-commerce
- Docs/developer
- Editorial
- Web forms
- Responsive/navigation
- Performance/accessibility
- Completion checks

## Browser baseline

Respect:
- semantic HTML;
- back/forward;
- URLs/deep links;
- focus/keyboard;
- zoom/reflow;
- responsive layout;
- loading/network failure;
- native form behavior;
- link vs button semantics.

Do not turn ordinary web UI into a custom canvas without product need.

## Positive patterns

### Expressive web routing

For portfolio, agency, festival, campaign, culture, entertainment, luxury or experimental sites where experience/identity materially matters, load `references/expressive-web.md`.

The normal Web rules remain the usability/content/navigation baseline. Expressive rules add experience craft; they do not replace browser semantics, responsive behavior, accessibility or performance.

Do not apply award-site spectacle automatically to authenticated/repeated-use product screens.

## Marketing
`clear promise → primary CTA → product-specific proof → capabilities/use cases → objections/trust → final action`

### SaaS / web app
`navigation/context → primary work area → state/action controls → contextual details → recovery`

### Dashboard
`scope/time/filter → decision summary → inspectable data → compare/drill-down → bulk/export`

### Docs
`global nav/search → section nav/TOC → technical content → anchors/code/examples → version/context`

#### Data color semantics

For charts and dense data views:
- categorical series need sufficiently distinguishable hues;
- sequential data should use an ordered lightness/chroma scale;
- diverging data should use a meaningful neutral midpoint;
- positive/negative meaning must not rely on red/green alone;
- identical meaning should use identical color semantics across charts;
- do not reuse the brand accent for unrelated data categories merely to make charts look branded;
- highlight one selected/important series by emphasis while allowing others to recede.

For many series, reduce simultaneous chromatic emphasis and use labels, line styles, markers, grouping, small multiples or interaction. Do not solve a 12-series chart with 12 equally saturated colors.

Missing/unavailable data should use a distinct neutral treatment unless success/failure semantics are actually true.

## E-commerce
`product confidence → variant/price/availability → purchase action → shipping/returns/trust → cart/checkout recovery`

## Marketing

Prioritize:
- what product is;
- why it matters;
- primary CTA;
- truthful proof;
- coherent narrative.

Avoid fabricated metrics/logos/testimonials and generic adjective-heavy copy.

Hero treatment should be a thesis, not a required giant block.

## Web apps and authenticated SaaS

Prioritize:
- task completion;
- state clarity;
- route/history behavior;
- useful density;
- keyboard/focus;
- loading/error recovery.

### Authentication
Handle relevant:
- sign in/out;
- registration;
- password reset;
- email verification;
- MFA/2FA;
- SSO.

### Session
Handle:
- expiration;
- refresh/reauthentication;
- unsaved work;
- logout elsewhere when relevant.

### Authorization
Distinguish:
- unauthenticated;
- forbidden (`403`);
- not found (`404`);
- server failure (`5xx`).

### Route guards
Avoid redirect loops and protected-content flash.
Preserve intended destination after login when appropriate.

### Account/workspace switching
Keep current context obvious and avoid stale data leaking across contexts.

## Offline / reconnect / PWA

Distinguish offline from server failure.

Preserve unsent input where possible.
Retry safely without duplicate mutations.

For PWA:
- do not nag install;
- model service-worker update state;
- avoid unsafe refresh while work is active;
- define what remains available offline;
- request browser permissions in context.

## Dashboard / data-heavy

Design around decisions.

Prioritize:
- data scope;
- time range;
- filters;
- sorting;
- search;
- comparison;
- drill-down;
- bulk actions;
- density.

### Tables
Support relevant:
- sorting/filtering;
- column alignment;
- sticky headers;
- selection;
- visibility/resize;
- copy;
- pagination/virtualization;
- empty/loading/error.

### Charts
A chart must answer a real question.

Require relevant:
- title/context;
- units;
- time range;
- source freshness;
- accessible legend;
- non-color encoding where needed.

Do not manipulate axes to exaggerate.
Bar charts normally need a meaningful zero baseline unless an exception is clearly justified.
Use dual axes cautiously.
Make aggregation explicit.
For dense time series, use sensible sampling/aggregation and accessible non-hover alternatives.
Provide a table/summary when important information cannot otherwise be understood non-visually.

## E-commerce

### Product
Clarify:
- identity/media;
- price;
- selected variant;
- stock;
- shipping/delivery;
- returns/trust;
- purchase action.

### Variants
Selected state must be obvious.
Unavailable combinations should be honest.
Do not reset choices unexpectedly.

### Cart/checkout
Support:
- quantities/options;
- price breakdown;
- update/remove;
- final total;
- validation;
- payment state;
- duplicate-submit protection;
- failure recovery.

Do not use deceptive urgency/scarcity/trust patterns.

## Docs / developer portals

Support relevant:
- sidebar hierarchy;
- TOC;
- anchors/deep links;
- search;
- breadcrumbs;
- version selector;
- code blocks/copy;
- API/property tables;
- long pages.

Code must handle horizontal overflow and accessible syntax contrast.

## Editorial

Prioritize reading:
- reasonable measure;
- heading rhythm;
- paragraph spacing;
- figures/captions;
- references;
- non-obstructive sticky UI.

Do not center long-form body text.

## Web forms

Core owns shared form behavior.

Web additions:
- real label semantics;
- correct input types;
- autofill;
- password-manager compatibility;
- Enter behavior;
- accessible error association;
- browser-native editing;
- dirty-form route behavior.

## Responsive / navigation

Responsive means reprioritization, not stacking.

May require:
- reordered content;
- alternate navigation;
- changed control placement;
- changed density;
- hidden secondary content;
- alternate table/list treatment;
- collapsed filters.

Preserve relevant:
- back/forward;
- reload;
- deep links;
- shareable URLs;
- route/filter state;
- selected destination.

## Performance / accessibility

Challenge:
- huge media;
- autoplay backgrounds;
- blur/filter abuse;
- layout shifts;
- excessive client JS;
- animation-heavy scroll;
- unvirtualized huge lists.

Accessibility:
- landmarks/headings;
- labels;
- keyboard/focus;
- skip links when needed;
- accessible names;
- zoom/reflow;
- contrast;
- reduced motion;
- error identification;
- live regions for meaningful async state.

Prefer native semantics over ARIA recreation.

## Completion checks

```text
[ ] Browser history/navigation works
[ ] Auth/session/authorization states are distinct when relevant
[ ] Offline/reconnect/PWA update states are safe when relevant
[ ] Responsive hierarchy is verified
[ ] Long/localized content is handled
[ ] Dashboard/chart semantics are honest when relevant
[ ] E-commerce/docs/editorial module checks are applied when relevant
[ ] Web semantics/accessibility are preserved
[ ] Performance-heavy decoration is justified
```

# MAX Edition Web Addendum

For substantial web work also inspect semantic DOM structure, browser history, focus management after route/state changes, URL/deep-link behavior, server/client loading boundaries, offline/retry conditions, reduced motion, responsive media, font loading, and actual network latency states. A polished static screenshot is not sufficient evidence of a high-quality web product.
