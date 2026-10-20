import FreeSimpleGUI as sg


class RemoteView:

    def __init__(self):
        sg.theme("Kayak")
        
    def close(self):
        self.window.close()