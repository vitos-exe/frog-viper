from app.game import Game

GAMES: dict[str, Game] = {}

def create(initial_player_ids: list[str] = []) -> str:
    new_game = Game(initial_player_ids)
    GAMES[new_game.id] = new_game
    return new_game.id

def find(game_id: str) -> Game | None:
    return GAMES.get(game_id)

def add_player(game_id: str, player_id: str) -> None:
    game = GAMES.get(game_id)
    if game is None:
        raise Exception(f'Game with ID {game_id} was unexpectedly not found')
    game.add_player(player_id)

