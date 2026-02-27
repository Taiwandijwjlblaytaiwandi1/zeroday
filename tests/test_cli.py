from pathlib import Path

import pytest

from zeroday import cli


def test_cli_fails_for_missing_target(monkeypatch: pytest.MonkeyPatch) -> None:
    missing = Path("/tmp/zeroday-target-does-not-exist")
    monkeypatch.setattr("sys.argv", ["zeroday", "scan", str(missing)])

    with pytest.raises(SystemExit) as exc:
        cli.main()

    assert "Target path must exist and be a directory" in str(exc.value)


def test_cli_requires_language_with_use_sample(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("sys.argv", ["zeroday", "scan", "--use-sample"])

    with pytest.raises(SystemExit) as exc:
        cli.main()

    assert "--use-sample requires --language" in str(exc.value)


def test_cli_scan_sample_python_to_file(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    output = tmp_path / "scan.json"
    monkeypatch.setattr(
        "sys.argv",
        [
            "zeroday",
            "scan",
            "--language",
            "python",
            "--use-sample",
            "--output",
            str(output),
        ],
    )

    cli.main()

    assert output.exists()
