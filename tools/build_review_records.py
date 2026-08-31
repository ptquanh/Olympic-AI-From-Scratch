"""Build the human-readable chapter review record without persisted execution reports."""

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    manifest = yaml.safe_load((ROOT / "curriculum.yml").read_text(encoding="utf-8"))
    module_markdown = len(list((ROOT / "modules").rglob("*.md")))
    public_notebooks = sum(
        1
        for chapter in manifest["chapters"]
        for path in (ROOT / chapter["path"]).glob("*.ipynb")
        if "practice" not in path.name
    )

    lines = [
        "# Review log — Technical Review Beta",
        "",
        "> Ngày review baseline: 2026-08-31 · Reviewer: Codex (AI-assisted technical review).",
        "",
        "## Phạm vi và nguyên tắc",
        "",
        f"- 41 chương, {module_markdown} file Markdown và {public_notebooks} notebook công khai theo manifest.",
        "- Ba notebook hình thức của PyTorch Fundamentals được thay bằng một lab Concept; 6 notebook `*_practice` cá nhân bị loại khỏi scope.",
        "- Static audit đọc contract, metadata, exercise/solution parity, code notes, references, source code và liên kết. Automated pass không thay learner testing.",
        "- Report JSON là CI/release artifact tạm gắn với commit, không phải nội dung version-control.",
        "",
        "## Execution policy",
        "",
        "- Baseline 2026-08-31: CPU 63/63 chạy hai lần; clean Python 3.10 CPU 63/63; local GPU full 19/19.",
        "- Pull request chỉ chạy notebook bị ảnh hưởng. Thay đổi Markdown chỉ cần static audit.",
        "- Full CPU run chạy theo lịch Chủ nhật hoặc thủ công trước release; GPU/cloud full run là release gate cho chương `gpu_full: true`.",
        "- CI artifact và commit/CI run URL là bằng chứng thực thi; không commit report JSON.",
        "",
        "## Review record 41/41",
        "",
        "| Chương | Archetype | Track | Runtime policy | Manifest status |",
        "|---|---|---|---|---|",
    ]
    for chapter in manifest["chapters"]:
        runtime_policy = "incremental CPU + scheduled full"
        if chapter["gpu_full"]:
            runtime_policy += " + release GPU/cloud"
        track = f"Foundation: {chapter['foundation']}; Contest: {chapter['contest']}"
        lines.append(
            f"| `{chapter['id']}` | {chapter['archetype']} | {track} | "
            f"{runtime_policy} | {chapter['status']} |"
        )

    lines.extend(
        [
            "",
            "## Release decision",
            "",
            "Repo mang nhãn **Technical Review Beta**, không phải Published. `learner_tested`, `revised` và `published` chỉ được cập nhật sau learner testing có người thật. Chương GPU còn `drafted` cho đến khi portability gate của release được hoàn tất.",
            "",
        ]
    )
    (ROOT / "_dev" / "review_log.md").write_text("\n".join(lines), encoding="utf-8")
    print("Built 41-chapter review log without persisted execution reports.")


if __name__ == "__main__":
    main()
