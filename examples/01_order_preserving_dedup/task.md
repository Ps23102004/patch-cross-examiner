# Example 01 — order-preserving dedup

Spec: `dedup(items)` returns each distinct value once, **in first-seen order**.
`dedup([3, 1, 3, 2, 1])` must be `[3, 1, 2]`.

Reported bug: duplicates were not removed at all.
The AI-written patch removes duplicates — but via `set()`, which destroys
first-seen order. The existing tests only check membership, so they pass.
The counterexample pins the order down.
