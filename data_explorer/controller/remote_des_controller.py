import FreeSimpleGUI as sg
from data_explorer.data.data_source_repository import DataSourceRepository
from data_explorer.data.file_manager import FileManager
from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.model.data_source import DataSource
from data_explorer.data.session_repository import SessionRepository
from data_explorer.data.message_repository import MessageRepository
from data_explorer.exceptions import DataExplorerException

class RemoteDESController:
    def __init__(self, session, user, view_factory, chart_data=None):
        self.session = session
        self.user = user
        self.view = None
        self.view_factory = view_factory
        self.data_source = None
        self.chart_data = chart_data
        self.data_source_repository = None
        self.session_repository = None
        self.message_repository = None
        self.file_manager = None
        
    def replace_data(self, data_source):
        data_source_id = data_source.data_source_id
        try:
            data = self.data_source_repository.get_data_source_by_id(data_source_id)
            if data is not None:
                self.session_repository.update_session(self.session.session_id, {"data_source_id": data_source_id})
                self.data_source = data
                self.session.data_source_id = data_source_id
                self.view.update_dropdowns(self.data_source.columns())
        except DataExplorerException as e:
            self.view.show_error(str(e))
        
    def update_combos(self):
        user_sources = self.data_source_repository.get_sources_by_user_id(self.user.user_id)
        self.view.update_combos(user_sources)
        
    def upload_data(self, file_path, data_name):
        self.file_manager = FileManager()
        try:
            data = self.file_manager.read_csv(file_path)
            self.data_source_repository.create_data_source(data_name, data, self.user.user_id)
            self.view.show_message("Data uploaded successfully.")
        except DataExplorerException as e:
            self.view.show_error(str(e))
        
    def append_data(self, data_source):
        if self.data_source is None:
            self.view.show_error("No data source available to append to.")
            return
        try:
            new_data = self.data_source_repository.get_data_source_by_id(data_source.data_source_id)
            if new_data is not None:
                current_data = self.data_source
                current_data.extend_data(new_data.data)
                new_id = self.data_source_repository.create_data_source(f"{self.data_source.name}_appended", current_data.data, self.user.user_id)
                self.session_repository.update_session(self.session.session_id, {"data_source_id": new_id})
                self.data_source = self.data_source_repository.get_data_source_by_id(new_id)
                self.session.data_source_id = new_id
                self.view.show_message("Data appended successfully.")
                self.update_combos()
        except DataExplorerException as e:
            self.view.show_error(str(e))
    
    def generate_chart(self, series_key, x_key, y_key):
        if self.data_source is None:
            self.view.show_error("No data source selected. Please select a data source first.")
            return
        
        if self.data_source.is_empty():
            self.view.show_error("Data source is empty. Please select data first.")
            return
        
        try:
            dv = DataVisualiser(self.data_source, x_key, y_key, series_key)
            self.chart_data = dv.create_chart_data(self.data_source.name, x_key, y_key, series_key)
            self.view.draw_chart(self.chart_data)
        except DataExplorerException as e:
            self.view.show_error(str(e))
    
    def run(self):
        self.data_source_repository = DataSourceRepository()
        self.session_repository = SessionRepository()
        self.message_repository = MessageRepository()
        self.view = self.view_factory(self.chart_data, self.session.name)
        self.update_combos()
        self.data_source = self.data_source_repository.get_data_source_by_id(self.session.data_source_id) if self.session.data_source_id else None
        if self.data_source:
            self.view.update_dropdowns(self.data_source.columns())

        while True:
            event, values = self.view.window.read(timeout=2000)
            
            if event == '__TIMEOUT__':
                remote_session = self.session_repository.get_session_by_id(self.session.session_id)
                if remote_session is None:
                    self.view.show_error("This session has been deleted by the host.")
                    self.view.close()
                    break
                if remote_session.data_source_id != self.session.data_source_id and remote_session.data_source_id is not None:
                    try:
                        self.data_source = self.data_source_repository.get_data_source_by_id(remote_session.data_source_id)
                        if self.data_source:
                            self.view.update_dropdowns(self.data_source.columns())
                            self.session.data_source_id = remote_session.data_source_id
                            self.view.show_message("The data source for this session has been updated")
                            self.view.draw_chart(None)
                    except DataExplorerException as e:
                        self.view.show_error(str(e))
            
            if event == sg.WIN_CLOSED:
                self.view.close()
                break
            
            if event == '-APPEND-DATA-':
                file = values['-APPEND-FILE-']
                self.append_data(file)
            
            if event == '-UPLOAD-FILE-':
                file_path = values['-FILE-']
                data_name = values['-DATA-NAME-']
                if not file_path:
                    self.view.show_error("Please select a file to upload.")
                    continue
                if not data_name:
                    self.view.show_error("Please provide a name for the data source.")
                    continue
                self.upload_data(file_path, data_name)
                self.update_combos()
            
            if event == '-REPLACE-FILE-':
                file = values['-REPLACE-FILE-']
                self.replace_data(file)
                
            if event == '-GENERATE-CHART-':
                series_key = values['-SERIES_KEY-']
                x_key = values['-X-KEY-']
                y_key = values['-Y-KEY-']
                if series_key == 'Select a new series key':
                    series_key = None
                self.generate_chart(series_key, x_key, y_key)
            
            
