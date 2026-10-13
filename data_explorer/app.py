from data_visualiser import DataVisualiser
from data_source import DataSource
from login_view import LoginView
from remote.remote_app import remote_run
from local.local_app import local_run
from user import User


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
            login_view.close()
            local_run()
        
        if event == "__WINDOW_CLOSED__":
            login_view.close()
            break

    if user is not None:
        login_view.close()
        remote_run(user)
