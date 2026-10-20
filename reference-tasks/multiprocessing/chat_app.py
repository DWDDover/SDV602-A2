from chat_view import ChatView
import config
import FreeSimpleGUI as fsg
from chat_message import ChatMessage

def run():
    username = fsg.popup_get_text("Enter Username:", "Live Chat")
    
    if not username:
        return
    
    view = ChatView()
    
    while True:
        event, values = view.read(config.POLL_RATE)
        
        if event == fsg.WIN_CLOSED:
            break
        
        if event == "__TIMEOUT__":
            messages = ChatMessage.all()
            
            output = ""
            
            for message in messages:
                output += f"{message.username}: {message.text} \n"
        
            view.update_messages(output)
            
        if event == "Send":
            text = values["-CHAT-"]
            
            if text:
                ChatMessage(username, text).save()
                view.clear_input()
                
    view.close()