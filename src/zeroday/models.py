from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path


@dataclass(slots=True)
class FunctionRef:
    name: str
    line: int


@dataclass(slots=True)
class FileIndex:
    path: str
    language: str
    line_count: int
    function_count: int
    functions: list[FunctionRef] = field(default_factory=list)


@dataclass(slots=True)
class Finding:
    id: str
    category: str
    path: str
    line: int
    summary: str
    confidence: float
    evidence: dict[str, str]

    def to_dict(self) -> dict:
        return asdict(self)


def detect_language(path: Path) -> str:
    ext = path.suffix.lower()
    if ext == ".py":
        return "python"
    if ext in {".js", ".ts"}:
        return "javascript"
    if ext in {".c", ".h", ".cpp", ".cc", ".hpp"}:
        return "c_family"
    return "unknown"
