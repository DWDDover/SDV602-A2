from database_manager import DatabaseManager

class DataSource:
    
    def __init__(self, name, data):
        self.name = name
        self.data = data
        
        self.db = DatabaseManager.getInstance()
        
    def save(self):
        return self.db.insert_one({
            "name" : self.name,
            "data" : self.data
        })
    
    @classmethod
    def load(cls, name):
        db = DatabaseManager.getInstance()
        document = db.find_one_by_name(name)
        
        if document is None:
            return
        
        return cls(name, document["data"])

    