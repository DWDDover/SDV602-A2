import csv
from exceptions import InvalidFileFormatError, EmptyFileError, InvalidFilePathError


class FileManager:
    """Handles all File I/O operations."""

    def __init__(self):
        pass

    def read_csv(self, file_name):
        """Reads a CSV file and returns the data as a list of dictionaries."""
        ## empty list fits the format in data source
        data = []
        try:
            with open(file_name, mode='r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    data.append(row)
                    
                if reader.fieldnames is None:
                    raise EmptyFileError("File is empty")

            return data

        except FileNotFoundError:
            raise InvalidFilePathError("File not found, please check the file path.")

        except csv.Error:
            raise InvalidFileFormatError("Invalid CSV format")