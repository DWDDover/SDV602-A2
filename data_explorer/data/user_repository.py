from data_explorer.data.database_manager import DatabaseManager
from data_explorer.model.user import User
import bcrypt

##methods: login, regfister
class UserRepository:
    
    def __init__(self):
        self.db_manager = DatabaseManager.getInstance()

    def login(self, username, password):
        user_data = self.db_manager.find_one_by_name("users", username)
        if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data['password']):
            return User(user_id=str(user_data['_id']), username=user_data['name'])
        return None

    def register(self, username, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        if self.db_manager.find_one_by_name("users", username):
            return None  #duplociate username
        user_id = self.db_manager.insert_one("users", {"name": username, "password": hashed_password})
        return User(user_id=str(user_id), username=username)