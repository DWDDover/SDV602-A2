import FreeSimpleGUI as sg

from data_explorer.data.file_manager import FileManager
from data_explorer.view.local_view import LocalView

class LocalController:
    def run(self):
        file_manager = FileManager()
        local_view = LocalView()

        while True:
            event, values = local_view.window.read()

            if event == sg.WIN_CLOSED:
                local_view.close()
                break