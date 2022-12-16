def validate_user_input(game_config):
    game_mode = game_config['game_mode']
    player_1_name = game_config['player_1_name']
    player_2_name = game_config['player_2_name']

    if game_mode == 'SingleMode':
        return player_1_name != '' and player_2_name != ''

    elif game_mode == 'TwoPlayersMode':
        invalid_fields = ['', 'bot', 'BOT']
        return player_1_name not in invalid_fields and player_2_name not in invalid_fields
    else:
        return False
