from __future__ import annotations

from pathlib import Path

from .models import FileIndex

HIGH_RISK_KEYWORDS = [
    "eval(",
    "exec(",
    "pickle.loads",
    "subprocess",
    "system(",
    "strcpy(",
    "memcpy(",
]


def score_file(index: FileIndex) -> float:
    score = 0.0
    score += min(index.function_count * 0.5, 10.0)
    score += min(index.line_count / 200.0, 10.0)

    try:
        content = Path(index.path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return round(score, 2)

    for keyword in HIGH_RISK_KEYWORDS:
        if keyword in content:
            score += 2.5

    if index.language == "c_family":
        score += 2.0

    return round(min(score, 25.0), 2)
