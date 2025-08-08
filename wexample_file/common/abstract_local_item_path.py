from abc import ABC, abstractmethod
from pathlib import Path

from pydantic import BaseModel, Field, field_validator


class AbstractLocalItemPath(BaseModel, ABC):
    """Abstract base class for handling local file system paths.

    Accepts either a string or a pathlib.Path for ``path`` and always stores a
    resolved absolute Path (with user home expanded). This keeps comparisons and
    downstream usage consistent regardless of how the input was provided.
    """
    path: Path = Field(description="The path to the file or directory")

    @field_validator("path", mode="before")
    @classmethod
    def _coerce_and_resolve_path(cls, v):
        """Coerce input into a resolved Path.

        - Accepts str or Path
        - Expands '~' and resolves to an absolute path with strict=False
        """
        if isinstance(v, str):
            v = Path(v)
        if isinstance(v, Path):
            return v.expanduser().resolve(strict=False)
        raise TypeError("path must be a str or pathlib.Path")

    @abstractmethod
    def _kind(self) -> str:
        """Return the kind of local item (e.g., 'file' or 'directory').

        Subclasses must implement this to mark the class as abstract and to
        provide a simple discriminator for debugging and representation.
        """

    def __str__(self) -> str:
        return str(self.path)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(path={repr(str(self.path))})"

    def __eq__(self, other) -> bool:
        if isinstance(other, AbstractLocalItemPath):
            return self.path == other.path
        if isinstance(other, (str, Path)):
            other_path = Path(other).expanduser().resolve(strict=False)
            return self.path == other_path
        return NotImplemented
