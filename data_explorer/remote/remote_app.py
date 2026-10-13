from .remote_view import RemoteView
import config
import FreeSimpleGUI as fsg



def remote_run(user):
    
    username = user.username
    
    if not username:
        return
    
    view = RemoteView()
    
    
    view.close()