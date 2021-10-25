"""
Copyright (c) 2021 Plugin Andrey (9keepa@gmail.com)
Licensed under the MIT License
"""
from typing import List
import logging
from sport.api import FootballSport
import time
from toolkit import FootballMatch, ChangeTracker

logging.basicConfig(
    format='%(asctime)s : %(lineno)d : %(name)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Start script")

def pprint(new_object: FootballMatch, old_object: FootballMatch):
    """Отправка в телеграм. Запись в базу."""
    print(f"{'='*40}")
    print("OLD", old_object)
    print("NEW", new_object)
    print(f"{'='*40}")



token = "1000001021:31875375750a4c7b829df5dea9686acb"
football = FootballSport(token)
tracker = ChangeTracker()
tracker.registration_function(pprint)


for _ in range(1000):
    matches = football.live()
    matches_list:List[FootballMatch] = [FootballMatch(**x) for x in matches]
    tracker.load(matches_list)
    logger.info("Tick")
    time.sleep(1)

