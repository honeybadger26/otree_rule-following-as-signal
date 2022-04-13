from otree.api import *
import random

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

    def vars_for_template(self):
        return {
            'redemption_code': self.participant.label or self.participant.code,
            'money_earned': self.participant.payoff.to_real_world_currency(self.session)
        }

page_sequence = [PaymentInfo]