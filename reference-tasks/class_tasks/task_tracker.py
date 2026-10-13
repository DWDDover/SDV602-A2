# Session 4 - Task Tracking System

# Define your tasks list
# You may change this to a different data structure if you want
tasks = []

# Main application loop


mainMenu = {
    '1.' : {'text' : 'Add task'},
    '2.' : {'text' : 'View tasks'},
    '3.' : {'text' : 'Mark complete'},
    '4.' : {'text' : 'Exit application'},
}
        
def printMainMenu():
    print('Please select a menu item:')
    for key, value in mainMenu.items():
        print(key, value['text'])
                
def addTask():
    print('Enter task name:')
    taskName = input()
    while True:
        print('Enter task priority: (low, medium, high)')
        userInput = input()
        if userInput.lower() in {'low', 'medium', 'high'}:
            priority = userInput
            break
        else:
            print('Invalid priority')
            continue
    tasks.append({
        'name' : taskName,
        'priority' : priority,
        'status' : 'Incomplete',
        })
    
def viewTasks():
    for index, t in enumerate(tasks):
        print(index+1, 'Task Name: ', t['name'], 'Task priority: ', t['priority'], 'Status: ', t['status'])


def markComplete():
    viewTasks()
    while True: 
        print('Enter task index to mark complete: ')
        selection = int(input())-1
        try:
            tasks[selection]['status'] = 'Complete'
            break
        except:
            print('Please select a valid task:')
            continue

def task_tracker():
    run_flag = True
    while run_flag:
        
        # Print menu (Add task, View tasks, Mark complete, Exit)

        printMainMenu()
        # Get user choice
        selection = int(input())
        # Handle choice "1" - Add task
        # Ask for name, priority (low, medium, high), add to task storage
        # Validate priority input, whether string literal or a correlated number
        if selection == 1:
            addTask()
        # Handle choice "2" - View tasks
        # Loop through tasks and display the name, priority, and status
        elif selection == 2:
            if len(tasks) > 0:
                viewTasks()
            else:
                print('No tasks')
        # Handle choice "3" - Edit tasks
        elif selection == 3:
            if len(tasks) > 0:
                markComplete()
            else:
                print('No tasks')
        # Show a numbered list (id/index - task), prompt for task number
        # Show a set of edit options for task, priority, and status (this is how a task is set as completed)
        elif selection == 4:
            run_flag = False
            break
        # Handle choice "4" - Exit
        # The user should be able to exit at any point of the program with the command 'exit'
        else: 
            print('Invalid menu item')
        # Handle invalid choice

        pass  # remove this


if __name__ == "__main__":
    task_tracker()
