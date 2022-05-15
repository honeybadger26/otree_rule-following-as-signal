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

    @staticmethod
    def is_displayed(player: Player):
        player.participant.payoff = player.participant.vars['rfas_total_payoff']
        return True

    @staticmethod
    def vars_for_template(player: Player):
        vars = player.participant.vars
        session = player.session

        return {
            'payoff1': vars['rfas_payoff1'].to_real_world_currency(session),
            'payoff2': vars['rfas_payoff2'].to_real_world_currency(session)
        }

page_sequence = [PaymentInfo]