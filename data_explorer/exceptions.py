class DataExplorerException(Exception):
    """Base class for exceptions in this module."""

class InvalidFileFormatError(Exception):
    """Exception raised for errors in the input file format."""

class EmptyFileError(Exception):
    """Exception raised for empty files."""
    
class InvalidFilePathError(Exception):
    """Exception raised for invalid file paths."""
    
class IncompatibleDataSourceError(Exception):
    """Exception raised for incompatible data sources."""