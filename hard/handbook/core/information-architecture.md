# Information Architecture

Information architecture determines what exists, how it is grouped, where users expect it, and how they move between levels.

## Start from jobs, not pages

List primary user jobs. Group information around jobs and entities rather than implementation modules.

Bad IA often exposes backend architecture: “services”, “objects”, “jobs”, “resources” as separate tabs even when users think in projects, files, downloads, conversations, servers, or orders.

## Hierarchy tests

For each piece of content ask:
- Is it global, section-level, local, contextual, or transient?
- Is it a destination, action, filter, status, metadata, or explanation?
- Must it persist while navigating?
- Does it belong to the selected entity or to the whole product?

Avoid navigation that mixes destinations with actions without clear distinction.

## Progressive disclosure

Hide complexity only when users can still discover it at the moment they need it. Do not bury high-frequency actions under “More” to create a cleaner screenshot.

## Stable placement

Frequent controls benefit from stable placement. Moving a primary action between states can increase cognitive load. Contextual actions can move with context, but the relationship must remain obvious.

## Breadcrumbs, sidebars, tabs, command surfaces

Choose based on depth and task shape, not fashion. Sidebars work well for persistent destinations. Tabs work for peer views of one entity. Breadcrumbs work for nested location. Command palettes supplement discoverability; they should not replace all visible navigation for ordinary users.
