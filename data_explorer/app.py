from data_visualiser import DataVisualiser
from data_source import DataSource
from login_view import LoginView
from remote.register_view import RegisterView
from local.local_view import LocalView
from user import User

from chat_app import run


if __name__ == "__main__":
    login_view = LoginView()
    user = None

    while user is None:
        event, values = login_view.window.read()

        if event in ("Login", "__TIMEOUT__"):
            user = User.login(values["-USERNAME-"], values["-PASSWORD-"])

            if user is None:
                login_view.show_error("Invalid username or password.")
            else:
                break

        if event == "Login" and user is None:
            login_view.clear_input()

        if event == "Register":
            register_view = RegisterView()
            event, values = register_view.window.read()
            
            if event == "Create Account":
                new_user = User(values["-USERNAME-"], values["-PASSWORD-"])

                if new_user.save():
                    register_view.show_message("User created successfully")
                    register_view.close()
                    continue
                
                else:
                    register_view.show_error("Username already exists.")
                    
        if event == "Local Mode" :
            local_view = LocalView()
            event, values = local_view.window.read()
        
        if event == "__WINDOW_CLOSED__":
            login_view.close()
            break

    if user is not None:
        login_view.close()
        run(user)
