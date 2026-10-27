import FreeSimpleGUI as sg


class RemoteView:

    def __init__(self):
        sg.theme("DarkRed1")
        
        session_box = [
            [sg.Listbox(values=[], size=(30, 4), key='-SESSION_LIST-')],
            [sg.Button('Join Session', pad=20, size=(15, 2), bind_return_key=True)],
        ]
        
        self.layout = [
            [sg.Frame('Join a session', session_box)],
            [sg.Text("upload a CSV:"), sg.Input(key="-FILE-", enable_events=True), sg.FileBrowse(button_text='Browse', file_types=(('CSV Files', '*.csv'),))],
            [sg.Text('Data name:'), sg.Input(size=(40, 5), key='-NAME-'), sg.Button('Upload')],
        ]
        
        self.window = sg.Window("Remote Mode", self.layout, size=(900, 430), finalize=True)
        
    def close(self):
        self.window.close()
        
    def show_error(self, message):
        sg.popup_error(message)

    def show_message(self, message):
        sg.popup(message)