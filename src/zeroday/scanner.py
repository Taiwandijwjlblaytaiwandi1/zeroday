from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

from .indexer import build_index, iter_source_files
from .models import Finding, detect_language
from .risk import score_file


LANGUAGE_CHOICES = {"python", "javascript", "c_family"}


def _semgrep_findings(target: Path) -> list[Finding]:
    if not shutil.which("semgrep"):
        return []

    result = subprocess.run(
        ["semgrep", "scan", "--config", "auto", "--json", str(target)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode not in {0, 1}:
        return []

    parsed = json.loads(result.stdout or "{}")
    findings: list[Finding] = []
    for i, res in enumerate(parsed.get("results", []), start=1):
        start = res.get("start", {})
        findings.append(
            Finding(
                id=f"semgrep-{i}",
                category=res.get("check_id", "semgrep"),
                path=res.get("path", ""),
                line=int(start.get("line", 1)),
                summary=res.get("extra", {}).get("message", "semgrep finding"),
                confidence=0.5,
                evidence={"tool": "semgrep"},
            )
        )
    return findings


def scan_project(target: Path, language: str | None = None) -> dict:
    if language and language not in LANGUAGE_CHOICES:
        raise ValueError(f"Unsupported language: {language}")

    indexes = [build_index(path) for path in iter_source_files(target, language=language)]
    risk_ranked = sorted(
        (
            {
                "path": idx.path,
                "language": idx.language,
                "line_count": idx.line_count,
                "function_count": idx.function_count,
                "risk_score": score_file(idx),
            }
            for idx in indexes
        ),
        key=lambda r: r["risk_score"],
        reverse=True,
    )
    findings = [f.to_dict() for f in _semgrep_findings(target)]
    if language:
        findings = [
            f
            for f in findings
            if f.get("path") and detect_language(Path(f["path"])) == language
        ]

    return {
        "summary": {
            "scanned_files": len(indexes),
            "findings": len(findings),
            "language_filter": language or "all",
        },
        "risk_ranking": risk_ranked,
        "findings": findings,
    }

