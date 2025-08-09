from pathlib import Path

from pydantic import field_validator

from wexample_file.excpetion.file_not_found_exception import FileNotFoundException
from wexample_file.excpetion.not_a_file_exception import NotAFileException
from .abstract_local_item_path import AbstractLocalItemPath


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

    def _kind(self) -> str:
        from wexample_file.const.globals import PATH_NAME_FILE

        return PATH_NAME_FILE

    def _not_found_exc(self):
        return FileNotFoundException(self.path)
