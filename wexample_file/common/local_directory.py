from pathlib import Path

from pydantic import field_validator

from .abstract_local_item_path import AbstractLocalItemPath
from wexample_file.excpetion.directory_not_found_exception import DirectoryNotFoundException
from wexample_file.excpetion.not_a_directory_exception import NotADirectoryException


class LocalDirectory(AbstractLocalItemPath):
    """Represents a local directory path.

    The path is stored as a resolved absolute Path. If the path exists, it must
    be a directory.
    """

    @field_validator("path")
    @classmethod
    def _validate_is_dir(cls, v: Path) -> Path:
        if v.exists() and not v.is_dir():
            raise NotADirectoryException(v)
        return v

    @field_validator("path")
    @classmethod
    def _validate_existence_when_required(cls, v: Path, info):
        should_exist = bool(info.data.get("should_exist")) if hasattr(info, "data") else False
        if should_exist and not v.exists():
            raise DirectoryNotFoundException(v)
        return v

    def _kind(self) -> str:
        from wexample_file.const.globals import PATH_NAME_DIRECTORY

        return PATH_NAME_DIRECTORY

    def _not_found_exc(self):
        return DirectoryNotFoundException(self.path)
