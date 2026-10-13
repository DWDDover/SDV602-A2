# Session 3 - Pizza Ordering System

# Build a console-based pizza ordering system.
# Follow the TODO sections below.

# TODO: Define your menu as a dictionary
# Keys = pizza ID (int)
# Values = dict with "name" (str) and "price" (float)
# Example:
# {1: {"name": "Meatlovers", "price": 10.00},
#  2: {"name": "Hawaiian", "price": 8.50}}

# TODO: Write a function to display the menu

# TODO: Write a function to display the current order
# Order is a list of tuples: [(pizza_id, quantity), ...]

# TODO: Write the main function
# - Show menu
# - While loop for user input
# - Validate input using try/except
# - Allow user to: select pizza by ID, view order, exit
# - Track order as list of (pizza_id, quantity) tuples
# - Print final order summary and total cost on exit

# TODO: Entry point

menu = {
    '1' : {
        "name" : "Hawaiian",
        "price" : "10.00"
    },
    '2' : {
        "name" : "Pepperoni",
        "price" : "11.00"
    },
    '3' : {
        "name" : "Vegetarian",
        "price" : "9.00"
    },
    '4' : {
        "name" : "Deluxe",
        "price" : "15.00"
    },   
}

order = []

def showMenu(menu):
    for key, value in menu.items():
        print(key + ': ')
        print('Pizza Name: ', value.get('name'))
        print('Price: $', value.get('price'))


def printOrder(order, total):
    for i in order:
        print(i.get('name'), i.get('price'))
    print('Total Cost: $', total)



def main():
    run_flag = True
    total = 0.00
    showMenu(menu)
    while run_flag:
        print('Please enter the number of the selected pizza: ', 'Type exit at any time to exit')
        try:
            selection = input().lower()
            if selection == 'exit':
                run_flag = False
                break
            newPizza = menu.get(selection)
            order.append(newPizza)
            total += float(newPizza.get('price'))
            print('Your current order is: ')
            printOrder(order, total)
        except:
            print('Invalid selection')
            continue
        print('Would you like to add another pizza? (y/n)')
        try:
            selection = input().lower()
            if selection == 'exit':
                run_flag = False
                break
            elif selection == 'y':
                continue
            elif selection == 'n':
                print('Your order is: ')
                printOrder(order, total)
                break
        except:
            print('Please enter a valid option')
            continue
    


if __name__ == "__main__":
     main()
     

