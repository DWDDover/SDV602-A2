from data_explorer.exceptions import EmptyFileError
from operator import itemgetter
from data_explorer.model.chart_data import ChartData


class DataVisualiser:

    def __init__(self, data_source=None, x_key=None, y_key=None, series_key=None):
        self.data_source = data_source
        self.x_key = x_key
        self.y_key = y_key
        self.series_key = series_key

    ##method to prepare the data from the data source for plotting a line chart
    def create_chart_data(self, x_key, y_key, series_key=None):
        if self.data_source is None or self.data_source.is_empty():
            raise EmptyFileError("No data to plot!")

        series = {}
        for row in self.data_source.data:
            series.setdefault(row.get(series_key), []).append(row)


        for name, rows in series.items():
            rows.sort(key=itemgetter(x_key))

            x_values = []
            y_values = []

            for row in rows:
                x_values.append(row[x_key])
                y_values.append(float(row[y_key]))
                
            series[name] = (x_values, y_values)
            
        return ChartData(x_key, y_key, series)
                

