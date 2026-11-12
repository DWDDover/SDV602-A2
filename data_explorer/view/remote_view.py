import FreeSimpleGUI as sg


class RemoteView:

    def __init__(self):
        sg.theme("DarkRed1")
        
        session_box = [
            [sg.Listbox(values=[], size=(30, 12), key='-SESSION_LIST-')],
            [sg.Button('Join Session', pad=20, size=(15, 2), key='-JOIN_SESSION-', bind_return_key=True)],
        ]
        create_session_box = [
            [sg.Text('Session name:'), sg.Input(size=(20, 1), key='-SESSION_NAME-')],
            [sg.Checkbox('Private', key='-PRIVATE-', default=False)],
            [sg.Button('Create Session', pad=20, size=(15, 2), key='-CREATE_SESSION-', bind_return_key=True)],
        ]

        self.layout = [
            [sg.Push(), sg.Text("Logged in as: "), sg.Text("", key='-USERNAME-', size=(20, 1)), sg.Button('Logout', size=(10, 1)), sg.Push()],
            [sg.Frame('Join a session', session_box, pad=(20, 15)), sg.Push(), sg.Frame('Create a session', create_session_box, pad=(20, 15))],
            [sg.VPush()],
            [sg.Push(),sg.Text("upload a CSV:"), sg.Input(key="-FILE-", enable_events=True), sg.FileBrowse(button_text='Browse', file_types=(('CSV Files', '*.csv'),)), sg.Push(),],
            [sg.Push(),sg.Text('Data name:'), sg.Input(size=(40, 5), key='-DATA-NAME-'), sg.Button('Upload'), sg.Push(),],
        ]
        
        self.window = sg.Window("Remote Mode", self.layout, size=(700, 430), finalize=True)
        
    def close(self):
        self.window.close()
        
    def show_error(self, message):
        sg.popup_error(message)

    def show_message(self, message):
        sg.popup(message)