# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from game import *
import utils


if __name__ == '__main__':
    print("Please Select a Game Mode:")
    print("1 - One Player Mode")
    print("2 - Two Player Mode")

    valid_input_game_mode = False
    _game_mode = ""

    while not valid_input_game_mode:
        _game_mode = input("Enter number: ")

        valid_input_game_mode = utils.validate_game_mode_input(_game_mode)

        if not valid_input_game_mode:
            print("INVALID INPUT. PLEASE RE-ENTER.")

    game_mode = int(_game_mode)

    game = None

    if game_mode == 1:
        print("You are on One Player Mode")
        game = SingleModeGame()
    elif game_mode == 2:
        print("You are on Two Player Mode")
        game = TwoPlayerModeGame()

    board = game.board.get_board()
    winner = game.get_winner()

    current_player = "X"

    print()
    print("GAME START")
    print("---------------------------------------")

    game.game_interface()
