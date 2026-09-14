# Mobile & Tablet Application UI

## Contents
- Navigation/Back/deep links
- Software keyboard / IME
- Permissions
- Safe areas/system bars
- Reachability and gestures
- Lifecycle/restoration
- Tablet adaptation
- Mobile accessibility
- Input methods

## Mobile principle

Mobile is not desktop compressed.
Prioritize one dominant task per screen, touch-sized actions, predictable navigation and interruption-safe state.

## Navigation / Back / deep links

Use platform-appropriate stack, peer tabs/bottom navigation, top bars, sheets and contextual actions.

System Back must behave predictably.
Selected destination must remain obvious.
Deep links must enter a valid navigable state and provide a sensible return path.
Avoid unnecessary deep nesting.

## Software keyboard / IME

Verify:
- correct keyboard/input type;
- focused field remains visible;
- primary action remains reachable;
- Next/Done behavior;
- keyboard dismissal;
- bottom controls are not hidden;
- IME composition is not broken by aggressive validation/rerender.

Do not test only with keyboard closed.

## Permissions

Request in context.
Handle denial, permanent denial/settings route, partial functionality and re-request strategy.
Explain value before asking when context is not obvious.
Permission denial is a product state, not an edge case.

## Safe areas / system bars

Respect status bar, home/navigation indicator, cutouts/notches, gesture regions, edge-to-edge content and keyboard insets.
Interactive controls must not collide with system gesture areas.

## Reachability / gestures

Keep high-frequency phone actions reachable where practical without breaking platform conventions.

Gestures may accelerate but should not hide essential functionality.
For swipe/drag/long-press provide feedback, protect destructive actions, avoid system gesture conflicts and provide alternatives where needed.

## Lifecycle / interruption / restoration

Handle relevant:
- backgrounding;
- process death;
- rotation/configuration change;
- external intents/share flows;
- permission prompts;
- interruptions.

Recover navigation, form data, selection, task progress and pending action when product semantics require it.

## Tablet

Tablet is not a large phone.
Use space for master-detail, split view, sidebars, inspector, drag/drop, keyboard/pointer and multi-window when they improve workflow.
Do not merely enlarge phone controls.

## Mobile accessibility

### iOS / iPadOS
Support Dynamic Type, meaningful VoiceOver labels/traits/values/order, accessible custom actions and layouts that survive preferred text size growth.

### Android
Support system font scaling, TalkBack content/roles/states, logical traversal, accessible alternatives for custom gestures and semantic custom controls.

Important async state changes should be available to assistive technology.

## Pointer / stylus / touch

Tablets may support pointer, hover and stylus alongside touch.
Do not make hover mandatory.
Use precision interactions only where the device/input actually supports them.
Keep essential actions reachable through touch/keyboard alternatives.
