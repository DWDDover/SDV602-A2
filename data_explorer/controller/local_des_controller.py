import FreeSimpleGUI as sg
from data_explorer.data.file_manager import FileManager
from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.model.data_source import DataSource

class LocalDESController:
    def __init__(self, chart_data, view_factory, data_source=None, series_key=None):
        self.chart_data = chart_data
        self.view_factory = view_factory
        self.view = None
        self.data_source = data_source
        self.series_key = series_key

    def run(self):

        self.view = self.view_factory(self.chart_data)

        while True:
            event, values = self.view.window.read()
            
            if event == '-REPLACE-FILE-':
                file_manager = FileManager()
                try:
                    new_data = file_manager.read_csv(values["-REPLACE-FILE-"])
                    self.data_source = DataSource(new_data)
                    self.view.show_message("Data source changed successfully.")
                except Exception as e:
                    self.view.show_error(f"Error changing data source: {str(e)}")
                    continue
                
                self.view.update_dropdowns(self.data_source.columns())
                
                self.series_key = values["-SERIES_KEY-"]
                
            if event == 'Generate new DES':
                if self.data_source is None:
                    self.view.show_error("Please select a CSV file first.")
                    continue

                self.series_key = values["-SERIES_KEY-"]
                dv = DataVisualiser(
                    self.data_source,
                    values["-X-KEY-"],
                    values["-Y-KEY-"],
                    self.series_key
                )

                try:
                    self.chart_data = dv.create_chart_data(
                        self.chart_data.title,
                        values["-X-KEY-"],
                        values["-Y-KEY-"],
                        self.series_key
                    )
                    self.view.draw_chart(self.chart_data)
                except Exception as e:
                    self.view.show_error(f"Error updating chart data: {str(e)}")
                    continue
            
            if event == '-APPEND-FILE-':
                
                if self.data_source is None:
                    self.view.show_error("No data source available to append to.")
                    continue

                file_manager = FileManager()
                try:
                    new_data = file_manager.read_csv(values["-APPEND-FILE-"])
                    self.data_source.extend_data(new_data)
                    self.view.show_message("Data appended successfully.")
                except Exception as e:
                    self.view.show_error(f"Error appending data: {str(e)}")
                    
                dv = DataVisualiser(self.data_source, self.chart_data.x_key, self.chart_data.y_key, self.series_key)
                try:
                    self.chart_data = dv.create_chart_data(self.chart_data.title, self.chart_data.x_key, self.chart_data.y_key, self.series_key)
                except Exception as e:
                    self.view.show_error(f"Error updating chart data: {str(e)}")
                    continue
                self.view.draw_chart(self.chart_data)
            
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                self.view.close()
                break
            
            