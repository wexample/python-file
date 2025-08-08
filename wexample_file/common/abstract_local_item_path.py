from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


class AbstractLocalItemPath(BaseModel):
    """Base class for handling local file paths with type checking capabilities."""
    path: Path = Field(description="The path to the file or directory")
    check_is_file: Optional[bool] = Field(
        default=None,
        description="If True, verify path is a file. If False, verify it's a directory. If None, accept either."
    )

    def __str__(self) -> str:
        return str(self.path)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(str(self.path))})"

    def __eq__(self, other) -> bool:
        if isinstance(other, AbstractLocalItemPath):
            return self.path == other.path
        return self.path == other
