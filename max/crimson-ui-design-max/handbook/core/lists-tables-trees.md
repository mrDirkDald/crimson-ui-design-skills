# Lists, Tables and Trees

Dense information surfaces require deliberate hierarchy rather than oversized cards.

## Lists
Define item identity, primary label, secondary metadata, state, selection, leading/trailing actions, and multi-select behavior. Repeated row actions should align consistently.

## Tables
Choose columns based on decisions, not all available fields. Support sort/filter only where meaningful. Numeric columns align for comparison. Long text truncation needs a recovery path. Column resize/reorder should persist if the product promises customization.

## Trees
Trees expose hierarchy but can become cognitively heavy. Show expand/collapse state, selection, focus, drag target, depth, and loading of lazy children. Avoid nesting actions at every level unless users truly need them.

## Large data
Virtualization, paging, incremental loading, and search each solve different problems. Maintain stable selection and scroll state through updates.
