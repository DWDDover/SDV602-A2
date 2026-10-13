import bcrypt
from database_manager import DatabaseManager
import config

class User:

    db = DatabaseManager.getInstance()
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.db = DatabaseManager.getInstance()
        
    def hash_password(self, password):
        password_bytes = password.encode('utf-8')
    
        salt = bcrypt.gensalt()
        
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password
    
    def verify_password(self, password):       
        return bcrypt.checkpw(password.encode('utf-8'), self.password)
        
    @classmethod
    def login(cls, username, password):

        user_details = cls.db.find_one_by_name(config.USER_COLLECTION, username)

        if not user_details:
            return None

        user = cls(user_details["name"], user_details["password"])
        return user if user.verify_password(password) else None
            
    def save(self):
        
        if not self.db.find_one_by_name(config.USER_COLLECTION, self.username):
            self.db.insert_one(config.USER_COLLECTION, {
                "name" : self.username,
                "password" : self.hash_password(self.password)
            })
            return True
        
        else:
            return False
            