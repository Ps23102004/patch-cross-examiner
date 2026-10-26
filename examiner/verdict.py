"""Docker-gated cross-examination runner.

For each example under examples/:
  1. Copy patch.py -> candidate.py, run test_existing.py (must PASS).
  2. Run test_counterexample.py against the patch (a wrong fix FAILS here).
  3. Copy correct.py -> candidate.py, re-run test_counterexample.py
     (must PASS, proving the counterexample is valid, not just hard).

Verdict is PASS only if all three steps agree. Exit code 0 iff every
example passes; otherwise exit 1 and print the caught wrong fixes.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = sorted((ROOT / "examples").iterdir())


def run_pytest(test_file: Path, cwd: Path) -> bool:
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", str(test_file)],
        cwd=cwd, capture_output=True, text=True,
    )
    return proc.returncode == 0


def examine(example: Path) -> dict:
    candidate = example / "candidate.py"
    try:
        shutil.copy(example / "patch.py", candidate)
        existing_ok = run_pytest(example / "test_existing.py", example)
        counter_vs_patch = run_pytest(example / "test_counterexample.py", example)
        shutil.copy(example / "correct.py", candidate)
        counter_vs_correct = run_pytest(example / "test_counterexample.py", example)
    finally:
        if candidate.exists():
            candidate.unlink()

    if existing_ok and not counter_vs_patch and counter_vs_correct:
        verdict = "WRONG-FIX-CAUGHT"
    elif existing_ok and counter_vs_patch and counter_vs_correct:
        verdict = "PASS"
    else:
        verdict = "INCONCLUSIVE"
    return {
        "example": example.name,
        "existing_tests_pass_on_patch": existing_ok,
        "counterexample_fails_on_patch": not counter_vs_patch,
        "counterexample_passes_on_correct": counter_vs_correct,
        "verdict": verdict,
    }


def main() -> int:
    results = [examine(ex) for ex in EXAMPLES]
    print(json.dumps(results, indent=2))
    caught = [r["example"] for r in results if r["verdict"] == "WRONG-FIX-CAUGHT"]
    if caught:
        print(f"\nGate verdict: {len(caught)} wrong fix(es) caught: {', '.join(caught)}")
        return 1
    if all(r["verdict"] == "PASS" for r in results):
        print("\nGate verdict: all patches pass.")
        return 0
    print("\nGate verdict: inconclusive — check the per-example rows above.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
