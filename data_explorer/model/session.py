class Session:

    def __init__(self, name, host_id, private, users, data_source_id=None, session_id=None):
        self.name = name
        self.host_id = host_id
        self.users = users
        self.private = private
        self.data_source_id = data_source_id
        self.session_id = session_id