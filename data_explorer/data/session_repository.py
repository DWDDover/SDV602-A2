from data_explorer.data.database_manager import DatabaseManager
from data_explorer.model.session import Session

##methods: create_session, get_session_by_id, update_session, delete_session
class SessionRepository:
    
    def __init__(self):
        self.db_manager = DatabaseManager.getInstance()

    def create_session(self, name, host_id, private, data_source_id=None):
        session = Session(name=name, host_id=host_id, private=private, data_source_id=data_source_id)
        session_id = self.db_manager.insert_one("sessions", {
            "name": session.name,
            "host_id": session.host_id,
            "private": session.private,
            "data_source_id": session.data_source_id
        })
        session.session_id = str(session_id)
        return session
    
    def document_to_session(self, session_data):
        session = Session(
            name=session_data['name'],
            host_id=session_data['host_id'],
            private=session_data['private'],
            data_source_id=session_data.get('data_source_id'),
            session_id=str(session_data['_id'])
        )
        return session

    def get_session_by_id(self, session_id):
        session_data = self.db_manager.find_one_by_id("sessions", session_id)
        if session_data:
            return self.document_to_session(session_data)
        return None
    
    def list_public_sessions(self):
        sessions = self.db_manager.get_collection("sessions").find({"private": False})
        list_of_sessions = []
        for session in sessions:
            list_of_sessions.append(self.document_to_session(session))
        return list_of_sessions

    def update_session(self, session_id, update):
        self.db_manager.update_one_by_id("sessions", session_id, update)
    
    def delete_session(self, session_id):
        self.db_manager.delete_one_by_id("sessions", session_id)
        
    
