from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
            'money_earned': self.participant.payoff.to_real_world_currency(self.session)
        }



page_sequence = [PaymentInfo]
