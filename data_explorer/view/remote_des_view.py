import FreeSimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure



class RemoteDESView:

    def __init__(self, chart_data, name="Remote Data Exploration Session"):
        sg.theme("LightGreen9")
        
        upload_data_box = [
            [
                sg.Text("upload a CSV:"), 
                sg.Input(key="-FILE-", enable_events=True), 
                sg.FileBrowse(button_text='Browse', file_types=(('CSV Files', '*.csv'),)), 
            ],
            [
                sg.Text('Data name:'), 
                sg.Input(size=(40, 5), key='-DATA-NAME-'), 
                sg.Button('Upload', key='-UPLOAD-FILE-'), 
            ],
            [
                sg.Text('Append data:'),
            ],
            [
                sg.Combo(values=['Select data to append'], size=(40, 5), key='-APPEND-FILE-')
            ],
            [
                sg.Button('Append Data', pad=20, size=(15, 2), key='-APPEND-DATA-'),
            ]
        ]
        
        new_chart_box = [
            [
                sg.Text('Replace data:'),
                sg.Combo(key="-REPLACE-FILE-", size=(40, 5), values=['Select a new CSV file'], enable_events=True),
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
            [sg.Button('Generate Chart', pad=20, size=(15, 2), key='-GENERATE-CHART-')],
        ]
        
        chat_box = [
            [sg.Multiline(size=(50, 20), disabled=True,
                          autoscroll=True, key='-OUTPUT-')],
            [sg.Input(size=(40, 5), key='-CHAT-', do_not_clear=True)],
            [sg.Button('Send', bind_return_key=True)]
        ]

        self.layout = [
            [sg.Push(), sg.Text(f"{name}"), sg.Push()],
            [sg.Canvas(size=(640, 520), key='-CANVAS-'), sg.Frame('Chat', chat_box)],
            [
                sg.Frame('Upload or append data', upload_data_box), 
                sg.Frame('Replace data', new_chart_box),
            ],
        ]
        
        self.window = sg.Window(name, self.layout, finalize=True)
        self.figure = Figure(figsize=(6.4, 4.2), dpi=100)
        self.axes = self.figure.add_subplot(111)
        
        tk_canvas = self.window["-CANVAS-"].TKCanvas
        self.canvas = FigureCanvasTkAgg(self.figure, master=tk_canvas)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        self.toolbar = NavigationToolbar2Tk(self.canvas, tk_canvas)
        self.toolbar.update()
        self.toolbar.pack(fill="x", expand=False)
        
        if chart_data:  
            self.draw_chart(chart_data)

    def update_dropdowns(self, columns):
        self.window["-SERIES_KEY-"].update(values=(columns))
        self.window["-X-KEY-"].update(values=(columns))
        self.window["-Y-KEY-"].update(values=(columns))
        
    def update_combos(self, user_sources):
        self.window["-REPLACE-FILE-"].update(values=user_sources)
        self.window["-APPEND-FILE-"].update(values=user_sources)

    def draw_chart(self, chart_data):
        
        ##for intial session creation before data is chosen
        if chart_data is None:
            self.axes.clear()
            self.axes.set_title("No data available")
            self.canvas.draw()
            return
        
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