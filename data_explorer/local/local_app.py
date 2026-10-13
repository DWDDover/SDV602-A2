from .local_view import LocalView
from ..data_visualiser import DataVisualiser
from ..data_source import DataSource
import config
import FreeSimpleGUI as fsg


def local_run():
    
    view = LocalView()
    
    
    view.close()