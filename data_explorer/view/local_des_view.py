import FreeSimpleGUI as sg


class LocalDESView:

    def __init__(self, chart_data):
        sg.theme("LightBlue3")
        
        self.layout = [
            [sg.Push(), sg.Text(f"{chart_data.title}"), sg.Push()],
            [sg.Canvas()],
            [sg.Button('Change data source', pad=20, size=(15, 2))],
            [sg.Button('Append to data source', pad=20, size=(15, 2))],
        ]
        
        self.window = sg.Window("Local DES", self.layout, size=(900, 430), finalize=True)
        
    def close(self):
        self.window.close()
        
    def show_error(self, message):
        sg.popup_error(message)

    def show_message(self, message):
        sg.popup(message)