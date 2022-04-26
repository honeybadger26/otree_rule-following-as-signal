from sys import path_importer_cache
from otree.api import Currency as c, currency_range
from . import *

class PlayerBot(Bot):

    def play_round(self):
        yield InformedConsent
        # yield PayID, { 'pay_id': 'asldkj1232' }
