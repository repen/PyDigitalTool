"""
Copyright (c) 2021 Plugin Andrey (9keepa@gmail.com)
Licensed under the MIT License
"""
from dataclasses import dataclass
from typing import List

@dataclass
class FootballMatch:
    match_id: str
    start_time: int
    home_team: str
    away_team: str
    league: str
    country: str
    home_goals: int
    away_goals: int
    elapsed_time: int
    extra_time: str
    match_status: str
    home_goals_before45: int
    away_goals_before45: int
    statistics: str

    def get_unique_field(self):
        """Вернуть уникальный атрибут объекта"""
        return self.match_id

    def __hash__(self):
        """Хешируем атрибуты которые будут менятся"""
        return hash((self.home_goals, self.away_goals))
        # return hash((self.elapsed_time,))

    def __str__(self):
        string = f"{self.elapsed_time}. {self.get_unique_field()} {self.home_team} {self.home_goals} - " \
                 f"{self.away_goals} {self.away_team}"
        return string


class ChangeTracker:
    """Класс отслеживает изменения у объекта"""
    def __init__(self, *args, **kwargs):
        self.state_container = dict()
        self.functions = []


    def registration_function(self, func):
        self.functions.append(func)


    def get_update(self, new_object, old_object):
        for func in self.functions:
            func(new_object, old_object)


    def load(self, objects: List[FootballMatch]):
        for new_object in objects:
            key = new_object.get_unique_field()
            if key in self.state_container:
                old_object = self.state_container[key]
                if hash(new_object) != hash(old_object):
                    # сделай что нибудь полезное
                    self.get_update(new_object, old_object)
                    # устанавливаем новый объект на место старого
                    self.state_container[key] = new_object
            else:
                self.state_container[key] = new_object

