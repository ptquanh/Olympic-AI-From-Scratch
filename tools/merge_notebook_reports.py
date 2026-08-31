"""Replace stale rows in a complete report with verified targeted reruns."""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("base")
    parser.add_argument("patches", nargs="+")
    args = parser.parse_args()
    base_path = ROOT / args.base
    base = json.loads(base_path.read_text(encoding="utf-8"))
    rows = {row["path"]: row for row in base["notebooks"]}
    merged = []
    for name in args.patches:
        patch = json.loads((ROOT / name).read_text(encoding="utf-8"))
        if patch["environment"]["profile"] != base["environment"]["profile"]:
            raise ValueError(f"profile mismatch in {name}")
        for row in patch["notebooks"]:
            if row["path"] not in rows:
                raise ValueError(f"patch path is outside base coverage: {row['path']}")
            rows[row["path"]] = row
            merged.append(row["path"])
    ordered = [rows[path] for path in sorted(rows)]
    failed = sum(row["status"] != "passed" for row in ordered)
    base["notebooks"] = ordered
    base["summary"] = {"passed": len(ordered) - failed, "total": len(ordered), "failed": failed}
    base["environment"]["targeted_reruns"] = merged
    base_path.write_text(json.dumps(base, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Merged {len(merged)} targeted rerun(s) into {base_path}.")


if __name__ == "__main__":
    main()
