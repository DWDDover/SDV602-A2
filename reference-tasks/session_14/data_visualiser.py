from file_manager import FileManager
import matplotlib.pyplot as plt
from operator import itemgetter
from data_source import DataSource

class DataVisualiser:
    
    def __init__(self):
        self.fm = FileManager()
        self.data_source = DataSource("default", None)
        
    def __load_csv(self, file_name):
        data = self.fm.read_csv(file_name)
        
        if not data:
            print(f"No data loaded from file: {file_name}")
            return
        
        return data
    
    def load_data(self, file_name):
        data = self.__load_csv(file_name)
        if not data:
            return
        
        data_source = DataSource(file_name, data)
        
        self.data_source = data_source
        
        
    def append_data(self, file_name):
        new_data = self.__load_csv(file_name)
        if not new_data or not self.data_source:
            return
        
        if self.data_source.data[0].keys() != new_data[0].keys():
            print("Data doesn't match")
            return
        
        self.data_source.data.extend(new_data)
        
    def load_data_source(self, name):
        self.data_source = DataSource.load(name)
        
    def plot_line_chart(self, x_key, y_key, title, series_key=None):
        
        if not self.data_source:
            print("No data to plot")
            return
        
        series = {}
        for row in self.data_source.data:
            series.setdefault(row.get(series_key) , []).append(row)
            
        plt.figure(figsize=(8, 8))
        
        for name, rows in series.items():
            rows.sort(key=itemgetter(x_key))
            
            x_values = []
            y_values = []
            
            for row in rows:
                x_values.append(row[x_key])
                y_values.append(float(row[y_key]))
                
            plt.plot(x_values, y_values, marker='o', label=name)
            
        if series_key:
            plt.legend()
            
        plt.xlabel(x_key)
        plt.ylabel(y_key)
        plt.title(title)
        
        plt.show()

        
