import sys
from test_app import run_headless_tests
from local_app import local_run
from remote_app import remote_run

HEADLESS = '--headless' in sys.argv
REMOTE = '--remote' in sys.argv
LOCAL = '--local' in sys.argv

if __name__ == "__main__":
    
    if HEADLESS:
        results = run_headless_tests
        print(results)
    
    elif REMOTE:
        remote_run()
        
    elif LOCAL:
        local_run()
        
        
    