import FreeSimpleGUI as sg


class LocalView:

    def __init__(self):
        sg.theme("DarkBlue")
        
    def close(self):
        self.window.close()