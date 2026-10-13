from FreeSimpleGUI import Text, Window, WIN_CLOSED


def create_window():

    main_text = Text('Hello World!', font=('Any', '20', 'italic'))

    layout = [
        [main_text]
    ]

    return Window('Demo', layout, size=(200, 100))


if __name__ == "__main__":
    window = create_window()

    while True:
        event, values = window.read()

        if event == WIN_CLOSED:
            break
