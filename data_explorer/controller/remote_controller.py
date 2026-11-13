from data_explorer.data.file_manager import FileManager
from data_explorer.view.remote_des_view import RemoteDESView
from data_explorer.data.session_repository import SessionRepository
from data_explorer.data.data_source_repository import DataSourceRepository
from data_explorer.controller.remote_des_controller import RemoteDESController
from data_explorer.exceptions import DataExplorerException
from multiprocessing import Process
import FreeSimpleGUI as sg

class RemoteController:
    
    def __init__(self, user, remote_view):
        self.user = user
        self.remote_view = remote_view
        self.session_repository = SessionRepository()
        self.data_source_repository = DataSourceRepository()
        self.file_manager = FileManager()
        self.active_sessions = []
        
    def create_session(self, session_name, user_id, private):
        try:
            session = self.session_repository.create_session(session_name, user_id, private)
        except DataExplorerException as e:
            self.remote_view.show_error(str(e))
            return
        dc = RemoteDESController(session, self.user, RemoteDESView)
        process = Process(target=dc.run)
        process.start()
        self.active_sessions.append(process)
        
    def join_session(self, session_id):
        try:
            session = self.session_repository.get_session_by_id(session_id)
            if session is None:
                self.remote_view.show_error(DataExplorerException("Session not found."))
                return
        except DataExplorerException as e:
            self.remote_view.show_error(str(e))
            return
        dc = RemoteDESController(session, self.user, RemoteDESView)
        process = Process(target=dc.run)
        process.start()
        self.active_sessions.append(process)
        
    def logout(self):
        self.session_repository.delete_sessions_by_host_id(self.user.user_id)
        for process in self.active_sessions:
            process.terminate()
        self.active_sessions.clear()
        self.remote_view.close()
        ##import of login controller here to avoid circular import
        from data_explorer.controller.login_controller import LoginController
        lc = LoginController()
        lc.run()
        
    def delete_session(self, session):
        if session.host_id != self.user.user_id:
            self.remote_view.show_error("You do not have permission to delete this session.")
            return
        try:
            self.session_repository.delete_session(session.session_id)
            self.refresh_sessions()
        except DataExplorerException as e:
            self.remote_view.show_error(str(e))
            
    def upload_data(self, file_path, data_name):
        try:
            data = self.file_manager.read_csv(file_path)
            self.data_source_repository.create_data_source(data_name, data, self.user.user_id)
            self.remote_view.show_message("Data uploaded successfully.")
        except DataExplorerException as e:
            self.remote_view.show_error(str(e))
            
    def refresh_sessions(self):
        try:
            sessions = self.session_repository.list_public_sessions()
            self.remote_view.refresh_sessions(sessions)
        except DataExplorerException as e:
            self.remote_view.show_error(str(e))


    def run(self):
        remote_view = self.remote_view
        
        remote_view.window['-USERNAME-'].update(self.user.username)
        self.refresh_sessions()
        
        while True:
            event, values = remote_view.window.read()
            
            if event == "-LOGOUT-":
                self.logout()
                break
            
            if event == '-CREATE_SESSION-':
                session_name = values['-SESSION_NAME-']
                ##default name if none provided
                if not session_name:
                    session_name = f"{self.user.username}'s session"
                private = values['-PRIVATE-']
                self.create_session(session_name, self.user.user_id, private)
                
            if event == '-JOIN_SESSION-':
                selected_sessions = values['-SESSION_LIST-']
                if not selected_sessions:
                    remote_view.show_error("Please select a session to join.")
                    continue
                session = selected_sessions[0]
                session_id = session.session_id
                self.join_session(session_id)


            if event == '-REFRESH_SESSIONS-':
                try:
                    self.refresh_sessions()
                except DataExplorerException as e:
                    remote_view.show_error(str(e))
                    
            if event == '-DELETE_SESSION-':
                selected_sessions = values['-SESSION_LIST-']
                if not selected_sessions:
                    remote_view.show_error("Please select a session to delete.")
                    continue
                session = selected_sessions[0]
                self.delete_session(session)
                
            if event == '-UPLOAD_DATA-':
                file_path = values['-FILE-']
                data_name = values['-DATA-NAME-']
                if not file_path:
                    remote_view.show_error("Please select a file to upload.")
                    continue
                if not data_name:
                    remote_view.show_error("Please enter a name for the data.")
                    continue
                self.upload_data(file_path, data_name)

            if event == sg.WIN_CLOSED:
                for process in self.active_sessions:
                    process.terminate()
                remote_view.close()
                break