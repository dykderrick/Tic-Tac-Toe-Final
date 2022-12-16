import pandas as pd


class GlobalRank:
    def __init__(self):
        self.log_file_path = "./data/game_log.csv"

        self.user_wins = {}
        self.user_losses = {}
        self.user_draws = {}
        self._set_user_wins()

    def _set_user_wins(self):
        data_df = pd.read_csv(self.log_file_path)

        for _, row in data_df.iterrows():
            current_win_username = None
            current_lose_username = None
            current_draw_x_username = None
            current_draw_o_username = None

            if row["game_result"] == "X":
                current_win_username = row["playerX_username"]
                current_lose_username = row["playerO_username"]
            elif row["game_result"] == "O":
                current_win_username = row["playerO_username"]
                current_lose_username = row["playerX_username"]
            else:  # draw
                current_draw_x_username = row["playerX_username"]
                current_draw_o_username = row["playerO_username"]

            # update user_wins
            if current_win_username:
                if current_win_username not in self.user_wins.keys():
                    self.user_wins[current_win_username] = 1
                else:
                    self.user_wins[current_win_username] += 1

            if current_lose_username:
                if current_lose_username not in self.user_losses.keys():
                    self.user_losses[current_lose_username] = 1
                else:
                    self.user_losses[current_lose_username] += 1

            if current_draw_x_username and current_draw_o_username:
                if current_draw_x_username not in self.user_draws.keys():
                    self.user_draws[current_draw_x_username] = 1
                else:
                    self.user_draws[current_draw_x_username] += 1

                if current_draw_o_username not in self.user_draws.keys():
                    self.user_draws[current_draw_o_username] = 1
                else:
                    self.user_draws[current_draw_o_username] += 1

        # sort dict by value
        self.user_wins = dict(sorted(self.user_wins.items(), key=lambda item: item[1], reverse=True))

    def __str__(self):
        output = "[GLOBAL RANK] - Sorted by # of wins\n"
        output += "Rank #  |  username  |  # of wins  |  # of losses  |  # of draws\n"
        output += "----------------------------------------------------------------\n"

        index = 1
        for key_username in self.user_wins.keys():
            losses_time = self.user_losses[key_username] if key_username in self.user_losses.keys() else 0
            draws_time = self.user_draws[key_username] if key_username in self.user_draws.keys() else 0

            output += str(index) + "    " + key_username + "    " + str(self.user_wins[key_username]) + "    " + str(losses_time) + "    " + str(draws_time) + "    \n"
            output += "----------------------------------------------------------------\n"
            index += 1

        return output
