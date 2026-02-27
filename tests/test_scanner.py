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
    assert output["summary"]["language_filter"] == "all"


def test_scan_project_language_filter_limits_files(tmp_path: Path) -> None:
    (tmp_path / "main.py").write_text("def run():\n    pass\n", encoding="utf-8")
    (tmp_path / "main.js").write_text("function run() {}", encoding="utf-8")

    output = scan_project(tmp_path, language="python")

    assert output["summary"]["scanned_files"] == 1
    assert output["risk_ranking"][0]["language"] == "python"
    assert output["summary"]["language_filter"] == "python"


def test_scan_project_rejects_invalid_language(tmp_path: Path) -> None:
    try:
        scan_project(tmp_path, language="ruby")
    except ValueError as exc:
        assert "Unsupported language" in str(exc)
    else:
        raise AssertionError("Expected ValueError for unsupported language")
