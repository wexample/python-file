import pytest
from pathlib import Path

from wexample_file.common.local_directory import LocalDirectory


def test_local_directory_instantiation_with_str(tmp_path):
    d = tmp_path / "adir"
    d.mkdir()
    ld = LocalDirectory(path=str(d))
    assert isinstance(ld.path, Path)
    assert ld.path == d.resolve()


def test_local_directory_instantiation_with_path_nonexistent(tmp_path):
    d = tmp_path / "missing_dir"
    assert not d.exists()
    ld = LocalDirectory(path=d)
    assert ld.path == d.resolve()


def test_local_directory_rejects_file(tmp_path):
    f = tmp_path / "afile.txt"
    f.write_text("hello")
    with pytest.raises(ValueError):
        LocalDirectory(path=f)
