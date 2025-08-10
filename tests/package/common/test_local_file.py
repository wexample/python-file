import pytest
from pathlib import Path

from wexample_file.common.local_file import LocalFile
from wexample_file.excpetion.not_a_file_exception import NotAFileException
from wexample_file.excpetion.file_not_found_exception import FileNotFoundException


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
    with pytest.raises(NotAFileException):
        LocalFile(path=d)


def test_local_file_should_exist_true_accepts_existing_file(tmp_path):
    p = tmp_path / "exists.txt"
    p.write_text("data")
    lf = LocalFile(path=p, should_exist=True)
    assert lf.path == p.resolve()


def test_local_file_should_exist_true_rejects_missing(tmp_path):
    p = tmp_path / "missing2.txt"
    assert not p.exists()
    with pytest.raises(FileNotFoundException):
        LocalFile(path=p, should_exist=True)


def test_local_file_remove_deletes_file(tmp_path):
    p = tmp_path / "toremove.txt"
    p.write_text("data")
    lf = LocalFile(path=p, should_exist=True)
    assert p.exists()
    lf.remove()
    assert not p.exists()


def test_local_file_remove_idempotent(tmp_path):
    p = tmp_path / "missing_after_remove.txt"
    lf = LocalFile(path=p)
    # First remove on non-existent path should not raise
    lf.remove()
    assert not p.exists()
    # Create then remove, then remove again
    p.write_text("hello")
    lf2 = LocalFile(path=p, should_exist=True)
    lf2.remove()
    assert not p.exists()
    # Idempotent second call
    lf2.remove()
