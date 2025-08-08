from wexample_helpers.exception.abstract_exception import AbstractException


class NotAFileException(AbstractException):
    error_code: str = "FILE_EXPECTED"

    def __init__(self, path, message: str | None = None):
        msg = message or f"Path is not a file: {path}"
        super().__init__(msg, data={"path": str(path)})
