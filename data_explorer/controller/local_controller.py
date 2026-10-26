from multiprocessing import Process
from ..exceptions import DataExplorerException
import FreeSimpleGUI as sg

from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.controller.des_controller import DESController
from data_explorer.data.file_manager import FileManager
from data_explorer.view.local_view import LocalView
from data_explorer.view.local_des_view import LocalDESView
from data_explorer.model.data_source import DataSource

class LocalController:
    def run(self):
        file_manager = FileManager()
        local_view = LocalView()
        ds = None
        active_des = []

        while True:
            event, values = local_view.window.read()

            if event == sg.WIN_CLOSED:
                for process in active_des:
                    process.terminate()
                local_view.close()
                break
            
            if event == "-FILE-":
                selected_file_path = values["-FILE-"]
                try:
                    ds = DataSource(file_manager.read_csv(selected_file_path))
                    local_view.window["-X-AXIS-"].update(values=(ds.columns()))
                    local_view.window["-Y-AXIS-"].update(values=(ds.columns()))
                    local_view.window["-SERIES_KEY-"].update(values=(ds.columns()))
                except DataExplorerException as e:
                    local_view.show_error(f"Error reading CSV file: {str(e)}")
                    continue

            if event == "Generate DES":
                
                chart_title = 'Untitled Chart'
                
                if ds is None:
                    local_view.show_error("Please select a CSV file first.")
                    continue

                try:
                    x_key = values["-X-AXIS-"]
                    y_key = values["-Y-AXIS-"]
                except Exception as e:
                    local_view.show_error(f"Error reading input values: {str(e)}")
                    continue
                
                series_key = values["-SERIES_KEY-"]

                if values["-TITLE-"]:
                    chart_title = values["-TITLE-"]
                
                if not x_key or not y_key:
                    local_view.show_error("Please select x-axis and y-axis.")
                    continue
                
                                
                dv = DataVisualiser(ds, x_key, y_key, series_key)
                
                try:
                    chart_data = dv.create_chart_data(chart_title, x_key, y_key, series_key)
                except DataExplorerException as e:
                    local_view.show_error(str(e))
                    continue
                
                dc = DESController(chart_data, LocalDESView)
                process = Process(target=dc.run)
                process.start()
                active_des.append(process)

                
                
                