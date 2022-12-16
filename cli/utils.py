from typing import List


def validate_game_mode_input(user_input: str) -> bool:
    """
    Validate if user's input for game mode selection is correct or not.
    :param user_input: A string that user inputs.
    :return: True if user input is either 1 or 2, or False otherwise.
    """
    try:
        game_mode = int(user_input)
    except ValueError:
        return False

    return game_mode == 1 or game_mode == 2


def validate_input(board: List[List[str]], user_input_x: str, user_input_y: str) -> bool:
    """
    Validate if user's input coordinate (x and y) is valid or not.
    The coordinate should be in the range of 0 to 2, and cannot be occupied before.
    :param board: The 2d-list of strings for the board.
    :param user_input_x: A string for user's input of coordinate x.
    :param user_input_y: A string for user's input of coordinate y.
    :return: True if the input is valid or False otherwise.
    """
    try:
        x_coordinate = int(user_input_x)
    except ValueError:
        return False

    try:
        y_coordinate = int(user_input_y)
    except ValueError:
        return False

    return 0 <= x_coordinate <= 2 and 0 <= y_coordinate <= 2 and board[x_coordinate][y_coordinate] is None


def validate_username(username: str) -> bool:
    return username != "BOT"
