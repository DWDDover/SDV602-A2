from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline
from reference_tasks.class_tasks.password_gen import generate_password


def make_window():
    
    layout = [
        [Text("Password Generator", font="Any 20", pad=((0, 0), (0, 20)))],
        [Text("Length:"), Input(key="-LENGTH-", default_text="8", size=(30, 1))],
        [
            Checkbox("Capitals", key="-CAPITALS-", default=True), 
            Checkbox("Symbols", key="-SYMBOLS-"), 
            Checkbox("Numbers", key="-NUMBERS-", default=True)
        ],
        [Button("Generate", key="-GENERATE-")],
        [Multiline(key="-OUTPUT-", size=(400, 30))]
    ]
    
    return Window("Password Generator", layout)

def password_generator():
    window = make_window()

    while True:
        event, values = window.read()
        
        if event == "-GENERATE-":
            length = int(values["-LENGTH-"])
            capitals = values["-CAPITALS-"]
            symbols = values["-SYMBOLS-"]
            numbers = values["-NUMBERS-"]
            
            if length < 8:
                window["-OUTPUT-"].update("Minimum length of 8 characters")
                continue
            
            password = generate_password(
                length=length,
                capitals=capitals,
                symbols=symbols,
                numbers=numbers,
            )
            
            window["-OUTPUT-"].update(password)
        
        if event == WIN_CLOSED:
            break


if __name__ == "__main__":
    password_generator()