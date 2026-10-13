import FreeSimpleGUI as sg
from game import Game

class GUI():
    def __init__(self, game: Game):
        self.game = game
        self.window = self.create_window(self, game)
        
    def create_window(self, game):
        """Create and return the main application window.

        The left area is a coloured `sg.Graph` element used to represent the current location.
        The right area shows the description and a text input.
        """
        game = self.game
        
        sg.theme('Dark Blue 3')

        prompt_input = [
            sg.Text('Enter your command', font='Any 14'),
            sg.Input(key='-IN-', size=(20, 1), font='Any 14'),
        ]
        buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]
        command_col = sg.Column([prompt_input, buttons], element_justification='r')

        colour = game.get_current_location().colour

        graph = sg.Graph(
            canvas_size=(100, 100),
            graph_bottom_left=(0, 0),
            graph_top_right=(100, 100),
            key='-CANV-',
            background_color=colour,
        )

        layout = [
            [graph, sg.Text('HP: ' + str(game.player.health_current) + '/' + str(game.player.health_max) +
                            ' DMG: ' + str(game.player.damage) + ' BLOCK: ' + str(game.player.block) +
                            '\n' +
                            str(game.get_current_location().story), size=(
                100, 4), font='Any 12', key='-OUTPUT-')],
            [command_col],
        ]
        return sg.Window('Adventure Game', layout, size=(400, 200))
    
    def run(self):
        while True:
            event, values = window.read()
            if event == 'Enter':
                command_success = False
                current_story = game.get_current_location().story
    
                if 'north' in values['-IN-'].lower():
                    current_location = game.get_current_location()
                    if current_location.north:
                        proposed_location = game.locations[current_location.north]
                        game.move(proposed_location)
                        command_success = True
    
                elif 'south' in values['-IN-'].lower():
                    current_location = game.get_current_location()
                    if current_location.south:
                        proposed_location = game.locations[current_location.south]
                        game.move(proposed_location)
                        command_success = True
    
                elif 'search' in values['-IN-'].lower():
                    item = game.get_current_location().item
    
                    if game.inventory.add_item(item):
                        current_story = 'You found a ' + item.name + \
                            '!\n' + game.get_current_location().story
    
                    else:
                        current_story = 'You already found the ' + \
                            item.name + '.\n' + game.get_current_location().story
                    command_success = True
    
                # use or equip an item
                # elif 'use ' in values['-IN-'].lower():
                #     use_item_name = values['-IN-'].lower().replace('use ',
                #                                                    '').strip()
                #     current_story = ''
                #     item = inventory[use_item_name]
                #     if item['has_item']:
                #         if 'equipped' in item:
                #             if item['equipped']:
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
                #     current_story += game_places[game_state]['Story']
                #     command_success = True
    
                if command_success:
                    window['-OUTPUT-'].update(value='HP: ' + str(game.player.health_current) + '/' + str(game.player.health_max) +
                                              ' DMG: ' + str(game.player.damage) + ' BLOCK: ' + str(game.player.block) +
                                              '\n' +
                                              str(game.get_current_location().story)
                                              )
                    window['-IN-'].update(value='')
    
                # Update the Graph's background colour to reflect the new location.
                colour = game.get_current_location().colour
                window['-CANV-'].update(background_color=colour)
    
            elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
                break
            
        window.close()