from __future__ import annotations

from typing import Any

from wexample_helpers.const.types import PathOrString


class WithPathMixin:
    path: Any = None

    def get_path(self) -> Any:
        assert self.path is not None
        return self.path

    def set_path(self, path: PathOrString | None) -> None:
        from pathlib import Path

        self.path = None if path is None else Path(path)
