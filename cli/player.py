class Player:
    def __init__(self, player_username: str, is_x: bool, is_bot: bool):
        if is_bot:
            self.player_username = "BOT"
            self.is_bot = True
        else:
            self.player_username = player_username
            self.is_x = is_x
            self.is_bot = is_bot

    def __str__(self):
        return self.player_username

    def get_player_symbol(self):
        return "X" if self.is_x else "O"

    def get_player_username(self):
        return self.player_username
