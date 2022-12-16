from flask import Flask
from flask import render_template, request

from utils import validate_user_input

app = Flask(__name__)


@app.route('/')
def game_mode_selection():  # put application's code here
    game_mode = request.args.get('gameMode')
    player_1_name = request.args.get('player1Name')
    player_2_name = request.args.get('player2Name')

    game_config = {
        'game_mode': game_mode,
        'player_1_name': player_1_name,
        'player_2_name': player_2_name,
    }

    if validate_user_input(game_config):
        return render_template('game/index.html', game_config=game_config)

    return render_template('game_mode_selection/index.html')


if __name__ == '__main__':
    app.run(port=8000, debug=True)
    # app.run()
