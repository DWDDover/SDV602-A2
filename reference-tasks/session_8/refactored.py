import FreeSimpleGUI as sg
from player import Player
from game import Game
from gui import GUI

if __name__ == "__main__":
    player = Player(
        health_current=50
    )
    game = Game(player)

    gui = GUI(game)


