from exceptions import EmptyFileError


class DataVisualiser:

    def __init__(self, data_source=None, x_key=None, y_key=None, series_key=None):
        self.data_source = data_source
        self.x_key = x_key
        self.y_key = y_key
        self.series_key = series_key

    def __load_csv(self):
        data = self.data_source.data
        if not data:
            raise EmptyFileError(f"No data loaded from file: {self.data_source.name}")

        return data

    def load_data(self, file_name):
        data = self.__load_csv(file_name)
        if not data:
            return
        
        data_source = DataSource(file_name, data)

        self.data_source = data_source

    def append_data(self, file_name):
        new = self.__load_csv(file_name)
        if not new or not self.data_source:
            return

        if self.data_source.data[0].keys() != new[0].keys():
            print("Data doesn't match")
            return

        self.data_source.data.extend(new)

    def load_data_source(self, name):
        self.data_source = DataSource.load(name)

    def plot_line_chart(self, x_key, y_key, title, series_key=None):
        if not self.data_source:
            print("No data to plot!")
            return

        series = {}
        for row in self.data_source.data:
            series.setdefault(row.get(series_key), []).append(row)

        plt.figure(figsize=(8, 6))


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
