"""Promote only chapters whose required local/cloud execution evidence is current."""

import argparse
import hashlib
import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def report_rows(name: str) -> dict[str, dict]:
    path = ROOT / "_dev" / name
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {row["path"]: row for row in payload.get("notebooks", [])}


def chapter_evidence(chapter: dict, reports: list[dict[str, dict]]) -> bool:
    notebooks = [
        path
        for path in (ROOT / chapter["path"]).glob("*.ipynb")
        if "practice" not in path.name
    ]
    for report in reports:
        for path in notebooks:
            relative = path.relative_to(ROOT).as_posix()
            row = report.get(relative)
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if not row or row.get("status") != "passed" or row.get("sha256") != digest:
                return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    manifest_path = ROOT / "curriculum.yml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    cpu = report_rows("cpu_repro_report.json")
    clean = report_rows("cpu_py310_report.json")
    gpu = report_rows("gpu_local_report.json")
    cloud = report_rows("gpu_cloud_report.json")

    promotable = set()
    blocked = {}
    for chapter in manifest["chapters"]:
        if not chapter_evidence(chapter, [cpu, clean]):
            blocked[chapter["id"]] = "CPU/clean-Python evidence missing, failed or stale"
            continue
        if chapter["gpu_full"]:
            if not chapter_evidence(chapter, [gpu]):
                blocked[chapter["id"]] = "local GPU evidence missing, failed or stale"
                continue
            if not cloud or not chapter_evidence(chapter, [cloud]):
                blocked[chapter["id"]] = "Colab/Kaggle GPU evidence pending"
                continue
        promotable.add(chapter["id"])

    print(f"Promotable: {len(promotable)}; blocked: {len(blocked)}")
    for chapter_id, reason in blocked.items():
        print(f"- {chapter_id}: {reason}")
    if not args.apply:
        return

    lines = manifest_path.read_text(encoding="utf-8").splitlines(keepends=True)
    current_id = None
    changed = 0
    for index, line in enumerate(lines):
        match = re.match(r"\s+id:\s*([^,\s]+)", line)
        if match:
            current_id = match.group(1)
        if current_id in promotable and re.match(r"\s+status:\s*drafted", line):
            lines[index] = line.replace("status: drafted", "status: technically_reviewed")
            changed += 1
    manifest_path.write_text("".join(lines), encoding="utf-8")
    print(f"Updated {changed} manifest status field(s).")


if __name__ == "__main__":
    main()
