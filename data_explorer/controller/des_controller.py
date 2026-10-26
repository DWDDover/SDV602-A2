from data_explorer.view.local_des_view import LocalDESView

class DESController:
     def __init__(self, chart_data):
         self.chart_data = chart_data

     def local_des_run(self):
         
         self.view = LocalDESView(self.chart_data)
         self.view.show()
         
         while True:
             event, values = self.view.window.read()
             if event == sg.WINDOW_CLOSED or event == 'Exit':
                 break
             elif event == 'Close':
                 self.view.close()
                 break