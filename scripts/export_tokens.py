#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


TOKEN_PATTERN = re.compile(r"^\s*(--[A-Za-z0-9_-]+)\s*:\s*(.+?)\s*;\s*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="把 CSS token 文件导出为 JSON 和 SCSS。"
    )
    parser.add_argument("input", help="输入的 CSS token 文件路径")
    parser.add_argument(
        "--output-dir",
        help="输出目录。默认输出到输入文件所在目录。",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="同时将 JSON 输出到标准输出。",
    )
    return parser.parse_args()


def parse_tokens(css_text: str) -> dict[str, str]:
    tokens: dict[str, str] = {}
    for line in css_text.splitlines():
        match = TOKEN_PATTERN.match(line)
        if not match:
            continue
        name, value = match.groups()
        tokens[name] = value
    return tokens


def to_scss(tokens: dict[str, str]) -> str:
    lines = [f"${name[2:]}: {value};" for name, value in tokens.items()]
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"未找到输入文件：{input_path}", file=sys.stderr)
        return 1

    css_text = input_path.read_text(encoding="utf-8")
    tokens = parse_tokens(css_text)
    if not tokens:
        print("未解析到任何 CSS 变量", file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir).resolve() if args.output_dir else input_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    stem = input_path.stem
    json_path = output_dir / f"{stem}.json"
    scss_path = output_dir / f"{stem}.scss"

    json_text = json.dumps(tokens, ensure_ascii=False, indent=2) + "\n"
    scss_text = to_scss(tokens)

    json_path.write_text(json_text, encoding="utf-8")
    scss_path.write_text(scss_text, encoding="utf-8")

    print(f"已导出 JSON：{json_path}")
    print(f"已导出 SCSS：{scss_path}")

    if args.stdout:
        print(json_text, end="")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
