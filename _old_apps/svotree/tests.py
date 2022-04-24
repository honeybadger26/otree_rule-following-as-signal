from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

    def play_round(self):
        yield pages.SliderPrimaryContinuous, {
            'slider1': 4,
            'slider2': 2,
            'slider3': 1,
            'slider4': 4,
            'slider5': 6,
            'slider6': 2,
        }