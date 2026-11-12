import FreeSimpleGUI as sg
from data_explorer.data.file_manager import FileManager
from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.exceptions import DataExplorerException
from data_explorer.model.data_source import DataSource

class LocalDESController:
    def __init__(self, chart_data, view_factory, data_source=None, series_key=None):
        self.chart_data = chart_data
        self.view_factory = view_factory
        self.view = None
        self.data_source = data_source
        self.series_key = series_key
        
    def replace_file(self, file_path):
        file_manager = FileManager()
        try:
            new_data = file_manager.read_csv(file_path)
            self.data_source = DataSource(new_data)
            self.view.show_message("Data source changed successfully.")
            self.view.update_dropdowns(self.data_source.columns())
        except DataExplorerException as e:
            self.view.show_error(f"Error changing data source: {str(e)}")
            return
        
    def append_file(self, file_path):
        if self.data_source is None:
            self.view.show_error("No data source available to append to.")
            return

        file_manager = FileManager()
        try:
            new_data = file_manager.read_csv(file_path)
            self.data_source.extend_data(new_data)
            self.view.show_message("Data appended successfully.")
        except DataExplorerException as e:
            self.view.show_error(f"Error appending data: {str(e)}")
            return
        
        dv = DataVisualiser(self.data_source, self.chart_data.x_key, self.chart_data.y_key, self.series_key)
        try:
            self.chart_data = dv.create_chart_data(self.chart_data.title, self.chart_data.x_key, self.chart_data.y_key, self.series_key)
            self.view.draw_chart(self.chart_data)
        except Exception as e:
            self.view.show_error(f"Error updating chart data: {str(e)}")
            return
        
    def generate_des(self, chart_title, x_key, y_key, series_key):
        if self.data_source is None:
            self.view.show_error("Please select a CSV file first.")
            return None
        
        if not x_key or not y_key:
            self.view.show_error("Please select x-axis and y-axis.")
            return None
        
        if series_key == 'Select a series key':
            series_key = None
            
        if series_key and series_key not in self.data_source.columns():
            self.view.show_error(f"Series key '{series_key}' not found in data source.")
            return None

        dv = DataVisualiser(self.data_source, x_key, y_key, series_key)
        
        try:
            chart_data = dv.create_chart_data(chart_title, x_key, y_key, series_key)
            return chart_data
        except DataExplorerException as e:
            self.view.show_error(str(e))
            return None

    def run(self):

        self.view = self.view_factory(self.chart_data)

        while True:
            event, values = self.view.window.read()
            
            if event == '-REPLACE-FILE-':
                file_path = values["-REPLACE-FILE-"]
                self.replace_file(file_path)
                
                
            if event == 'Generate new DES':
                
                self.chart_data = self.generate_des(
                    values["-CHART-TITLE-"],
                    values["-X-KEY-"],
                    values["-Y-KEY-"],
                    values["-SERIES_KEY-"]
                )
            
            if event == '-APPEND-FILE-':
                
                file_path = values["-APPEND-FILE-"]
                self.append_file(file_path)
            
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                self.view.close()
                break
            
            