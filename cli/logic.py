# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def get_board_filled_num(board):
    num = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                num += 1

    return num


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""

    # If a player wants to win Tic-Tac-Toe,
    # these are all possible combinations
    # for a player to win the game.
    wins = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def check_win(S) -> bool:
        """
        Check if a set of a player's pieces leads to win.
        :param S: a set
        :return: True if the set can lead to win otherwise False
        """
        for win in wins:
            flag = True
            for pos in win:
                if pos not in S:
                    flag = False
                    break
            if flag:
                return True

        return False

    x_set, o_set = set(), set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                x_set.add((i, j))
                if check_win(x_set):
                    return "X"
            elif board[i][j] == "O":
                o_set.add((i, j))
                if check_win(o_set):
                    return "O"

    # Otherwise let the game continue
    return None if get_board_filled_num(board) != 9 else "DRAW"


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O" if player == "X" else "X"
