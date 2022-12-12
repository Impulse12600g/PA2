import Country
from Player import Player


class Team:
    _name: ''
    _squad: []
    _country: Country

    def __init__(self, _name: '', _country: Country):
        self._name = _name
        self._country = _country
        self._squad = []

    # Getters
    def get_name(self): return self._name
    def get_squad(self) -> list: return self._squad
    def get_country(self) -> Country: return self._country

    # Add Player
    def add_player(self, _name: '', _age: int, _height: float, _weight: float):
        if self.get_squad() is None:
            self._squad.append(Player(_name, _age, _height, _weight))
        elif len(self._squad) < 35:
            self._squad.append(Player(_name, _age, _height, _weight))
        else:
            raise Exception("Squad already has 35 players")
