from ..exceptions import EmptyFileError, NonColumnKeyError, NonNumericDataError
from operator import itemgetter
from data_explorer.model.chart_data import ChartData


class DataVisualiser:

    def __init__(self, data_source=None, x_key=None, y_key=None, series_key=None):
        self.data_source = data_source
        self.x_key = x_key
        self.y_key = y_key
        self.series_key = series_key

    ##method to prepare the data from the data source for plotting a line chart
    def create_chart_data(self, title, x_key, y_key, series_key=None):
        if self.data_source is None or self.data_source.is_empty():
            raise EmptyFileError("No data to plot!")
        
        if x_key not in self.data_source.columns():
            raise NonColumnKeyError(f"'{x_key}' is not a valid x-axis column key in the dataset.")
        
        if y_key not in self.data_source.columns():
            raise NonColumnKeyError(f"'{y_key}' is not a valid y-axis column key in the dataset.")

        if series_key and series_key not in self.data_source.columns():
            raise NonColumnKeyError(f"'{series_key}' is not a valid series key in the dataset.")

        series = {}
        for row in self.data_source.data:
            series.setdefault(row.get(series_key), []).append(row)


        for name, rows in series.items():
            rows.sort(key=itemgetter(x_key))

            x_values = []
            y_values = []

            for row in rows:
                x_values.append(row[x_key])
                try:
                    y_values.append(float(row[y_key]))
                except (ValueError, TypeError) as e:
                    raise NonNumericDataError(f"Non-numeric data found in the y-axis column on value {row[y_key]}.") from e

            series[name] = (x_values, y_values)
            
        return ChartData(title, x_key, y_key, series)
                

