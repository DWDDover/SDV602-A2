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
