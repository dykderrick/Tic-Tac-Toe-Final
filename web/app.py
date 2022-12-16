from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def game_mode_selection():  # put application's code here
    game_mode = request.args.get('gameMode')
    player_1_name = request.args.get('player1Name')
    player_2_name = request.args.get('player2Name')

    if game_mode == 'SingleMode':
        return render_template('game/index.html')

    return render_template('game_mode_selection/index.html')


if __name__ == '__main__':
    # app.run(port=8000, debug=True)
    app.run()
