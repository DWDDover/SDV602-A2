import sys
from data_explorer.testing.test_app import testing_run
from local_app import local_run
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
        
        
    