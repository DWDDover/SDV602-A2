from .remote_view import RemoteView
from ..data_visualiser import DataVisualiser
from ..data_source import DataSource
import config
import FreeSimpleGUI as fsg



def remote_run(user):
    
    username = user.username
    
    if not username:
        return
    
    view = RemoteView()
    
    
    view.close()