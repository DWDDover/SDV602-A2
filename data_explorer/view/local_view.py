import FreeSimpleGUI as sg


class LocalView:

    def __init__(self):
        sg.theme("LightBlue3")
        
        self.layout = [
            [sg.Push(), sg.Text("Choose a CSV:"), sg.Input(key="-FILE-", enable_events=True), sg.FileBrowse(button_text='Browse', file_types=(('CSV Files', '*.csv'),)), sg.Push()],
            [sg.Push(), sg.Text('Chart Title: ', font='Any 14', pad=(0, 20)), sg.Input(size=(40, 5), key='-TITLE-'), sg.Push()],
            [sg.Push(), sg.Text('x-axis Label: ', font='Any 14', pad=(0, 20)), sg.Input(size=(40, 5), key='-X_AXIS-'), sg.Push()],
            [sg.Push(), sg.Text('y-axis Label: ', font='Any 14', pad=(0, 20)), sg.Input(size=(40, 5), key='-Y_AXIS-'), sg.Push()],
            [sg.Push(), sg.Text('Series Key: ', font='Any 14', pad=(0, 20)), sg.OptionMenu(values=['Select a series key'], size=(40, 5), key='-SERIES_KEY-'), sg.Push()],
            [
            sg.Push(),
            (sg.Button('Generate DES', pad=20, size=(15, 2), bind_return_key=True)),
            (sg.Button('Clear Fields', pad=20, size=(15, 2), bind_return_key=True)),
            sg.Push()
            ]
        ]
        
        self.window = sg.Window("Local Mode", self.layout, size=(900, 430), finalize=True)
        
    def close(self):
        self.window.close()
        
    def show_error(self, message):
        sg.popup_error(message)

    def show_message(self, message):
        sg.popup(message)