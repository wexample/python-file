from wexample_helpers.exception.abstract_exception import AbstractException


class NotADirectoryException(AbstractException):
    error_code: str = "DIRECTORY_EXPECTED"

    def __init__(self, path, message: str | None = None):
        msg = message or f"Path is not a directory: {path}"
        super().__init__(msg, data={"path": str(path)})
