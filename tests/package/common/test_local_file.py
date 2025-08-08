import pytest
from pathlib import Path

from wexample_file.common.local_file import LocalFile


def test_local_file_instantiation_with_str(tmp_path):
    p = tmp_path / "file.txt"
    p.write_text("hello")
    lf = LocalFile(path=str(p))
    assert isinstance(lf.path, Path)
    assert lf.path == p.resolve()


def test_local_file_instantiation_with_path_nonexistent(tmp_path):
    p = tmp_path / "missing.txt"
    assert not p.exists()
    lf = LocalFile(path=p)
    assert lf.path == p.resolve()


def test_local_file_rejects_directory(tmp_path):
    d = tmp_path / "adir"
    d.mkdir()
    with pytest.raises(ValueError):
        LocalFile(path=d)
