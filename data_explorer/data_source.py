class DataSource:
    """A class used to represent a data source."""
    def __init__(self, name="", data=None):
        """ Initialise a new data source instance
        
        Parameters:
        name (str): the name of the data source
        data (list of dicts): the data held by the data source """
        
        self.name = name
        if data is None:
            self.data = []
        else:
            self.data = data
        
    def columns(self):
        """Return the column names from the data

        Returns:
            list: A list of column names or an mpty list if the data is empoty
        """
        if self.is_empty():
            return []
            
        else:
            return list(self.data[0].keys())
        
    def is_empty(self):
        """Check if the data source is empty

        Returns:
            bool: True if the data source is empty, False otherwise
        """
        ## this works because a none data source is always turned into an empty list in constructor
        return len(self.data) == 0
    
    def is_compatible(self, other):
        """Checks if the data source compatible with another data source

        Parameters:
            other (DataSource): The other data source
            
        Returns:
            bool: True if the data sources are compatible, False if not
        """
            
        if self.is_empty() or other.is_empty():
            return True
        ## only compatible with exact column match
        else:
            return self.columns() == other.columns()
        
    def append_data(self, new_data):
        """Append new data to the data source, changes the source in place

        Parameters:
            new_data (list of dicts): The new data to append
            
        Raises:
            ValueError: If the new data is not compatible with the existing data
        """
        if not self.is_compatible(DataSource(data=new_data)):
            raise ValueError("New data is not compatible with existing data")
        
        self.data.extend(new_data)
            