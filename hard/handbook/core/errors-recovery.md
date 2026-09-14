# Errors, Recovery, Destructive Actions

## Recovery first

When an operation can fail, design the retry/cancel/recover path before polishing success state.

## Destructive actions

Differentiate irreversible deletion, reversible archive, remove-from-list, disconnect, revoke, and reset. Labels and confirmation should match real consequence.

## Undo

Undo is often better than modal confirmation for low-risk reversible actions.

## Partial failure

Batch operations need to show which items succeeded and which failed, not a single ambiguous toast.
