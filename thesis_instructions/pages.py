from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['consent']


class InformationBrochure(Page):
    form_model = 'player'
    form_fields = ['read']


class Instructions(Page):
    form_model = 'player'
    form_fields = ['comprehension1',
                   'comprehension2',
                   'comprehension3',
                   'comprehension4',
                   'comprehension5',
                   'comprehension6',
                   'understood1',
                   'understood11',
                   'understood12',
                   'understood13',
                   'understood2',
                   'understood21',
                   'understood22',
                   'understood23',
                   'understood24']

    def understood_error_message(self, values):
        if values['self.player.understood1'] is None or values['self.player.understood11'] is None or values['self.player.understood12'] is None or \
                values['self.player.understood13'] is None or values['self.player.understood2'] is None or values['self.player.understood21'] is None or \
                values['self.player.understood22'] is None or values['self.player.understood23'] is None or values['self.player.understood24'] is None:
            return 'Tick all the boxes in the subsections to show you read and understood the instructions.'

    def comprehension_error_message(self, values):
        if values['self.player.comprehension1'] != 2 or values['self.player.comprehension2'] != 2 or values['self.player.comprehension3'] != 1 \
                or values['self.player.comprehension4'] != 1 or values['self.player.comprehension5'] != 3 or \
                values['self.player.comprehension6'] != 3:
            return 'At least one answer is wrong. Please try again.'


page_sequence = [
    InformedConsent,
    InformationBrochure,
    Instructions,
]
