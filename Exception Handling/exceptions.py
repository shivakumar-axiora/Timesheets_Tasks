class DataReaderError(Exception):
    """Base class for TXT reader errors."""
    pass


class FileEmptyError(DataReaderError):
    """Raised when file is empty."""
    pass


class InvalidFileError(DataReaderError):
    """Raised when file is not a valid .txt file."""
    pass