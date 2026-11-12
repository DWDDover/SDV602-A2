class Session:

    def __init__(self, name, host_id, private, data_source_id=None, session_id=None):
        self.name = name
        self.host_id = host_id
        self.private = private
        self.data_source_id = data_source_id
        self.session_id = session_id
        
    def __str__(self):
        return self.name if self.name else "Unnamed Session"