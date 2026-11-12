from data_explorer.data.database_manager import DatabaseManager
from data_explorer.model.chat_message import ChatMessage
from datetime import datetime
from bson import ObjectId

class MessageRepository:
    
    def __init__(self):
        self.db_manager = DatabaseManager.getInstance()

    def create_message(self, username, session_id, content):
        # Ignore empty messages or just blank spaces
        if content.strip() == "":
            return None 
        message_id = self.db_manager.insert_one("messages", {
            "username": username,
            "session_id": session_id,
            "content": content,
            "timestamp": datetime.now()
        })
        return ChatMessage(username=username, session_id=session_id, content=content, timestamp=datetime.now(), message_id=message_id)
    
    def get_messages_by_session(self, session_id, last_message_id=None):
        query = {"session_id": session_id}
        if last_message_id is not None:
            query["_id"] = {"$gt": ObjectId(last_message_id)}
        messages_data = self.db_manager.get_collection("messages").find(query)
        messages = []
        for message_data in messages_data:
            messages.append(ChatMessage(
                username=message_data['username'],
                session_id=message_data['session_id'],
                content=message_data['content'],
                timestamp=message_data['timestamp'],
                message_id=str(message_data['_id'])
            ))
            ## Sort messages by message_id to ensure they are in the order they were created
            messages.sort(key=lambda x: str(x.message_id))
        return messages
    
    def delete_session_messages(self, session_id):
        self.db_manager.get_collection("messages").delete_many({"session_id": session_id})