from otree.api import *
from otree.api import Currency as c, currency_range

# Models #

class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = 1
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    payed_round1 = models.IntegerField()
    payed_round2 = models.IntegerField()

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass

# Pages #

class CalculatePayoffs(WaitPage):

    @staticmethod
    def after_all_players_arrive(group: Group):
        subsession = group.subsession
        session = group.session

        subsession.payed_round1 = session.vars['rfas_payed_round1']
        subsession.payed_round2 = session.vars['rfas_payed_round2']

        for p in group.get_players():
            p.participant.payoff =  p.participant.vars['rfas_payoff']


class PaymentInfo(Page):
    pass

page_sequence = [CalculatePayoffs, PaymentInfo]