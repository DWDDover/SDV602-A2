import FreeSimpleGUI as sg


class RemoteView:

    def __init__(self):
        sg.theme("LightGreen9")
        
        session_box = [
            [sg.Listbox(values=[], size=(30, 10), key='-SESSION_LIST-')],
            [sg.Button('Join Session', pad=5, size=(15, 2), key='-JOIN_SESSION-'), sg.Button('Refresh', pad=5, size=(15, 2), key='-REFRESH_SESSIONS-')],
            [sg.Button('Delete Session', pad=5, size=(15, 2), key='-DELETE_SESSION-')]
        ]
        create_session_box = [
            [sg.Text('Session name:'), sg.Input(size=(20, 1), key='-SESSION_NAME-')],
            [sg.Checkbox('Private', key='-PRIVATE-', default=False)],
            [sg.Button('Create Session', pad=20, size=(15, 2), key='-CREATE_SESSION-')],
        ]

        self.layout = [
            [sg.Push(), sg.Text("Logged in as: "), sg.Text("", key='-USERNAME-', size=(20, 1)), sg.Button('Logout', size=(10, 1), key='-LOGOUT-'), sg.Push()],
            [sg.Frame('Join a session', session_box, pad=(20, 15)), sg.Push(), sg.Frame('Create a session', create_session_box, pad=(20, 15))],
            [sg.VPush()],
            [sg.Push(),sg.Text("upload a CSV:"), sg.Input(key="-FILE-", enable_events=True), sg.FileBrowse(button_text='Browse', file_types=(('CSV Files', '*.csv'),)), sg.Push(),],
            [sg.Push(),sg.Text('Data name:'), sg.Input(size=(40, 5), key='-DATA-NAME-'), sg.Button('Upload', key='-UPLOAD_DATA-'), sg.Push(),],
        ]
        
        self.window = sg.Window("Remote Mode", self.layout, size=(700, 500), finalize=True)
        
    def refresh_sessions(self, sessions):
        self.window['-SESSION_LIST-'].update(sessions)  
        
    def close(self):
        self.window.close()
        
    def show_error(self, message):
        sg.popup_error(message)

    def show_message(self, message):
        sg.popup(message)