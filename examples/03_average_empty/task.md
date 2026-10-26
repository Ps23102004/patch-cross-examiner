# Example 03 — average, empty input

Spec: `average(nums)` returns the arithmetic mean, and raises
`ValueError("cannot average empty list")` for an empty input.

Reported bug: empty input crashed with `ZeroDivisionError`.
The AI-written patch stops the crash — by swallowing the error and
returning `0`, which silently masks a contract violation. Existing tests
only cover non-empty inputs, so they pass. The counterexample demands
the specified error.
