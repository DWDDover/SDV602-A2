from data_explorer.data.file_manager import FileManager
from data_explorer.view.remote_view import RemoteView
from multiprocessing import Process
from ..exceptions import DataExplorerException
import FreeSimpleGUI as sg

class RemoteController:
    
    def __init__(self, user):
        self.user = user

    def run(self):
        file_manager = FileManager()
        remote_view = RemoteView()
        ds = None
        active_sessions = []
        
        while True:
            event, values = remote_view.window.read()

            if event == sg.WIN_CLOSED:
                for process in active_sessions:
                    process.terminate()
                remote_view.close()
                break