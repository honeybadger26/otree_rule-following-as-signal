from otree.api import Currency as c, currency_range
from . import *


class PlayerBot(Bot):

    def play_round(self):
        yield Debriefing
