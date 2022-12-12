import Country
import Player
import Referee
import Team
from datetime import datetime
from LineUp import LineUp


class Match:
    _line_up_a: LineUp
    _line_up_b: LineUp
    _a_score: int
    _b_score: int
    _date: datetime
    _referees: list
    _recorded_bool: bool

    # Initialize The Match
    def __init__(self, _date: datetime, a: Team, b: Team):
        self._date = _date
        self._line_up_a = LineUp(a)
        self._line_up_b = LineUp(b)
        self._referees = []
        self._recorded_bool = False

    # Getters
    def get_team_a(self) -> LineUp:
        return self._line_up_a

    def get_team_b(self) -> LineUp:
        return self._line_up_b

    def get_a_score(self) -> int:
        return self._a_score

    def get_b_score(self) -> int:
        return self._b_score

    def get_a_country(self) -> Country:
        return self._line_up_a.get_team().get_country()

    def get_b_country(self) -> Country:
        return self._line_up_b.get_team().get_country()

    def get_date_time(self) -> datetime:
        return self._date

    def get_referees(self) -> []:
        return self._referees

    def get_recorded_bool(self) -> bool:
        return self._recorded_bool

    def is_upcoming(self) -> bool:
        return self._date > datetime.now()

    def add_player(self, _player: Player, _team: Team):
        # check for team a
        if _team.get_name() == self.get_team_a().get_team().get_name():
            if self._line_up_a.get_players() is not None:
                # check for less than 11 players on a team
                if len(self._line_up_a.get_players()) < 11:
                    for p in self._line_up_a.get_players():
                        # check for player already on the team
                        if p.get_name() == _player.get_name():
                            raise Exception("Player is already in match")
                    self._line_up_a.add_player(_player)
                else:
                    raise Exception("Cannot have more than 11 players on team")
            else:
                self._line_up_a.add_player(_player)
        # check for team b, follows same format as team a checks
        elif _team.get_name() == self.get_team_b().get_team().get_name():
            if self._line_up_b.get_players() is not None:
                if len(self._line_up_b.get_players()) < 11:
                    for p in self._line_up_b.get_players():
                        if p.get_name() == _player.get_name():
                            raise Exception("Player is already in match")
                    self._line_up_b.add_player(_player)
                else:
                    raise Exception("Cannot have more than 11 players on team")
            else:
                self._line_up_b.add_player(_player)
        else:
            raise Exception("Could not find team")

    def add_referee(self, _referee: Referee):
        if len(self._referees) == 4:
            raise Exception("There are already 4 referees assigned to this match")
        elif _referee.get_country() == self.get_a_country() or _referee.get_country() == self.get_b_country():
            raise Exception("Referee can not be from country of a participating team in this match.")
        else:
            self._referees.append(_referee)

    def set_match_score(self, _a_score: int, _b_score: int):
        self._a_score = _a_score
        self._b_score = _b_score
        self._recorded_bool = True
