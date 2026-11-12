from multiprocessing import Process
from ..exceptions import DataExplorerException
import FreeSimpleGUI as sg

from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.controller.local_des_controller import LocalDESController
from data_explorer.view.local_des_view import LocalDESView
from data_explorer.model.data_source import DataSource

class LocalController:
    
    def __init__(self, file_manager, local_view, data_source=None):
        self.file_manager = file_manager
        self.local_view = local_view
        self.data_source = data_source
        
    def file_chosen(self, file_path):
        try:
            self.data_source = DataSource(self.file_manager.read_csv(file_path))
            self.local_view.update_dropdowns(self.data_source.columns())
        except DataExplorerException as e:
            self.local_view.show_error(f"Error reading CSV file: {str(e)}")
            
    def generate_des(self, chart_title, x_key, y_key, series_key):
        if self.data_source is None:
            self.local_view.show_error("Please select a CSV file first.")
            return None
        
        if not x_key or not y_key:
            self.local_view.show_error("Please select x-axis and y-axis.")
            return None
        
        if series_key == 'Select a series key':
            series_key = None
            
        if series_key and series_key not in self.data_source.columns():
            self.local_view.show_error(f"Series key '{series_key}' not found in data source.")
            return None

        dv = DataVisualiser(self.data_source, x_key, y_key, series_key)
        
        try:
            chart_data = dv.create_chart_data(chart_title, x_key, y_key, series_key)
            return chart_data
        except DataExplorerException as e:
            self.local_view.show_error(str(e))
            return None
        
    def start_des_process(self, chart_data, series_key):
        dc = LocalDESController(chart_data, LocalDESView, self.data_source, series_key)
        process = Process(target=dc.run)
        process.start()
        return process

    def run(self):
        active_des = []

        while True:
            event, values = self.local_view.window.read()

            if event == sg.WIN_CLOSED:
                for process in active_des:
                    process.terminate()
                self.local_view.close()
                break
            
            if event == "Clear Fields":
                self.local_view.clear_fields()
                self.data_source = None
                continue
            
            if event == "-FILE-":
                selected_file_path = values["-FILE-"]
                self.file_chosen(selected_file_path)
                continue
                

            if event == "Generate DES":
                
                chart_title = 'Untitled Chart'

                x_key = values["-X-AXIS-"]
                y_key = values["-Y-AXIS-"]
                series_key = values["-SERIES_KEY-"]

                if values["-TITLE-"]:
                    chart_title = values["-TITLE-"]
                
                try:
                    chart_data = self.generate_des(chart_title, x_key, y_key, series_key)
                    if chart_data is None:
                        continue
                except DataExplorerException as e:
                    self.local_view.show_error(str(e))
                    continue
                
                process = self.start_des_process(chart_data, series_key)
                active_des.append(process)

                
                
                