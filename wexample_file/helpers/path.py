from pathlib import Path
from wexample_file.const.types import PathOrString


def path_wrap(path: PathOrString) -> Path:
    if isinstance(path, str):
        return Path(path)
    return path
