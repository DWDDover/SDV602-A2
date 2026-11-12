from data_explorer.data.database_manager import DatabaseManager
from data_explorer.model.chat_message import ChatMessage
from datetime import datetime

class MessageRepository:
    
    def __init__(self):
        self.db_manager = DatabaseManager.getInstance()

    def create_message(self, username, session_id, content):
        message_id = self.db_manager.insert_one("messages", {
            "username": username,
            "session_id": session_id,
            "content": content,
            "timestamp": datetime.now()
        })
        return ChatMessage(username=username, session_id=session_id, content=content, timestamp=datetime.now())
    
    def get_messages_by_session(self, session_id):
        messages_data = self.db_manager.get_collection("messages").find({"session_id": session_id})
        messages = []
        for message_data in messages_data:
            messages.append(ChatMessage(
                username=message_data['username'],
                session_id=message_data['session_id'],
                content=message_data['content'],
                timestamp=message_data['timestamp']
            ))
        return messages
    
    def delete_session_messages(self, session_id):
        self.db_manager.get_collection("messages").delete_many({"session_id": session_id})