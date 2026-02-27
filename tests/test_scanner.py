from pathlib import Path

from zeroday.scanner import scan_project


def test_scan_project_returns_summary_and_risk_ranking(tmp_path: Path) -> None:
    (tmp_path / "main.py").write_text(
        "import subprocess\n\ndef run(cmd):\n    return subprocess.run(cmd, shell=True)\n",
        encoding="utf-8",
    )

    output = scan_project(tmp_path)

    assert output["summary"]["scanned_files"] == 1
    assert len(output["risk_ranking"]) == 1
    assert output["risk_ranking"][0]["risk_score"] > 0
