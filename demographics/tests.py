from otree.api import Currency as c, currency_range
from . import *


class PlayerBot(Bot):

    def play_round(self):
        yield Demographics, {
            'age': 30,
            'gender': 'Male',
            'your_study': 'Engineering',
            'nr_similar_experiments': 20
        }