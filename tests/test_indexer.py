from pathlib import Path

from zeroday.indexer import build_index, iter_source_files


def test_iter_source_files_filters_supported_extensions(tmp_path: Path) -> None:
    (tmp_path / "a.py").write_text("def x():\n    pass\n", encoding="utf-8")
    (tmp_path / "b.txt").write_text("noop", encoding="utf-8")

    files = iter_source_files(tmp_path)
    assert [f.name for f in files] == ["a.py"]


def test_iter_source_files_filters_by_language(tmp_path: Path) -> None:
    (tmp_path / "a.py").write_text("def x():\n    pass\n", encoding="utf-8")
    (tmp_path / "b.js").write_text("function y() {}", encoding="utf-8")

    files = iter_source_files(tmp_path, language="python")
    assert [f.name for f in files] == ["a.py"]


def test_build_index_parses_python_functions(tmp_path: Path) -> None:
    file = tmp_path / "mod.py"
    file.write_text("def one():\n    pass\n\ndef two():\n    pass\n", encoding="utf-8")

    idx = build_index(file)
    assert idx.language == "python"
    assert idx.function_count == 2
    assert [f.name for f in idx.functions] == ["one", "two"]
