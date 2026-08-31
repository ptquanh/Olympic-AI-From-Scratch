"""Static quality gates for Olympic AI From Scratch.

The audit is intentionally dependency-light apart from PyYAML. It never edits
course files. Exit code 1 means at least one release-blocking error.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "curriculum.yml"
VALID_ARCHETYPES = {"core", "concept", "competition"}
VALID_STATUSES = {
    "outlined",
    "drafted",
    "technically_reviewed",
    "learner_tested",
    "revised",
    "published",
}
EXPECTED_FILES = {
    "core": {
        "README.md",
        "01_from_scratch.ipynb",
        "02_framework.ipynb",
        "03_experiments.ipynb",
        "code_notes.md",
        "exercises.md",
        "solutions.md",
        "olympiad_transfer.md",
        "references.md",
    },
    "concept": {
        "README.md",
        "lab.ipynb",
        "code_notes.md",
        "exercises.md",
        "solutions.md",
        "references.md",
    },
    "competition": {
        "README.md",
        "starter.ipynb",
        "solution.ipynb",
        "code_notes.md",
        "rubric.md",
        "postmortem.md",
        "references.md",
    },
}
NOTEBOOK_FIELDS = ("Runtime:", "Hardware:", "Network:", "Competition-safe:")
FORBIDDEN_NOTEBOOK_PATTERNS = {
    "automatic package installation": re.compile(
        r"(?:pip|conda)\s+install|subprocess\.(?:check_call|run|call).*install",
        re.IGNORECASE | re.DOTALL,
    ),
    "repository cloning": re.compile(r"git\s+clone", re.IGNORECASE),
    "absolute home path": re.compile(r"(?:/home/|[A-Za-z]:\\\\)"),
}
FRAMEWORK_IMPORTS = {"torch", "torchvision", "sklearn", "transformers", "tensorflow", "jax"}
IMPORT_TO_PACKAGE = {"cv2": "opencv-python", "PIL": "pillow", "sklearn": "scikit-learn", "yaml": "pyyaml"}
EXERCISE_ID = re.compile(r"\b([UIETO]-\d+)\b")
EXERCISE_BLOCK = re.compile(r"(^## ([UIETO]-\d+)\b.*?)(?=^## [UIETO]-\d+\b|\Z)", re.MULTILINE | re.DOTALL)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


@dataclass
class Finding:
    level: str
    location: str
    message: str


class Audit:
    def __init__(self) -> None:
        self.findings: list[Finding] = []

    def error(self, location: Path | str, message: str) -> None:
        self.findings.append(Finding("ERROR", self._relative(location), message))

    def warning(self, location: Path | str, message: str) -> None:
        self.findings.append(Finding("WARN", self._relative(location), message))

    @staticmethod
    def _relative(location: Path | str) -> str:
        if isinstance(location, Path):
            try:
                return location.resolve().relative_to(ROOT).as_posix()
            except ValueError:
                return str(location)
        return location


def load_manifest(audit: Audit) -> list[dict]:
    try:
        data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - startup guard
        audit.error(MANIFEST, f"cannot parse YAML: {exc}")
        return []
    chapters = data.get("chapters", [])
    profile_data = data.get("competition_profiles", {})
    profiles = set(profile_data)
    for profile_id, profile in profile_data.items():
        if re.search(r"_\d{4}$", profile_id):
            if not profile.get("verified"):
                audit.error(MANIFEST, f"{profile_id}: year-specific profile needs verified date")
            if not any(key.endswith("source") for key in profile):
                audit.error(MANIFEST, f"{profile_id}: year-specific profile needs an official source")
    if len(chapters) != 41:
        audit.error(MANIFEST, f"expected 41 chapters, found {len(chapters)}")
    ids = [c.get("id") for c in chapters]
    paths = [c.get("path") for c in chapters]
    if len(ids) != len(set(ids)):
        audit.error(MANIFEST, "chapter ids must be unique")
    if len(paths) != len(set(paths)):
        audit.error(MANIFEST, "chapter paths must be unique")
    known = set(ids)
    for chapter in chapters:
        cid = chapter.get("id", "<missing-id>")
        archetype = chapter.get("archetype")
        status = chapter.get("status")
        if archetype not in VALID_ARCHETYPES:
            audit.error(MANIFEST, f"{cid}: invalid archetype {archetype!r}")
        if status not in VALID_STATUSES:
            audit.error(MANIFEST, f"{cid}: invalid status {status!r}")
        for dependency in chapter.get("prerequisites", []):
            if dependency not in known:
                audit.error(MANIFEST, f"{cid}: unknown prerequisite {dependency}")
        if chapter.get("network") not in {"none", "optional", "required_first_run"}:
            audit.error(MANIFEST, f"{cid}: invalid network profile")
        unknown_profiles = set(chapter.get("profiles", [])) - profiles
        if unknown_profiles:
            audit.error(MANIFEST, f"{cid}: unknown competition profile(s): {sorted(unknown_profiles)}")
        for field in ("foundation", "contest", "cpu_smoke", "gpu_full", "profiles"):
            if field not in chapter:
                audit.error(MANIFEST, f"{cid}: missing manifest field {field}")
    return chapters


def check_chapter(audit: Audit, chapter: dict) -> None:
    path = ROOT / chapter["path"]
    if not path.is_dir():
        audit.error(path, "chapter directory is missing")
        return
    present = {item.name for item in path.iterdir() if item.is_file()}
    missing = EXPECTED_FILES[chapter["archetype"]] - present
    for name in sorted(missing):
        audit.error(path, f"missing required {chapter['archetype']} file: {name}")

    readme = path / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        required = ("Prerequisite", "Learning Outcomes", "Concept Map", "Intuition", "Time Estimate")
        if chapter["archetype"] == "competition":
            required = ("Learning Outcomes", "Metric", "Validation", "Time Estimate")
        for heading in required:
            if heading.lower() not in text.lower():
                audit.error(readme, f"missing learner-journey section containing {heading!r}")
        if "**Track:**" not in text:
            audit.error(readme, "missing standardized Track line")

    if chapter["archetype"] in {"core", "concept"}:
        exercises = path / "exercises.md"
        solutions = path / "solutions.md"
        if exercises.exists() and solutions.exists():
            exercise_text = exercises.read_text(encoding="utf-8")
            exercise_ids = EXERCISE_ID.findall(exercise_text)
            solution_ids = EXERCISE_ID.findall(solutions.read_text(encoding="utf-8"))
            expected_prefixes = {"U", "I", "E"}
            if chapter["archetype"] == "core":
                expected_prefixes |= {"T", "O"}
            actual_prefixes = {item[0] for item in exercise_ids}
            for prefix in expected_prefixes - actual_prefixes:
                audit.error(exercises, f"missing exercise tier {prefix}")
            if not exercise_ids:
                audit.error(exercises, "no stable U/I/E/T/O exercise ids")
            if sorted(exercise_ids) != sorted(solution_ids):
                audit.error(solutions, "exercise and solution ids do not match 1:1")
            if "Expected output" not in exercise_text and "Kết quả mong đợi" not in exercise_text:
                audit.error(exercises, "missing explicit expected outputs")
            blocks = EXERCISE_BLOCK.findall(exercise_text)
            if len(blocks) != len(set(exercise_ids)):
                audit.error(exercises, "every stable exercise id must own exactly one question block")
            for block, exercise_id in blocks:
                if "**Learning outcome:**" not in block:
                    audit.error(exercises, f"{exercise_id}: missing explicit learning-outcome mapping")
                if "Expected output" not in block and "Kết quả mong đợi" not in block:
                    audit.error(exercises, f"{exercise_id}: missing expected output in its own block")
            solution_text = solutions.read_text(encoding="utf-8")
            if solution_text.count("<details") < len(set(solution_ids)):
                audit.error(solutions, "each solution id must be hidden in its own <details>")
            if solution_text.count("Lỗi thường gặp:") < len(set(solution_ids)):
                audit.error(solutions, "each solution id must document a common mistake")
            if "```" not in solution_text:
                audit.error(solutions, "solutions must include at least one runnable code example")

        code_notes = path / "code_notes.md"
        if code_notes.exists():
            note_text = code_notes.read_text(encoding="utf-8")
            for section in ("Core Patterns", "API Cheat Sheet", "Code Tay", "Flashcards"):
                if section.lower() not in note_text.lower():
                    audit.error(code_notes, f"missing code-notes section containing {section!r}")

        transfer = path / "olympiad_transfer.md"
        if chapter["archetype"] == "core" and transfer.exists():
            transfer_text = transfer.read_text(encoding="utf-8")
            if "Profile áp dụng" not in transfer_text and "Profile mặc định" not in transfer_text:
                audit.error(transfer, "missing explicit competition-profile scope")

    references = path / "references.md"
    if references.exists():
        reference_text = references.read_text(encoding="utf-8")
        if len(re.findall(r"https?://", reference_text)) < 3:
            audit.error(references, "fewer than three direct external references")

    for notebook in path.glob("*.ipynb"):
        if "practice" not in notebook.name:
            check_notebook(audit, notebook, chapter)

    if chapter["gpu_full"]:
        torch_notebooks = 0
        for notebook in path.glob("*.ipynb"):
            if "practice" in notebook.name:
                continue
            _, _, source = notebook_source(notebook)
            if re.search(r"(?:^|\n)\s*(?:import torch|from torch)", source):
                torch_notebooks += 1
        if torch_notebooks == 0:
            audit.error(path, "gpu_full chapter has no PyTorch notebook to exercise the GPU")


def notebook_source(path: Path) -> tuple[dict, str, str]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    cells = notebook.get("cells", [])
    all_source = "\n".join("".join(c.get("source", [])) for c in cells)
    code_source = "\n".join(
        "".join(c.get("source", [])) for c in cells if c.get("cell_type") == "code"
    )
    return notebook, all_source, code_source


def declared_packages() -> set[str]:
    result = set()
    for name in ("requirements.txt", "requirements-optional.txt", "requirements-dev.txt"):
        for raw in (ROOT / name).read_text(encoding="utf-8").splitlines():
            line = raw.split("#", 1)[0].strip()
            if not line or line.startswith("-"):
                continue
            result.add(re.split(r"[<>=!~\[]", line, maxsplit=1)[0].lower())
    return result


DECLARED_PACKAGES = declared_packages()


def check_notebook(audit: Audit, path: Path, chapter: dict) -> None:
    try:
        notebook, all_source, code_source = notebook_source(path)
    except Exception as exc:
        audit.error(path, f"invalid notebook JSON: {exc}")
        return
    cells = notebook.get("cells", [])
    code_cells = [c for c in cells if c.get("cell_type") == "code"]
    if not code_cells:
        audit.error(path, "no code cells")
        return
    setup = "".join(code_cells[0].get("source", []))
    if "# === Setup ===" not in setup:
        audit.error(path, "first code cell must start with '# === Setup ==='")
    for field in NOTEBOOK_FIELDS:
        if field not in setup:
            audit.error(path, f"setup cell missing {field}")
    if "OAI_FAST_MODE" not in setup:
        audit.error(path, "setup cell does not support OAI_FAST_MODE")
    if not any(seed in setup for seed in ("seed(42)", "manual_seed(42)")):
        audit.error(path, "setup cell does not set seed 42")
    if chapter["gpu_full"] and re.search(r"(?:^|\n)\s*(?:import torch|from torch)", code_source):
        for token in ("OAI_RUNTIME_PROFILE", "DEVICE", "torch.set_default_device"):
            if token not in setup:
                audit.error(path, f"GPU notebook setup missing {token}")
    for label, pattern in FORBIDDEN_NOTEBOOK_PATTERNS.items():
        if pattern.search(code_source):
            audit.error(path, f"forbidden notebook behavior: {label}")
    try:
        compile(code_source, str(path), "exec")
    except SyntaxError as exc:
        audit.error(path, f"code-cell syntax error at combined line {exc.lineno}: {exc.msg}")

    try:
        tree = ast.parse(code_source)
        imports = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split(".")[0])
        undeclared = []
        for module in imports - sys.stdlib_module_names:
            package = IMPORT_TO_PACKAGE.get(module, module).lower()
            if package not in DECLARED_PACKAGES:
                undeclared.append(module)
        if undeclared:
            audit.error(path, f"undeclared notebook dependency import(s): {', '.join(sorted(undeclared))}")
    except SyntaxError:
        pass

    if path.name == "01_from_scratch.ipynb":
        if "assert " not in code_source:
            audit.error(path, "from-scratch core algorithm must include executable assertions")
        try:
            tree = ast.parse(code_source)
            imports = set()
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imports.update(alias.name.split(".")[0] for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split(".")[0])
            forbidden = sorted(imports & FRAMEWORK_IMPORTS)
            if forbidden:
                audit.error(path, f"from-scratch imports framework(s): {', '.join(forbidden)}")
        except SyntaxError:
            pass
    if path.name == "02_framework.ipynb" and "assert " not in code_source:
        audit.error(path, "framework notebook must assert shapes/metrics against its reference behavior")


def strip_code_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def check_local_links(audit: Audit) -> None:
    candidates = [
        ROOT / "README.md",
        ROOT / "HOW_TO_STUDY.md",
        ROOT / "SETUP.md",
        ROOT / "PROGRESS_TRACKER.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "COMPETITION_PROFILES.md",
        ROOT / "THIRD_PARTY_NOTICES.md",
        ROOT / "CHANGELOG.md",
    ]
    candidates.extend((ROOT / "modules").rglob("*.md"))
    for path in candidates:
        text = strip_code_fences(path.read_text(encoding="utf-8"))
        for raw_target in MARKDOWN_LINK.findall(text):
            target = unquote(raw_target.strip().split("#", 1)[0])
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                audit.error(path, f"broken local link: {raw_target}")


def tracked_notebooks() -> set[str]:
    output = subprocess.check_output(
        ["git", "ls-files", "*.ipynb"], cwd=ROOT, text=True, encoding="utf-8"
    )
    return {line.replace("\\", "/") for line in output.splitlines() if line}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit machine-readable findings")
    parser.add_argument("--strict-git", action="store_true", help="warn when manifest notebooks are not tracked")
    args = parser.parse_args()
    audit = Audit()
    chapters = load_manifest(audit)
    for chapter in chapters:
        check_chapter(audit, chapter)
    check_local_links(audit)

    manifest_notebooks = {
        path.relative_to(ROOT).as_posix()
        for chapter in chapters
        for path in (ROOT / chapter["path"]).glob("*.ipynb")
        if "practice" not in path.name
    }
    if args.strict_git:
        untracked_scope = manifest_notebooks - tracked_notebooks()
        for path in sorted(untracked_scope):
            audit.warning(path, "notebook is in curriculum scope but not tracked by git")

    if args.json:
        print(json.dumps([finding.__dict__ for finding in audit.findings], ensure_ascii=False, indent=2))
    else:
        for finding in audit.findings:
            print(f"{finding.level}: {finding.location}: {finding.message}")
        errors = sum(f.level == "ERROR" for f in audit.findings)
        warnings = sum(f.level == "WARN" for f in audit.findings)
        print(f"\nAudit summary: {errors} error(s), {warnings} warning(s), {len(chapters)} chapter(s).")
    return 1 if any(f.level == "ERROR" for f in audit.findings) else 0


if __name__ == "__main__":
    sys.exit(main())
