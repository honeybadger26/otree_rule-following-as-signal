from otree.api import *

# Models #

class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pay_id = models.StringField(label='PayID')

# Pages #

class InformedConsent(Page):
    pass

class PayID(Page):
    form_model = 'player'
    form_fields = ['pay_id']

page_sequence = [InformedConsent, PayID]
