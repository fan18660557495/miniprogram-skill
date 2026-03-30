#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MARKDOWN_FILES = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "references" / "styles" / "warm-enterprise.md",
]

EXPECTED_SELF_CHECK = {
    ROOT / "references" / "core" / "overview.md": "## 自检",
    ROOT / "references" / "core" / "page-flow.md": "## 页面级自检",
    ROOT / "references" / "core" / "form-and-feedback.md": "## 表单自检",
    ROOT / "references" / "core" / "voice.md": "## 语音自检",
    ROOT / "references" / "core" / "component-boundary.md": "## 自检",
    ROOT / "references" / "core" / "design-tokens.md": "## 自检",
    ROOT / "references" / "core" / "component-styles.md": "## 自检",
    ROOT / "references" / "core" / "writing.md": "## 自检",
    ROOT / "references" / "core" / "engineering.md": "## 自检",
    ROOT / "references" / "core" / "acceptance.md": "## 自检",
}

PATH_PATTERN = re.compile(r"`((?:references|assets|scripts)/[^`\s]+/?)(?=`)")
TOKEN_FILES = [
    ROOT / "assets" / "tokens" / "warm-enterprise.css",
    ROOT / "assets" / "tokens" / "warm-enterprise-semantic.css",
]


def iter_markdown_paths() -> list[Path]:
    refs: set[Path] = set()
    for file_path in MARKDOWN_FILES:
        text = file_path.read_text(encoding="utf-8")
        for match in PATH_PATTERN.findall(text):
            refs.add(ROOT / match.rstrip("/"))
    return sorted(refs)


def check_paths() -> list[str]:
    failures: list[str] = []
    for ref in iter_markdown_paths():
        if not ref.exists():
            failures.append(f"缺少引用路径: {ref}")
    return failures


def check_self_check_sections() -> list[str]:
    failures: list[str] = []
    for file_path, heading in EXPECTED_SELF_CHECK.items():
        text = file_path.read_text(encoding="utf-8")
        if heading not in text:
            failures.append(f"缺少自检段落: {file_path} -> {heading}")
    return failures


def check_token_export() -> list[str]:
    failures: list[str] = []
    export_script = ROOT / "scripts" / "export_tokens.py"
    with tempfile.TemporaryDirectory(prefix="miniapp-skill-check-") as tmp_dir:
        for token_file in TOKEN_FILES:
            result = subprocess.run(
                [
                    sys.executable,
                    str(export_script),
                    str(token_file),
                    "--output-dir",
                    tmp_dir,
                ],
                capture_output=True,
                text=True,
                cwd=ROOT,
            )
            if result.returncode != 0:
                failures.append(
                    f"token 导出失败: {token_file}\n{result.stderr.strip() or result.stdout.strip()}"
                )
                continue
            stem = token_file.stem
            json_path = Path(tmp_dir) / f"{stem}.json"
            scss_path = Path(tmp_dir) / f"{stem}.scss"
            if not json_path.exists() or not scss_path.exists():
                failures.append(f"token 导出缺少产物: {token_file}")
    return failures


def main() -> int:
    failures = []
    failures.extend(check_paths())
    failures.extend(check_self_check_sections())
    failures.extend(check_token_export())

    if failures:
        print("Skill 检查失败:")
        for item in failures:
            print(f"- {item}")
        return 1

    print("Skill 检查通过:")
    print("- 引用路径存在")
    print("- 核心文档包含自检段落")
    print("- token 导出脚本可正常运行")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
