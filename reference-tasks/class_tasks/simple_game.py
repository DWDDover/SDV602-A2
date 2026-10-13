import FreeSimpleGUI as sg

# Game state and map definition. Each place contains text
# to display to the player, connected places via directions, and a colour.
game_state = 'Forest'
game_places = {
    'Forest': {
        'Story': 'You are in the forest.\nTo the north is a cave.\nTo the south is a castle',
        'North': 'Cave',
        'South': 'Castle',
        'Colour': "#0000FF",
    },
    'Cave': {
        'Story': 'You are at the cave.\nTo the south is forest.',
        'North': '',
        'South': 'Forest',
        'Colour': "#FF0000",
    },
    'Castle': {
        'Story': 'You are at the castle.\nTo the north is forest.',
        'North': 'Forest',
        'South': '',
        'Colour': '#00FF00',
    },
}


def show_current_place():
    """Return the story text for the current `game_state`.

    Kept as a separate function so the GUI layout can call it when
    building the initial window contents.
    """
    global game_state
    return game_places[game_state]['Story']


def game_play(direction):
    """Attempt to move in `direction`.

    Returns the new location story string or an error message when the
    move is not allowed.
    """
    global game_state

    # Check the direction is available
    if direction.lower() in ('north', 'south'):
        game_place = game_places[game_state]
        proposed_state = game_place[direction]
        if proposed_state == '':
            return 'You can not go that way.\n' + game_places[game_state]['Story']
        else:
            # Change the global state and return the new place text
            game_state = proposed_state
            return game_places[game_state]['Story']


def make_a_window():
    """Create and return the main application window.

    The left area is a coloured `sg.Graph` element used to represent the current location.
    The right area shows the description and a text input.
    """
    sg.theme('Dark Blue 3')

    prompt_input = [
        sg.Text('Enter your command', font='Any 14'),
        sg.Input(key='-IN-', size=(20, 1), font='Any 14'),
    ]
    buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')

    colour = game_places[game_state].get('Colour', '#000000')
    graph = sg.Graph(
        canvas_size=(100, 100),
        graph_bottom_left=(0, 0),
        graph_top_right=(100, 100),
        key='-CANV-',
        background_color=colour,
    )

    layout = [
        [graph, sg.Text(show_current_place(), size=(
            100, 4), font='Any 12', key='-OUTPUT-')],
        [command_col],
    ]
    return sg.Window('Adventure Game', layout, size=(320, 200))


if __name__ == "__main__":
    window = make_a_window()

    while True:
        event, values = window.read()
        if event == 'Enter':
            if 'North'.lower() in values['-IN-'].lower():
                current_story = game_play('North')
                window['-OUTPUT-'].update(current_story)
            elif 'South'.lower() in values['-IN-'].lower():
                current_story = game_play('South')
                window['-OUTPUT-'].update(current_story)

            # Update the Graph's background colour to reflect the new location.
            colour = game_places[game_state].get('Colour', '#000000')
            window['-CANV-'].update(background_color=colour)

        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
    window.close()
