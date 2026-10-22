import FreeSimpleGUI as sg


class LoginView:

    def __init__(self):
        sg.theme("DarkRed1")

        self.layout = [
            [sg.Push(), sg.Text('Username: ', font='Any 14'), sg.Input(size=(40, 5), key='-USERNAME-', do_not_clear=True), sg.Push()],
            [sg.Push(), sg.Text('Password: ', font='Any 14'), sg.Input(size=(40, 5), key='-PASSWORD-', password_char='*', do_not_clear=True), sg.Push()],
            [
            (sg.Button('Login', pad=20, size=(15, 2), bind_return_key=True)),
            (sg.Button('Register', pad=20, size=(15, 2), bind_return_key=True)),
            (sg.Button('Local Mode', pad=20, size=(15, 2), bind_return_key=True))
            ]
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