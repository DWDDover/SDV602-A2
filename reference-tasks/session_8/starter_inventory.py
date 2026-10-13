import FreeSimpleGUI as sg
from game import Game, Player


# Game state and map definition. Each place contains text
# to display to the player, connected places via directions, and a colour.

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

    colour = game.showCurrentLocation().color
    graph = sg.Graph(
        canvas_size=(100, 100),
        graph_bottom_left=(0, 0),
        graph_top_right=(100, 100),
        key='-CANV-',
        background_color=colour,
    )

    layout = [
        [graph, sg.Text('HP: ' + str(game.player.currentHp) + '/' + str(game.player.maxHp) +
                        ' DMG: ' + str(game.player.damage) + ' BLOCK: ' + str(game.player.block) +
                        '\n' + game.showCurrentLocation().story, size=(
            100, 4), font='Any 12', key='-OUTPUT-')],
        [command_col],
    ]
    return sg.Window('Adventure Game', layout, size=(400, 200))


if __name__ == "__main__":
    player = Player(currentHp = 50)
    game = Game(player)
    
    window = make_a_window()

    while True:
        event, values = window.read()
        if event == 'Enter':
            command_success = False
            current_story = game.showCurrentLocation().story
            if 'north' in values['-IN-'].lower():
                new_location = game.move(game.locations[game.showCurrentLocation().north])
                if new_location:
                    current_story = new_location
                    command_success = True
            elif 'south' in values['-IN-'].lower():
                new_location = game.move(game.locations[game.showCurrentLocation().south])
                if new_location:
                    current_story = new_location
                    command_success = True
            elif 'search' in values['-IN-'].lower():
                item = game.showCurrentLocation().item
                if game.inventory.addItem(item):
                    current_story = 'You found a ' + item.name + \
                        '!\n' + game.showCurrentLocation().story
                else:
                    current_story = 'You already found the ' + \
                        item.name + '.\n' + game.showCurrentLocation().story
                command_success = True

            # use or equip an item
            # elif 'use ' in values['-IN-'].lower():
            #     use_item_name = values['-IN-'].lower().replace('use ',
            #                                                    '').strip()
            #     current_story = ''
            #     item = game.inventory.getItem(use_item_name)
            #     if game.inventory.hasItem(item):
            #         if item.equipped:
            #             if item.equipped:
            #                 item['equipped'] = False
            #                 player['damage'] -= item['damage']
            #                 player['block'] -= item['block']
            #                 current_story = 'You unequipped ' + \
            #                     item['name'] + '.\n'
            #             else:
            #                 item['equipped'] = True
            #                 player['damage'] += item['damage']
            #                 player['block'] += item['block']
            #                 current_story = 'You equipped ' + \
            #                     item['name'] + '.\n'
            #         elif 'used' in item:
            #             if not item['used']:
            #                 item['used'] = True
            #                 player['health_current'] += item['heal']
            #                 if player['health_current'] > player['health_max']:
            #                     player['health_current'] = player['health_max']
            #                 current_story = 'You used ' + item['name'] + '.\n'
            #             else:
            #                 current_story = item['name'] + ' already used.\n'
            #     else:
            #         current_story = 'You do not have ' + use_item_name + '.\n'
            #     current_story += game.showCurrentLocation().story
            #     command_success = True

            if command_success:
                window['-OUTPUT-'].update(
                    'HP: ' + str(game.player.currentHp) + '/' + str(game.player.maxHp) +
                    ' DMG: ' + str(game.player.damage) + ' BLOCK: ' + str(game.player.block) +
                    '\n' + str(current_story)
                )
                window['-IN-'].update('')

            # Update the Graph's background colour to reflect the new location.
            colour = game.showCurrentLocation().color
            window['-CANV-'].update(background_color=colour)

        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break
    window.close()
