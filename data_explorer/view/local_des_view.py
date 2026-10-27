import FreeSimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class LocalDESView:

    def __init__(self, chart_data):
        sg.theme("LightBlue3")
        
        new_chart_box = [
            [
                sg.Input(key="-REPLACE-FILE-", enable_events=True),
                sg.FileBrowse(button_text='Browse', file_types=(('CSV Files', '*.csv'),))
            ],
            [sg.Text('New chart options:')],
            [
                sg.Text('Series Key:'),
                sg.OptionMenu(values=['Select a new series key'], size=(40, 5), key='-SERIES_KEY-')
            ],
            [
                sg.Text('x-axis:'),
                sg.OptionMenu(values=['Select a new x-axis value'], size=(40, 5), key='-X-KEY-')
            ],
            [
                sg.Text('y-axis:'),
                sg.OptionMenu(values=['Select a new y-axis value'], size=(40, 5), key='-Y-KEY-'),
            ],
            [sg.Button('Generate new DES', pad=20, size=(15, 2)),],
        ]

        append_data_box = [
            [sg.Input(key="-APPEND-FILE-", enable_events=True), sg.FileBrowse(button_text='Append from file', file_types=(('CSV Files', '*.csv'),))]
        ]

        self.layout = [
            [sg.Push(), sg.Text(f"{chart_data.title}"), sg.Push()],
            [sg.Canvas(size=(640, 520), key='-CANVAS-'), sg.Frame('Replace data', new_chart_box)],
            [sg.Frame('Extend data', append_data_box)]
        ]
        
        self.window = sg.Window(chart_data.title, self.layout, finalize=True)
        self.figure = Figure(figsize=(6.4, 4.2), dpi=100)
        self.axes = self.figure.add_subplot(111)
        
        tk_canvas = self.window["-CANVAS-"].TKCanvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=tk_canvas)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, tk_canvas)
        self.toolbar.update()
        self.toolbar.pack(fill="x", expand=False)
        
        self.draw_chart(chart_data)

    def draw_chart(self, chart_data):
        self.axes.clear()

        for series_name, (x_values, y_values) in chart_data.series.items():
            label = str(series_name) if series_name is not None else None
            self.axes.plot(x_values, y_values, marker="o", label=label)

        self.axes.set_xlabel(chart_data.x_key)
        self.axes.set_ylabel(chart_data.y_key)
        self.axes.set_title(chart_data.title)
        if any(series_name is not None for series_name in chart_data.series):
            self.axes.legend()

        self.figure.tight_layout()
        self.canvas.draw()
        
    def close(self):
        self.window.close()
        
    def show_error(self, message):
        sg.popup_error(message)

    def show_message(self, message):
        sg.popup(message)