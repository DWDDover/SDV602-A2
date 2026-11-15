##Test local view class for testing local controllers calls

class TestLocalView:
    def __init__(self):
        self.dropdown_values = []
        self.error_message = None
        self.window_closed = False

    def update_dropdowns(self, columns):
        self.dropdown_values = columns

    def show_error(self, message):
        self.error_message = message

class TestRemoteView:
    def __init__(self):
        self.error_message = None
        self.message = None
        self.chart_data = None
        self.data_sources = []
        self.window_closed = False

    def show_error(self, message):
        self.error_message = message

    def show_message(self, message):
        self.message = message

    def draw_chart(self, chart_data):
        self.chart_data = chart_data

    def update_combos(self, data_sources):
        self.data_sources = data_sources
        
    def update_dropdowns(self, columns):
        self.dropdown_values = columns

    def close(self):
        self.window_closed = True