class ChatMessage:
    
    def __init__(self, username, session_id, content, timestamp, message_id=None):
        self.username = username
        self.session_id = session_id
        self.content = content
        self.timestamp = timestamp
        self.message_id = message_id
        
    def __str__(self):
        return f"{self.username}: {self.content}    ({self.timestamp.strftime('%H:%M:%S')})\n"