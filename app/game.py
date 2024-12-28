import uuid
from enum import Enum

class Game():
    def __init__(self, players) -> None:
        self.id = uuid.uuid4().hex
        self.status = GameStatus.WAITING_FOR_PLAYERS
        self._players = set(players)

    def add_player(self, id):
        self._players.add(id)

    def remove_player(self, id):
        self._players.remove(id)

class GameStatus(Enum):
    WAITING_FOR_PLAYERS = 1
    ONGOING = 2

