from pathlib import Path

from pydantic import field_validator

from .abstract_local_item_path import AbstractLocalItemPath
from wexample_file.excpetion.file_not_found_exception import FileNotFoundException
from wexample_file.excpetion.not_a_file_exception import NotAFileException


class LocalFile(AbstractLocalItemPath):
    """Represents a local file path.

    The path is stored as a resolved absolute Path. If the path exists, it must
    be a file.
    """

    @field_validator("path")
    @classmethod
    def _validate_is_file(cls, v: Path) -> Path:
        # Only validate type when it exists; creation workflows may pass a non-existent path
        if v.exists() and not v.is_file():
            raise NotAFileException(v)
        return v

    @field_validator("path")
    @classmethod
    def _validate_existence_when_required(cls, v: Path, info):
        # If should_exist is True, ensure file exists (complementary to base model check)
        # Access to other fields via info.data (pydantic v2), default False if not present yet
        should_exist = bool(info.data.get("should_exist")) if hasattr(info, "data") else False
        if should_exist and not v.exists():
            raise FileNotFoundException(v)
        return v

    def _kind(self) -> str:
        from wexample_file.const.globals import PATH_NAME_FILE

        return PATH_NAME_FILE

    def _not_found_exc(self):
        return FileNotFoundException(self.path)
