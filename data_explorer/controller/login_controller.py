import FreeSimpleGUI as sg

from data_explorer.controller.remote_controller import RemoteController
from data_explorer.data.user_repository import UserRepository
from data_explorer.view.login_view import LoginView
from data_explorer.view.register_view import RegisterView

class LoginController:
    
    def run(self):
        ur = UserRepository()
        login_view = LoginView()
        user = None

        while user is None:
            event, values = login_view.window.read()

            if event == sg.WIN_CLOSED:
                login_view.close()
                break

            if event in ("Login", "__TIMEOUT__"):
                user = ur.login(values["-USERNAME-"], values["-PASSWORD-"])

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
                    new_user = ur.register(values["-USERNAME-"], values["-PASSWORD-"])

                    if new_user is not None:
                        register_view.show_message("User created successfully")
                        register_view.close()
                        continue
                    
                    else:
                        register_view.show_error("Username already exists.")

        if user is not None:
            login_view.close()
            remote_controller = RemoteController(user)
            remote_controller.run()
        