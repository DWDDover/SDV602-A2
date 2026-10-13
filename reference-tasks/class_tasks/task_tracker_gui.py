from FreeSimpleGUI import Window, Button, Text, Input, Checkbox, WIN_CLOSED, Multiline, Radio


tasks = []

def make_window():
    
    layout = [
        [Text("Task Tracker", font="Any 20", pad=((0, 0), (0, 20)))],
        [Text("Task Name:"), Input(key="-NAME-", size=(30, 1))],
        [Text("Priority:", font="Any 15", pad=((0, 0), (0, 20)))],
        [
            Radio("Low", "PRIO_GROUP", key="-PRIORITY-", default=True), 
            Radio("Medium", "PRIO_GROUP", key="-PRIORITY-"), 
            Radio("High", "PRIO_GROUP", key="-PRIORITY-",)
        ],
        [Button("Add", key="-ADD-")],
        [Multiline(key="-LIST-", size=(100, 30))]
    ]
    
    return Window("Task Tracker", layout)

def add_task(
    *,
    name,
    priority,
    complete,
):
    tasks.append({
            'name' : name,
            'priority' : priority,
            'complete' : complete,
            })

def task_tracker():
    window = make_window()

    while True:
        event, values = window.read()
        
        if event == "-ADD-":
            name = values["-NAME-"]
            priority = values["-PRIORITY-"]
            
            if len(name) < 3:
                window["-OUTPUT-"].update("Minimum length of 3 characters")
                continue
            
            add_task(
                name=name,
                priority=priority,
                complete=False,
            )
            
            for task in tasks:
                window["-LIST-"].update(task)
        
        if event == WIN_CLOSED:
            break

if __name__ == "__main__":
    task_tracker()