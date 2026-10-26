from multiprocessing.dummy import Process

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

        while True:
            event, values = local_view.window.read()

            if event == sg.WIN_CLOSED:
                local_view.close()
                break
            
            if event == "-FILE-":
                selected_file_path = values["-FILE-"]
                ds = DataSource(file_manager.read_csv(selected_file_path))
                local_view.window["-X-AXIS-"].update(values=(ds.columns()))
                local_view.window["-Y-AXIS-"].update(values=(ds.columns()))
                local_view.window["-SERIES_KEY-"].update(values=(ds.columns()))
                
            if event == "Generate DES":
                
                if ds is None:
                    local_view.show_error("Please select a CSV file first.")
                    continue

                x_key = values["-X-AXIS-"]
                y_key = values["-Y-AXIS-"]
                series_key = values["-SERIES_KEY-"]

                if not x_key or not y_key or not series_key:
                    local_view.show_error("Please select x-axis, y-axis, and series key.")
                    continue
                
                active_des = []
                dc = DESController(ds)
                process = Process(target=dc.local_des_run)
                process.start()
                active_des.append(process)
                
                dv = DataVisualiser(ds, x_key, y_key, series_key)
                
                chart_data = dv.create_chart_data(x_key, y_key, series_key)
                
                # Generate the DES (Data Exploration Summary)
                des = ds.generate_des(chart_data)
                
                # Show the DES in a popup
                local_view.show_message(des)
                
                