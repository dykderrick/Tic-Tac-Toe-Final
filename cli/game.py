import random
import uuid
import utils

from typing import Tuple

from board import Board
from log import Logger
from logic import get_winner
from player import Player
from statistics import GlobalRank


class Game:
    def __init__(self):
        self.game_id = uuid.uuid4()
        self.game_mode = 0  # 1 means one-gamer (user vs bot), 2 means two-player (user vs user)
        self.board = Board()
        self.players = []
        self.winner = None

    def add_player(self, player: Player):
        self.players.append(player)

    def get_winner(self):
        return self.winner

    def get_players(self):
        return self.players

    def get_game_id(self):
        return self.game_id

    def game_interface(self):
        pass


class SingleModeGame(Game):
    def __init__(self):
        super().__init__()
        self.is_user_turn = True

    def _get_empty_space(self):
        space = []

        for i in range(3):
            for j in range(3):
                if self.board.get_board_element(i, j) is None:
                    space.append((i, j))

        return space

    def bot_random_step(self) -> Tuple:
        _empty_space = self._get_empty_space()

        return _empty_space[random.randint(0, len(_empty_space) - 1)]

    def game_interface(self):
        _is_valid_username = False
        _username = ""

        while not _is_valid_username:
            _username = input("X, Please enter your username: ")

            _is_valid_username = utils.validate_username(_username)

            if not _is_valid_username:
                print("USERNAME CANNOT BE BOT. PLEASE TRY AGAIN.")

        print("X Player: " + _username)

        x_player = Player(player_username=_username, is_x=True, is_bot=False)
        o_player = Player(player_username=_username, is_x=False, is_bot=True)

        self.add_player(x_player)  # user is the first player
        self.add_player(o_player)

        while self.winner is None:
            if not self.is_user_turn:
                print("Bot takes a turn!")

                bot_step = self.bot_random_step()

                print("Bot takes " + str(bot_step))

                self.board.set_board(bot_step[0], bot_step[1], "O")  # bot always takes O

            else:
                print(str(self.players[0]) + " takes a turn!")

                # Show the board to the user.
                print("CURRENT BOARD: ")
                print(self.board)

                # Input a move from the player.
                valid_input = False
                _x, _y = "", ""

                while not valid_input:
                    _x = input("Enter Coordinate For Row (zero-index): ")
                    _y = input("Enter Coordinate For Col (zero-index): ")

                    valid_input = utils.validate_input(self.board.get_board(), _x, _y)

                    if not valid_input:
                        print("INVALID INPUT. PLEASE RE-ENTER.")

                print("Your input is (%s, %s)" % (_x, _y))

                # Update the board.
                coordinate = (int(_x), int(_y))
                self.board.set_board(coordinate[0], coordinate[1], "X")  # User always takes O

            # Print the board
            print("CURRENT BOARD: ")
            print(self.board)

            # Update who's turn it is.
            self.is_user_turn = not self.is_user_turn

            self.winner = get_winner(self.board.get_board())

            print("---------------------------------------")

        if self.winner == "DRAW":
            print("GAME OVER. DRAW.")
        else:
            print("GAME OVER. " + self.winner + " WINS.")

        Logger(self).log()

        print(GlobalRank())


class TwoPlayerModeGame(Game):
    def __init__(self):
        super().__init__()
        self.current_player = None
        self.current_player_index = -1

    def game_interface(self):
        _is_valid_x_username, _is_valid_o_username = False, False
        _x_username, _o_username = "", ""

        while not _is_valid_x_username:
            _x_username = input("X, Please enter your username: ")
            _is_valid_x_username = utils.validate_username(_x_username)

            if not _is_valid_x_username:
                print("USERNAME CANNOT BE BOT. PLEASE TRY AGAIN.")

        print("X Player: " + _x_username)

        while not _is_valid_o_username:
            _o_username = input("O, Please enter your username: ")
            _is_valid_o_username = utils.validate_username(_o_username)

            if not _is_valid_o_username:
                print("USERNAME CANNOT BE BOT. PLEASE TRY AGAIN.")

        print("O Player: " + _o_username)

        x_player = Player(player_username=_x_username, is_x=True, is_bot=False)
        o_player = Player(player_username=_o_username, is_x=False, is_bot=False)

        self.add_player(x_player)
        self.add_player(o_player)

        current_player_index = 0  # x_player
        self.current_player = self.players[current_player_index]

        # business logic starts here
        while self.winner is None:
            print(str(self.current_player) + " takes a turn!")

            # Show the board to the user.
            print("CURRENT BOARD: ")
            print(self.board)

            # Input a move from the player.
            valid_input = False
            _x, _y = "", ""

            while not valid_input:
                _x = input("Enter Coordinate For Row (zero-index): ")
                _y = input("Enter Coordinate For Col (zero-index): ")

                valid_input = utils.validate_input(self.board.get_board(), _x, _y)

                if not valid_input:
                    print("INVALID INPUT. PLEASE RE-ENTER.")

            print("Your input is (%s, %s)" % (_x, _y))

            # Update the board.
            coordinate = (int(_x), int(_y))
            self.board.set_board(coordinate[0], coordinate[1], self.current_player.get_player_symbol())

            # Print the board
            print("CURRENT BOARD: ")
            print(self.board)

            # Update who's turn it is.
            current_player_index ^= 1  # XOR with 1 to toggle
            self.current_player = self.players[current_player_index]

            self.winner = get_winner(self.board.get_board())

            print("---------------------------------------")

        if self.winner == "DRAW":
            print("GAME OVER. DRAW.")
        else:
            print("GAME OVER. " + self.winner + " WINS.")

        Logger(self).log()

        print(GlobalRank())
