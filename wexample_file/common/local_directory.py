from pathlib import Path

from pydantic import field_validator

from .abstract_local_item_path import AbstractLocalItemPath


class LocalDirectory(AbstractLocalItemPath):
    """Represents a local directory path.

    The path is stored as a resolved absolute Path. If the path exists, it must
    be a directory.
    """

    @field_validator("path")
    @classmethod
    def _validate_is_dir(cls, v: Path) -> Path:
        if v.exists() and not v.is_dir():
            raise ValueError(f"Path is not a directory: {v}")
        return v

    def _kind(self) -> str:
        from wexample_file.const.globals import PATH_NAME_DIRECTORY

        return PATH_NAME_DIRECTORY
