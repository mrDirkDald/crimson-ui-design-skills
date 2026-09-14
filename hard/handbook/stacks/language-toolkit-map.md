# Language and Toolkit Map

This file makes the skill language-independent.

## Universal adapter for any unlisted language

When encountering an unfamiliar programming language or UI framework:

1. Identify the rendering model: DOM/document, retained-mode widgets, declarative tree, immediate-mode, scene graph/canvas, game engine, terminal, or embedded.
2. Locate the real view/screen/component entry point.
3. Locate theme/style/token primitives.
4. Locate layout primitives: row/column/grid/constraints/anchors/flex/stack/docking.
5. Locate interaction/event primitives.
6. Locate accessibility/semantics APIs.
7. Locate vector/icon support.
8. Locate animation primitives.
9. Locate platform/window/navigation primitives.
10. Apply the same design contract, hierarchy, color, type, state, accessibility, and QA rules through those primitives.

Never assume that an unfamiliar language means design rules do not apply.

## Broad map

| Language / ecosystem | Common UI paths | Design implementation notes |
|---|---|---|
| HTML/CSS | native DOM | semantic HTML, CSS layout/tokens, responsive web |
| JavaScript | DOM, React, Vue, Svelte, Electron | preserve semantics and state architecture |
| TypeScript | React/Next, Vue/Nuxt, Angular, Svelte, Electron, Tauri | type-safe component contracts and tokens |
| C# | WPF, WinUI 3, Avalonia, MAUI, Blazor, Unity | resources/styles/templates, XAML or component systems |
| F# | Avalonia, Fabulous, .NET UI | functional state mapping, shared .NET design resources |
| VB.NET | WinForms/WPF | use .NET/native control conventions; modernize cautiously |
| C | Win32, GTK, LVGL, ncurses, SDL | explicit layout/state; constrained/low-level patterns |
| C++ | Qt/QML, Win32, ImGui, wxWidgets, JUCE, Unreal | retained vs immediate vs engine-specific rules |
| Rust | Tauri, egui, iced, Slint, Dioxus, Leptos/Yew, ratatui | choose web/native/immediate/TUI lens per toolkit |
| Java | JavaFX, Swing, Android Views | scene graph/widget styling and platform conventions |
| Kotlin | Android Compose, Views, Compose Multiplatform | declarative state/theme, adaptive navigation |
| Swift | SwiftUI, UIKit, AppKit | Apple platform semantics, Dynamic Type, safe areas |
| Objective-C | UIKit/AppKit | same Apple design principles with legacy code constraints |
| Dart | Flutter | ThemeData, Material/Cupertino adaptation, widget composition |
| Python | PySide/PyQt, Tkinter, Kivy, Textual, web frameworks | toolkit-specific theming and accessibility varies |
| Go | Fyne, Gio, Wails, Bubble Tea | native/canvas/web/TUI depending toolkit |
| Ruby | Rails/Hotwire, Shoes, GTK bindings | mostly web design through HTML/CSS; native toolkit if used |
| PHP | Laravel/Blade, Symfony/Twig, Livewire | server-rendered web; semantics/CSS/component patterns |
| Elixir | Phoenix LiveView | server-driven reactive DOM; preserve latency/state feedback |
| Erlang | wxErlang/web | toolkit-specific; use universal adapter |
| Clojure | Swing/JavaFX, web | JVM/native or ClojureScript web |
| ClojureScript | Reagent/Re-frame, DOM | web semantics and state-driven component architecture |
| Scala | Scala.js, JavaFX, Swing | web or JVM lens |
| Haskell | Reflex, Brick, GTK | web/TUI/native according to toolkit |
| OCaml | Bonsai/Reason ecosystems, GTK | web/native adapter |
| Elm | browser UI | strong state model; semantic DOM/CSS |
| ReScript | React/web | React design implementation principles |
| ReasonML | React/web | React/web lens |
| Zig | raylib/SDL/custom, embedded | scene/canvas or embedded lens |
| Nim | GTK/Qt bindings, web | toolkit-specific adapter |
| Crystal | web frameworks/GTK bindings | web/native adapter |
| D | DlangUI, Qt bindings, SDL | retained/canvas adapter |
| Delphi/Object Pascal | VCL, FMX | form/component resources, platform adaptation |
| Pascal | Lazarus/LCL | desktop widget conventions |
| Lua | LÖVE, Defold, Roblox Luau, custom game UI | game/scene graph lens |
| Luau | Roblox UI | UDim2/layout constraints, input modes, safe areas, controller support |
| GDScript | Godot Control nodes | anchors/containers/themes/focus neighbors |
| C++/Blueprint | Unreal UMG/Slate | DPI scaling, focus/gamepad, style sets, widget lifecycle |
| C# Unity | UI Toolkit/uGUI | responsive anchors, scaling, input systems, accessibility limitations |
| Haxe | OpenFL, Heaps, game UI | scene/game lens |
| R | Shiny | web dashboard; data-viz and reactive-state rules |
| Julia | Makie, Gtk, web dashboards | data/desktop according to toolkit |
| Tcl | Tk | classic desktop widget model; density/platform conventions |
| Perl | Tk/web | toolkit-specific adapter |
| PowerShell | WPF/WinForms wrappers | treat as .NET desktop UI; separate script logic from view |
| Bash/Shell | dialog/whiptail/TUI | terminal hierarchy, keyboard navigation, plain-language feedback |
| QML | Qt Quick | declarative scene graph, anchors/layouts, states/transitions |
| JSX/TSX | React-like UI | component/state/semantic web or native lens |
| Razor | Blazor/ASP.NET | web semantics and component design |
| XAML | WPF/WinUI/Avalonia/MAUI | styles/resources/templates/theme dictionaries |
| XML Android | Android Views | resource qualifiers, ConstraintLayout, accessibility contentDescription |
| Compose DSL | Android/Desktop | declarative state/theme/modifier semantics |
| SwiftUI DSL | Apple | environment/theme/navigation/semantic modifiers |
| Flutter widgets | Dart | widget/theme/layout/adaptive behavior |

## If there is no mature UI toolkit

Do not invent a design framework. Determine whether the project uses a custom renderer, browser embedding, terminal, game engine, or graphics library. Apply design rules at that layer and keep business/domain logic separate from rendering.
