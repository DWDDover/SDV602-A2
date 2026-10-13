import FreeSimpleGUI as sg


class LocalView:

    def __init__(self):
        sg.theme("LightBlue3")
        
    def close(self):
        self.window.close()