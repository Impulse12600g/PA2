import Country


class Referee:
    _name: ''
    _country: Country

    def __init__(self, _name: '', _country: Country):
        self._name = _name
        self._country = _country

    # Getters
    def get_name(self): return self._name
    def get_country(self) -> Country: return self._country
