from data_explorer.data.file_manager import FileManager
from data_explorer.view.remote_view import RemoteView
from data_explorer.view.remote_des_view import RemoteDESView
from data_explorer.data.session_repository import SessionRepository
from data_explorer.data.data_source_repository import DataSourceRepository
from data_explorer.controller.remote_des_controller import RemoteDESController
from multiprocessing import Process
from ..exceptions import DataExplorerException
import FreeSimpleGUI as sg

class RemoteController:
    
    def __init__(self, user):
        self.user = user
        self.session_repository = SessionRepository()
        self.data_source_repository = DataSourceRepository()

    def run(self):
        file_manager = FileManager()
        remote_view = RemoteView()
        ds = None
        active_sessions = []
        
        while True:
            event, values = remote_view.window.read()
            
            if event == '-CREATE_SESSION-':
                session_name = values['-SESSION_NAME-']
                ##default name if none provided
                if not session_name:
                    session_name = f"{self.user.username}'s session"
                private = values['-PRIVATE-']
                try:
                    session = self.session_repository.create_session(session_name, self.user.user_id, private)
                except DataExplorerException as e:
                    remote_view.show_error(str(e))

                dc = RemoteDESController(session, self.user)
                process = Process(target=dc.run)
                process.start()
                active_sessions.append(process)

            if event == '-REFRESH_SESSIONS-':
                try:
                    sessions = self.session_repository.list_public_sessions()
                    remote_view.window['-SESSION_LIST-'].update(sessions)
                except DataExplorerException as e:
                    remote_view.show_error(str(e))

            if event == sg.WIN_CLOSED:
                for process in active_sessions:
                    process.terminate()
                remote_view.close()
                break