from database_manager import DatabaseManager
import config
from datetime import datetime

class ChatMessage:
    
    def __init__(self, username, text, timestamp=None):
        self.username = username
        self.text = text
        
        if timestamp is None:
            self.timestamp =datetime.now()
        else:
            self.timestamp = timestamp
            
        self.db = DatabaseManager.getInstance()
        
    #For my code just a method that returns the object. Will have another class that takes the 
    #object and sends to the correct collection, as well as returning the whole collection
    def save(self):
        return self.db.insert_one(config.CHAT_MESSAGES_COLLECTION, {
            "username" : self.username,
            "text" : self.text,
            "timestamp": self.timestamp
        })
        
    @classmethod
    def all(cls):
        db = DatabaseManager.getInstance()
        collection = db.get_collection(config.CHAT_MESSAGES_COLLECTION)
        
        messages = []
        for document in collection.find().sort("timestamp"):
            message = cls(document["username"], document["text"], document["timestamp"])
            messages.append(message)
            
        return messages