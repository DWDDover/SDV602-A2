import FreeSimpleGUI as sg


class LoginView:

    def __init__(self):
        sg.theme("DarkBlue")

        self.layout = [
            [sg.Text('Username: ', font='Any 14'), sg.Input(size=(40, 5), key='-USERNAME-', do_not_clear=True)],
            [sg.Text('Password: ', font='Any 14'), sg.Input(size=(40, 5), key='-PASSWORD-', do_not_clear=True)],
            [sg.Button('Login', bind_return_key=True)],
            [sg.Button('Register', bind_return_key=True)],
            [sg.Button('Local Mode', bind_return_key=True)],
        ]

        self.window = sg.Window("Login", self.layout, finalize=True)

    def clear_input(self):
        self.window['-USERNAME-'].update('')
        self.window['-PASSWORD-'].update('')

    def close(self):
        self.window.close()

    def show_error(self, message):
        sg.popup_error(message)

    def show_message(self, message):
        sg.popup(message)