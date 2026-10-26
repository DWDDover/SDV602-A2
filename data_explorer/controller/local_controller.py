import FreeSimpleGUI as sg

from data_explorer.data.file_manager import FileManager
from data_explorer.view.local_view import LocalView
from data_explorer.model.data_source import DataSource

class LocalController:
    def run(self):
        file_manager = FileManager()
        local_view = LocalView()
        ds = None

        while True:
            event, values = local_view.window.read()

            if event == sg.WIN_CLOSED:
                local_view.close()
                break
            
            if event == "-FILE-":
                selected_file_path = values["-FILE-"]
                ds = DataSource(file_manager.read_csv(selected_file_path))
                print((ds))
                local_view.window["-SERIES_KEY-"].update(values=(ds.columns()))
                
                