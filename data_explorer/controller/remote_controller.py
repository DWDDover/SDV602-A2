from data_explorer.data.file_manager import FileManager

class RemoteController:
    
    def __init__(self, user):
        self.user = user
        self.file_manager = FileManager()
        

    def run(self):
        pass