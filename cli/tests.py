import unittest
import logic
import utils
from game import SingleModeGame
from board import Board


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        """
        Given a given board for X to win, check if the get_winner function works.
        """
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_make_empty_board(self):
        """
        Given a correct empty board, check if the make_empty_board() function works.
        """
        correct_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        board = Board()

        self.assertEqual(board.get_board(), correct_board)

    def test_other_player(self):
        """
        Given a current player X, check if the other_player() function replies with a O. And check otherwise.
        """
        self.assertEqual(logic.other_player("X"), "O")
        self.assertEqual(logic.other_player("O"), "X")


class TestUtils(unittest.TestCase):
    def test_validate_game_mode_input(self):
        """
        Test game mode input validation function works properly.
        :return:
        """
        self.assertTrue(utils.validate_game_mode_input("1"))
        self.assertTrue(utils.validate_game_mode_input("2"))

        self.assertFalse(utils.validate_game_mode_input("abc"))
        self.assertFalse(utils.validate_game_mode_input("-30"))

    def test_validate_input(self):
        """
        Test player move coordinate input validation function works properly.
        :return:
        """
        test_board = [
            ['X', None, 'O'],
            [None, None, None],
            [None, 'O', 'X'],
        ]

        self.assertTrue(utils.validate_input(test_board, "1", "1"))
        self.assertFalse(utils.validate_input(test_board, "3", "3"))
        self.assertFalse(utils.validate_input(test_board, "0", "0"))


class TestGame(unittest.TestCase):
    def test_bot_random_step(self):
        """
        Test bot random step function works properly.
        :return:
        """
        game = SingleModeGame()
        game.board.set_board(0, 0, "X")
        game.board.set_board(0, 1, "O")
        game.board.set_board(0, 2, "X")

        # Bot's next step should be in a list with (0, 0), (0, 1) and (0, 2) excluded.
        self.assertIn(game.bot_random_step(), [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])


if __name__ == '__main__':
    unittest.main()
