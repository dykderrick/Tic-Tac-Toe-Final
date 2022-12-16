class Board:
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __str__(self):
        rows = ""
        for i in range(3):
            current_row = ""
            for j in range(3):
                if self.board[i][j] is not None:
                    current_row += self.board[i][j]
                else:
                    current_row += "_"

                current_row += " "

            rows += current_row + "\n"

        return rows

    def set_board(self, x: int, y: int, player_symbol: str):
        """
        Set board element at (x, y) to a specific symbol (either X or O).

        :param x: the x coordinate of board to set
        :param y: the y coordinate of board to set
        :param player_symbol: either X or O
        :return: None
        """
        self.board[x][y] = player_symbol

    def get_board_element(self, i: int, j: int):
        return self.board[i][j]

    def get_board(self):
        return self.board
