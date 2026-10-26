# Example 02 — binary search, first occurrence

Spec: `first_index(a, target)` returns the index of the **first** occurrence
of `target` in sorted list `a`, or `-1` if absent.

Reported bug: single-element lists always returned `-1` (the loop used
`lo < hi`, so it never ran when `lo == hi`).
The AI-written patch fixes the loop bound — but still returns *any*
matching index, not the first. Existing tests use unique values, so they pass.
The counterexample uses duplicates.
