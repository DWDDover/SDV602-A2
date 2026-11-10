from datetime import datetime

class ChatMessage:
    
    def __init__(self, user_id, session_id, content):
        self.user_id = user_id
        self.session_id = session_id
        self.content = content
        self.timestamp = datetime.now()