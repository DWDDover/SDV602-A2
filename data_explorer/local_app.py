from data_explorer.controller.local_controller import LocalController
from data_explorer.data.file_manager import FileManager
from data_explorer.view.local_view import LocalView

def local_run():
    file_manager = FileManager()
    local_view = LocalView()
    lc = LocalController(file_manager, local_view)
    lc.run()