import pickle
from Team import Team
from Country import Country
from Referee import Referee
from Player import Player
import string
from datetime import datetime


class Tournament:
    _participatingCountries: list
    _listTeams: list
    _listReferees: list
    _listMatches: list

    # initialize the tournament
    def __init__(self, name: string, startDate: datetime, endDate: datetime):
        self.__name = name
        self.__startDate = startDate
        self.__endDate = endDate

        self._participatingCountries = []
        self._listTeams = []
        self._listReferees = []
        self._listMatches = []

    def load_from_file(self, filename: string):
        pass

    def save_to_file(self, filename: string):
        pass

    def add_country(self, countryName: string):
        if bool(self._participatingCountries):  # if it is empty
            self._participatingCountries.append(Country(countryName))  # add country object in
        else:
            for x in self._participatingCountries:
                if self._participatingCountries[x] == countryName:  # if it contains that country
                    raise Exception("Country already in list")
            self._participatingCountries.append(Country(countryName))

    def add_team(self, teamName: string, country: string):
        for x in self._participatingCountries:
            if self._participatingCountries[x] == country:  # if country exists
                self._listTeams.append(Team(teamName, country))
            else:
                for x in self._listTeams:
                    if self._listTeams[x] == teamName:
                        raise Exception("Team already in list")
                self._listTeams.append(Team(teamName, country))

    def add_referee(self, name: string, country: string):
        for x in self._participatingCountries:
            if self._participatingCountries[x] == name:  # if country exits
                if len(self._listReferees) == 0:  # if list is empty
                    self._listReferees.append(Referee(name, country))
                else:
                    for y in self._listReferees:
                        if self._listReferees[y] == name:
                            raise Exception("eferee is already in the tournament")
                self._listReferees.append(Referee(name, country))

    def add_player(self, teamName: string, playerName: string, age: int, height: float, weight: float):
        for x in self._listTeams:
            if self._listTeams[x] == teamName:  # if country exits
                if len(self._listTeams) == 0:  # if list is empty
                    self._listTeams.append(Player(playerName, age, height, weight))
                else:
                    for y in self._listTeams:
                        if Player.get_name() == playerName:
                            raise Exception("TPlayer is already on a team")
                Team.add_player(playerName, age, height, weight)  # error here

