from __future__ import annotations

import ast
import re
from pathlib import Path

from .models import FileIndex, FunctionRef, detect_language

FUNC_PATTERNS = {
    "javascript": re.compile(r"\bfunction\s+([a-zA-Z0-9_]+)\s*\("),
    "c_family": re.compile(
        r"^\s*[a-zA-Z_][a-zA-Z0-9_\s\*]+\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^;]*\)\s*\{"  # noqa: E501
    ),
}

IGNORE_DIRS = {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"}


def iter_source_files(root: Path, language: str | None = None) -> list[Path]:
    files: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if any(part in IGNORE_DIRS for part in p.parts):
            continue
        detected = detect_language(p)
        if detected == "unknown":
            continue
        if language and detected != language:
            continue
        files.append(p)
    return sorted(files)


def _parse_python_functions(content: str) -> list[FunctionRef]:
    tree = ast.parse(content)
    refs: list[FunctionRef] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            refs.append(FunctionRef(name=node.name, line=node.lineno))
    return sorted(refs, key=lambda x: x.line)


def _parse_regex_functions(content: str, language: str) -> list[FunctionRef]:
    refs: list[FunctionRef] = []
    pattern = FUNC_PATTERNS[language]
    for i, line in enumerate(content.splitlines(), start=1):
        m = pattern.search(line)
        if m:
            refs.append(FunctionRef(name=m.group(1), line=i))
    return refs


def build_index(path: Path) -> FileIndex:
    language = detect_language(path)
    content = path.read_text(encoding="utf-8", errors="ignore")
    if language == "python":
        try:
            functions = _parse_python_functions(content)
        except SyntaxError:
            functions = []
    elif language in FUNC_PATTERNS:
        functions = _parse_regex_functions(content, language)
    else:
        functions = []

    line_count = len(content.splitlines())
    return FileIndex(
        path=str(path),
        language=language,
        line_count=line_count,
        function_count=len(functions),
        functions=functions,
    )
