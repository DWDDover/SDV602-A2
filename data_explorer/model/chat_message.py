class ChatMessage:
    
    def __init__(self, username, session_id, content, timestamp):
        self.username = username
        self.session_id = session_id
        self.content = content
        self.timestamp = timestamp
        
    def __repr__(self):
        return f"{self.username}: {self.content} ({self.timestamp})"