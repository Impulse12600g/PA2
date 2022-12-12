class Player:
    _name: ''
    _age: int
    _height: float
    _weight: float

    def __init__(self, _name: '', _age: int, _height: float, _weight: float):
        self._name = _name
        self._age = _age
        self._height = _height
        self._weight = _weight

    # Getters
    def get_name(self): return self._name
    def get_age(self) -> int: return self._age
    def get_height(self) -> float: return self._height
    def get_weight(self) -> float: return self._weight

    # Setters
    def set_name(self, _name: ''): self._name = _name
    def set_age(self, _age: int): self._age = _age
    def set_height(self, _height: float): self._height = _height
    def set_weight(self, _weight: float): self._weight = _weight
