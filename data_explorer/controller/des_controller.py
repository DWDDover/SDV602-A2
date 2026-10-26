import FreeSimpleGUI as sg

class DESController:
    def __init__(self, chart_data, view_factory):
        self.chart_data = chart_data
        self.view_factory = view_factory
        self.view = None

    def run(self):

        self.view = self.view_factory(self.chart_data)
         
        while True:
            event, values = self.view.window.read()
            
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                self.view.close()
                break
            
            