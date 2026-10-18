import FreeSimpleGUI as sg


class RegisterView:

    def __init__(self):
        sg.theme("DarkRed1")

        self.layout = [
            [sg.Push(), sg.Text('Username: ', font='Any 14'), sg.Input(size=(40, 5), key='-USERNAME-', do_not_clear=True), sg.Push()],
            [sg.Push(), sg.Text('Password: ', font='Any 14'), sg.Input(size=(40, 5), key='-PASSWORD-', do_not_clear=True), sg.Push()],
            [sg.Push(), sg.Text('Repeat password: ', font='Any 14'), sg.Input(size=(40, 5), key='-REPEAT_PASSWORD-', do_not_clear=True), sg.Push()],
            [sg.Button('Create Account', pad=20, size=(15, 2), bind_return_key=True)],
        ]

        self.window = sg.Window("Register", self.layout, finalize=True)

    def clear_input(self):
        self.window['-USERNAME-'].update('')
        self.window['-PASSWORD-'].update('')
        self.window['-REPEAT_PASSWORD-'].update('')

    def close(self):
        self.window.close()

    def show_error(self, message):
        sg.popup_error(message)

    def show_message(self, message):
        sg.popup(message)