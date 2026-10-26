# Patch Cross-Examiner

Catches AI-written code fixes that **pass the existing tests but are still wrong**,
by gating every candidate patch on counterexample tests written from the spec.

Built for the Meta Global AI Developer Hackathon (Indie Dev Track, Oct 26 – Nov 4, 2026).
The idea on file: a fix is only accepted when it passes the existing suite **and**
a set of counterexample tests that probe exactly where the old fix went wrong.

## How the gate works

For each example, the runner:

1. Copies the candidate `patch.py` in as `candidate.py`.
2. Runs the existing test suite — must pass.
3. Runs the counterexample suite — must pass. This is the cross-examination:
   it checks the spec the existing tests never pinned down.
4. Re-runs the counterexample suite against the known-correct `correct.py`,
   to prove the counterexample is valid (it passes on a genuinely right fix).

Verdict per example: `PASS` only if all three steps agree. Anything else is
reported as `WRONG-FIX-CAUGHT`, with the failing counterexample named.

## Run it

```bash
docker build -t patch-cross-examiner .
docker run --rm patch-cross-examiner
```

Or without Docker:

```bash
pip install pytest
python examiner/verdict.py
```

## The three curated examples (Part 1)

| # | Function | The wrong fix | What the counterexample catches |
|---|----------|---------------|-------------------------------|
| 01 | `dedup` (order-preserving) | `list(set(items))` | Set ordering destroys first-seen order |
| 02 | `first_index` (binary search) | Returns *any* match | Spec wants the *first* occurrence |
| 03 | `average` | `try/except` returning `0` | Masks the empty-input error instead of raising `ValueError` |

Each example ships `original.py` (the reported bug), `patch.py` (the
plausible-but-wrong AI fix), `correct.py` (reference fix), plus
`test_existing.py` and `test_counterexample.py`.

## Roadmap

- **Part 1 (this scaffold):** repo skeleton, Docker-gated runner, 3 hand-curated examples.
- **Part 2:** counterexample generator — propose candidate counterexamples from the
  spec + the patch diff, then verify each one against the reference fix.
- **Part 3:** verdict logic + report — ranked verdicts, minimal failing
  counterexample, demo video.
