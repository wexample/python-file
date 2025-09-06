from pathlib import Path

from pydantic import Field, field_validator
from wexample_helpers.const.types import PathOrString


class WithPathMixin:
    path: Path | None = Field(
        default=None,
        description="The local file or directory path"
    )

    def get_path(self) -> Path:
        assert self.path is not None
        return self.path

    @classmethod
    @field_validator("path", mode="before")
    def _coerce_path(cls, v: PathOrString | None) -> Path | None:
        if v is None or isinstance(v, Path):
            return v
        return Path(v)

    def set_path(self, path: PathOrString | None) -> None:
        self.path = None if path is None else Path(path)
