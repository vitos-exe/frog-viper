from flask import Flask, render_template, redirect, request, url_for, session
import uuid
import secrets

from app.game import GameStatus

from app import game_service

app = Flask(__name__)
app.secret_key = secrets.token_hex()

@app.before_request
def ensure_session_id():
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())

@app.get('/healthcheck')
def healthcheck():
    return 'healthy'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        game_id = request.form['id']
        return redirect(url_for('go_to_game', game_id=game_id))

@app.get('/create')
def create_game():
    user_session_id = session['session_id']
    new_game_id = game_service.create([user_session_id])
    return redirect(url_for('go_to_game', game_id=new_game_id)) 

@app.get('/<game_id>')
def go_to_game(game_id: str):
    game = game_service.find(game_id)
    if game is not None:
        players_session_id = session['session_id']
        if game.status == GameStatus.WAITING_FOR_PLAYERS:
            game_service.add_player(game_id, players_session_id)
            return render_template('lobby.html') 

        if game.status == GameStatus.ONGOING:
            return 'Ongoing'

    return 'Not found', 404


