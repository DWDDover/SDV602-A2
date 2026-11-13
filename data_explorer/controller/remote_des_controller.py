import FreeSimpleGUI as sg
from data_explorer.data.file_manager import FileManager
from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.model.data_source import DataSource

class RemoteDESController:
    def __init__(self, session, user, view_factory, chart_data=None):
        self.session = session
        self.user = user
        self.view = None
        self.view_factory = view_factory
        self.chart_data = chart_data
    def run(self):

        self.view = self.view_factory(self.chart_data, self.session.name)

        while True:
            event, values = self.view.window.read()
            
            if event == sg.WIN_CLOSED:
                self.view.close()
                break
            
