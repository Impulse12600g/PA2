import Player
import Team


class LineUp:
    _players: list
    _team: Team

    def __init__(self, _team: Team):
        self._team = _team
        self._players = []

    # getters
    def get_team(self) -> Team: return self._team
    def get_players(self) -> list: return self._players

    # Add player function
    def add_player(self, _player: Player): self._players.append(_player)
