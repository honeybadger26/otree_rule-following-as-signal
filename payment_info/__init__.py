from otree.api import *
from otree.api import Currency as c, currency_range

# Models #

class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

# Pages #

class PaymentInfo(Page):
    pass

page_sequence = [PaymentInfo]