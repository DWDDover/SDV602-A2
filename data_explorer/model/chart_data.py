class ChartData:
    def __init__(self, title, x_key, y_key, series=None):
        self.x_key = x_key
        self.y_key = y_key
        self.series = {} if series is None else series
        self.title = title