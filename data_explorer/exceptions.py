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
    
class NonNumericDataError(DataExplorerException):
    """Exception raised for non-numeric data in the dataset selected for the y axis."""
    
class NonColumnKeyError(DataExplorerException):
    """Exception raised for non-column keys in the dataset selected for the x axis or series key."""