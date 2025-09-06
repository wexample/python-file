from pathlib import Path

from pydantic import Field


class WithPathMixin:
    path: Path | None = Field(
        default=None,
        description="The local file or directory path"
    )

    def get_path(self) -> Path:
        assert self.path is not None
        return self.path
