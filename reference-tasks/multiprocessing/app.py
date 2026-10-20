from chat_app import run as chat_run
from multiprocessing import Process
import FreeSimpleGUI as sg

def run():
    layout = [
        [sg.Button("Open Chat")]
    ]
    
    window = sg.Window("Launcher", layout, size=(200,100))
    
    active_chats = []
    
    while True:
        event, values = window.read(timeout=1000)
        
        if event == sg.WIN_CLOSED:
            break

        if event == "Open Chat":
            process = Process(target=chat_run)
            process.start()
            active_chats.append(process)
            
    for process in active_chats:
        if process.is_alive():
            process.terminate()
            
    window.close()
            
            
if __name__ == "__main__":
    chat_run()
