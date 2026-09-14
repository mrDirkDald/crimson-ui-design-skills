# Navigation Deep Guide

Navigation structure should match the product's entity and task hierarchy.

## Global vs local
Global navigation changes major product area. Local navigation changes views of the current entity. Contextual actions should not masquerade as destinations.

## Back behavior
On web, respect browser history. On mobile, respect platform back semantics. On desktop, back/forward can be useful for document/location history but should not conflict with undo.

## Deep links
If users can share or revisit a state, preserve meaningful URL/document identity when architecture allows it.

## Sidebars
Use for persistent destination sets, trees, collections, or tools that benefit from constant visibility. Do not add a sidebar because SaaS templates have one.

## Tabs
Use for peer views in the same context. Persist state where expected. Avoid nested tab bars that create ambiguous hierarchy.
