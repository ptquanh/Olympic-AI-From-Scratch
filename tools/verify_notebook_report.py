"""Verify that an execution report covers the current manifest notebook bytes."""

import argparse
import hashlib
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def expected_notebooks(profile: str) -> set[str]:
    manifest = yaml.safe_load((ROOT / "curriculum.yml").read_text(encoding="utf-8"))
    result = set()
    for chapter in manifest["chapters"]:
        if profile == "gpu" and not chapter["gpu_full"]:
            continue
        for path in (ROOT / chapter["path"]).glob("*.ipynb"):
            if "practice" not in path.name:
                result.add(path.relative_to(ROOT).as_posix())
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report")
    parser.add_argument("--profile", choices=("cpu", "gpu"), required=True)
    parser.add_argument("--min-repeats", type=int, default=1)
    parser.add_argument(
        "--allow-partial",
        action="store_true",
        help="verify the runner-recorded incremental scope instead of requiring every notebook",
    )
    args = parser.parse_args()

    report_path = ROOT / args.report
    payload = json.loads(report_path.read_text(encoding="utf-8"))
    errors = []
    environment = payload.get("environment", {})
    if environment.get("profile") != args.profile:
        errors.append(f"profile mismatch: {environment.get('profile')!r}")
    if args.profile == "gpu":
        if not environment.get("cuda_available") or not environment.get("gpu"):
            errors.append("GPU report has no CUDA device evidence")
        if environment.get("fast_mode"):
            errors.append("GPU full report must not use fast mode")

    rows = payload.get("notebooks", [])
    actual = {row["path"] for row in rows}
    full_expected = expected_notebooks(args.profile)
    expected = full_expected
    if args.allow_partial and environment.get("selection_mode") in {"changed", "filtered"}:
        expected = set(environment.get("selected_notebooks", []))
        invalid = expected - full_expected
        if invalid:
            errors.append(f"incremental scope contains non-manifest notebooks: {sorted(invalid)}")
    if actual != expected:
        errors.append(f"coverage mismatch: missing={sorted(expected-actual)}, extra={sorted(actual-expected)}")
    for row in rows:
        path = ROOT / row["path"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if row.get("sha256") != digest:
            errors.append(f"stale hash: {row['path']}")
        if row.get("status") != "passed":
            errors.append(f"not passed: {row['path']}: {row.get('detail', '')}")
        if row.get("repeats", 0) < args.min_repeats:
            errors.append(f"insufficient repeats: {row['path']}")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    scope = "incremental" if expected != full_expected else "full"
    print(f"Verified {len(rows)}/{len(expected)} current {args.profile} notebook reports ({scope}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
