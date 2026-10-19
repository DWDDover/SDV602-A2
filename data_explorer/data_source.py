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
            list: A list of column names if data is not None, otherwise None
        """
        if self.data == []:
            return []
            
        else:
            return list(self.data[0].keys())
            