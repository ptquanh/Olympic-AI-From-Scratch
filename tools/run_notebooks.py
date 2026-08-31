"""Execute tracked curriculum notebooks without modifying source files."""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
import time
from pathlib import Path

import nbformat
import yaml
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError, CellTimeoutError
from jupyter_client.kernelspec import KernelSpecManager


ROOT = Path(__file__).resolve().parents[1]
NUMBER = re.compile(r"(?<![\w.])[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?")
FULL_RUN_FILES = {
    "constraints-py310.txt",
    "environment.yml",
    "environment-gpu.yml",
    "requirements.txt",
    "requirements-dev.txt",
    "requirements-contest.txt",
    "requirements-optional.txt",
    "tools/run_notebooks.py",
}


@contextlib.contextmanager
def working_directory(path: Path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def curriculum_notebooks() -> list[Path]:
    """Return notebooks in manifest chapter paths, including newly created files."""
    data = yaml.safe_load((ROOT / "curriculum.yml").read_text(encoding="utf-8"))
    paths = []
    for chapter in data["chapters"]:
        paths.extend(
            path for path in (ROOT / chapter["path"]).glob("*.ipynb") if "practice" not in path.name
        )
    return sorted(paths)


def manifest_metadata() -> dict[Path, dict]:
    data = yaml.safe_load((ROOT / "curriculum.yml").read_text(encoding="utf-8"))
    result: dict[Path, dict] = {}
    for chapter in data["chapters"]:
        chapter_path = (ROOT / chapter["path"]).resolve()
        result[chapter_path] = chapter
    return result


def select_changed_notebooks(
    notebooks: list[Path], metadata: dict[Path, dict], reference: str
) -> tuple[list[Path], str]:
    """Select notebooks affected since a Git reference; fall back to full when uncertain."""
    if not reference or set(reference) == {"0"}:
        return notebooks, "full"
    try:
        output = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=ACMRD", reference, "--"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"WARNING: cannot resolve incremental scope ({exc}); running the full profile.")
        return notebooks, "full"

    changed = {line.strip().replace("\\", "/") for line in output.splitlines() if line.strip()}
    if changed & FULL_RUN_FILES:
        return notebooks, "full"

    current = {path.relative_to(ROOT).as_posix(): path for path in notebooks}
    selected = {current[path] for path in changed if path in current}
    chapter_paths = {
        chapter_path.relative_to(ROOT).as_posix(): chapter_path for chapter_path in metadata
    }
    for changed_path in changed:
        # Markdown-only curriculum edits are covered by the static audit. Runtime support files
        # inside a chapter invalidate every public notebook in that chapter.
        if Path(changed_path).suffix.lower() in {".md", ".ipynb"}:
            continue
        for relative_chapter, chapter_path in chapter_paths.items():
            if changed_path.startswith(relative_chapter + "/"):
                selected.update(path for path in notebooks if path.parent.resolve() == chapter_path)
                break
    return sorted(selected), "changed"


def numeric_signature(notebook: dict) -> list[float]:
    """Extract stable numeric stdout/result tokens; ignore plots and memory addresses."""
    values: list[float] = []
    for cell in notebook.get("cells", []):
        for output in cell.get("outputs", []):
            chunks: list[str] = []
            if output.get("output_type") == "stream":
                value = output.get("text", "")
                chunks.append("".join(value) if isinstance(value, list) else value)
            elif output.get("output_type") in {"execute_result", "display_data"}:
                value = output.get("data", {}).get("text/plain", "")
                chunks.append("".join(value) if isinstance(value, list) else value)
            for chunk in chunks:
                for line in chunk.splitlines():
                    lowered = line.lower()
                    if "0x" in line or any(token in lowered for token in ("seconds", "runtime", "time:", " ms")):
                        continue
                    values.extend(float(token) for token in NUMBER.findall(line))
    return [value for value in values if math.isfinite(value)]


def signatures_close(left: list[float], right: list[float], *, rtol: float, atol: float) -> bool:
    return len(left) == len(right) and all(
        math.isclose(a, b, rel_tol=rtol, abs_tol=atol) for a, b in zip(left, right)
    )


def kernel_environment(kernel_name: str) -> dict:
    """Query the interpreter named by the kernelspec, not merely the runner process."""
    try:
        spec = KernelSpecManager().get_kernel_spec(kernel_name)
        executable = spec.argv[0]
        probe = (
            "import json,sys; versions={}; "
            "mods=['numpy','pandas','sklearn','torch','torchvision','transformers']; "
            "exec(\"for name in mods:\\n try:\\n  m=__import__(name); versions[name]=getattr(m,'__version__','unknown')\\n except Exception as e:\\n  versions[name]='missing:'+type(e).__name__\"); "
            "print(json.dumps({'python':sys.version,'versions':versions}))"
        )
        output = subprocess.check_output([executable, "-c", probe], text=True, encoding="utf-8")
        return json.loads(output)
    except Exception as exc:
        return {"probe_error": f"{type(exc).__name__}: {exc}"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast", action="store_true")
    parser.add_argument("--profile", choices=("cpu", "gpu"), default="cpu")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--gpu-only", action="store_true", help="only chapters whose gpu_full gate is true")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--kernel-name", default="python3")
    parser.add_argument("--match", help="only execute paths containing this text")
    parser.add_argument(
        "--changed-since",
        help="execute only notebooks affected since this Git ref; shared runtime changes run all",
    )
    parser.add_argument("--max", type=int, help="execute at most N notebooks")
    parser.add_argument("--repeats", type=int, default=1, choices=range(1, 4))
    parser.add_argument("--rtol", type=float, default=1e-5)
    parser.add_argument("--atol", type=float, default=1e-7)
    parser.add_argument("--report", default="_dev/notebook_report.json")
    args = parser.parse_args()

    if args.profile == "gpu":
        try:
            import torch
        except ImportError as exc:
            parser.error(f"GPU profile requires PyTorch: {exc}")
        if not torch.cuda.is_available():
            parser.error("GPU profile requested but torch.cuda.is_available() is false")

    if args.fast:
        os.environ["OAI_FAST_MODE"] = "1"
    os.environ["OAI_RUNTIME_PROFILE"] = args.profile
    if args.offline:
        os.environ.update(
            {
                "OAI_OFFLINE": "1",
                "HF_HUB_OFFLINE": "1",
                "TRANSFORMERS_OFFLINE": "1",
            }
        )

    metadata = manifest_metadata()
    notebooks = curriculum_notebooks()
    if args.gpu_only:
        notebooks = [path for path in notebooks if metadata[path.parent.resolve()]["gpu_full"]]
    if args.match:
        notebooks = [path for path in notebooks if args.match in path.as_posix()]
    selection_mode = "filtered" if args.match or args.max is not None else "full"
    if args.changed_since:
        notebooks, selection_mode = select_changed_notebooks(notebooks, metadata, args.changed_since)
    if args.max is not None:
        notebooks = notebooks[: args.max]

    selected_notebooks = [path.relative_to(ROOT).as_posix() for path in notebooks]
    print(f"Notebook selection: {selection_mode} ({len(notebooks)} notebook(s)).", flush=True)

    report = []
    failures = 0
    for path in notebooks:
        relative = path.relative_to(ROOT).as_posix()
        chapter = metadata.get(path.parent.resolve(), {})
        network = chapter.get("network", "unknown")
        start = time.perf_counter()
        repeat_seconds: list[float] = []
        signatures: list[list[float]] = []
        try:
            for _ in range(args.repeats):
                repeat_start = time.perf_counter()
                notebook = nbformat.read(path, as_version=4)
                client = NotebookClient(
                    notebook,
                    timeout=args.timeout,
                    kernel_name=args.kernel_name,
                    resources={"metadata": {"path": str(path.parent)}},
                    allow_errors=False,
                )
                with working_directory(path.parent):
                    client.execute()
                repeat_seconds.append(round(time.perf_counter() - repeat_start, 3))
                signatures.append(numeric_signature(notebook))
            reproducible = all(
                signatures_close(signatures[0], signature, rtol=args.rtol, atol=args.atol)
                for signature in signatures[1:]
            )
            if not reproducible:
                raise AssertionError(
                    f"numeric output differs across repeats beyond rtol={args.rtol}, atol={args.atol}"
                )
            status = "passed"
            detail = ""
        except (CellExecutionError, CellTimeoutError, Exception) as exc:
            status = "failed"
            detail = f"{type(exc).__name__}: {exc}"
            failures += 1
        elapsed = round(time.perf_counter() - start, 3)
        report.append(
            {
                "path": relative,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "status": status,
                "seconds": elapsed,
                "repeat_seconds": repeat_seconds,
                "repeats": args.repeats,
                "numeric_signature_size": len(signatures[0]) if signatures else 0,
                "network": network,
                "detail": detail,
            }
        )
        print(f"{status.upper():6} {elapsed:8.3f}s {relative}", flush=True)

    report_path = ROOT / args.report
    report_path.parent.mkdir(parents=True, exist_ok=True)
    kernel = {"skipped": "no notebooks selected"}
    if not notebooks:
        cuda_available = False
        torch_version = None
        gpu_name = None
    else:
        kernel = kernel_environment(args.kernel_name)
        try:
            import torch

            cuda_available = torch.cuda.is_available()
            torch_version = torch.__version__
            gpu_name = torch.cuda.get_device_name(0) if cuda_available else None
        except ImportError:
            cuda_available = False
            torch_version = None
            gpu_name = None
    payload = {
        "environment": {
            "profile": args.profile,
            "fast_mode": args.fast,
            "offline": args.offline,
            "python": sys.version,
            "platform": platform.platform(),
            "torch": torch_version,
            "cuda_available": cuda_available,
            "gpu": gpu_name,
            "repeats": args.repeats,
            "rtol": args.rtol,
            "atol": args.atol,
            "kernel_name": args.kernel_name,
            "kernel": kernel,
            "selection_mode": selection_mode,
            "changed_since": args.changed_since,
            "selected_notebooks": selected_notebooks,
        },
        "summary": {"passed": len(notebooks) - failures, "total": len(notebooks), "failed": failures},
        "notebooks": report,
    }
    report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nNotebook summary: {len(notebooks) - failures}/{len(notebooks)} passed. Report: {report_path}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
