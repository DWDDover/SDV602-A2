class ChartData:
    def __init__(self, title, x_key, y_key, series={}):
        self.title = title
        self.x_key = x_key
        self.y_key = y_key
        self.series = series