from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender',
                   'your_study',
                   'reason',
                   'nr_similar_experiments',
                   'other_info',
                   'real_humans']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


page_sequence = [
    Demographics,
]
