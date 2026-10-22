import sys
from pathlib import Path

## allows for running the app from the command line without having to install it as a package
if not __package__:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data_explorer.testing.test_app import testing_run
from data_explorer.local_app import local_run
from data_explorer.remote_app import remote_run

TESTING = '--testing' in sys.argv
REMOTE = '--remote' in sys.argv
LOCAL = '--local' in sys.argv

if __name__ == "__main__":
    
    if TESTING:
        testing_run()
    
    elif REMOTE:
        remote_run()
        
    elif LOCAL:
        local_run()
        
        
    