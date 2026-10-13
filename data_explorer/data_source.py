from database_manager import DatabaseManager
import json
import config

class DataSource:

    def __init__(self, name, data):
        self.name = name
        self.data = data

        self.db = DatabaseManager.getInstance()

    def save(self):
        return self.db.insert_one(config.DATA_SOURCES_COLLECTION, {
            "name": self.name,
            "data": self.data
        })

    @classmethod
    def load(cls, name):
        db = DatabaseManager.getInstance()
        document = db.find_one_by_name(config.DATA_SOURCES_COLLECTION,name)

        if document is None:
            return None

        return cls(name, document["data"])