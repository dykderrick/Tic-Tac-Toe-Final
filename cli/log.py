import pandas as pd


class Logger:
    def __init__(self, game):
        self.game = game
        self.log_file_path = "./data/game_log.csv"

    def log(self):
        _players = self.game.get_players()
        _game_result = ""

        if self.game.get_winner() is None:
            _game_result = "DRAW"
        else:
            _game_result = self.game.get_winner()

        last_data_df = pd.read_csv(self.log_file_path)

        game_data = {
            "game_id": [str(self.game.get_game_id())],
            "playerX_username": [_players[0].get_player_username()],
            "playerO_username": [_players[1].get_player_username()],
            "game_result": [_game_result],
        }

        data_df = pd.DataFrame.from_dict(data=game_data)

        new_data_df = pd.concat([last_data_df, data_df])

        new_data_df.to_csv(self.log_file_path, index=False)
