from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        if self.subsession.round_number == 1:
            yield pages.EnvironmentPage1
            yield pages.Role

        if self.player.role() == 'selector':
            yield pages.RFTaskStart
            yield pages.RFSelection, {
                'select1': True,
                'select2': False, 
                'select3': False
            }
            yield pages.StageThreeSelector

            if self.subsession.round_number <= Constants.pt1_num_rounds:
                yield pages.DictatorResults

        if self.player.role() == 'partner':
            for _ in range(Constants.rftask_num_rounds):
                yield pages.RFTask, {
                    'yellow_choice': False,
                    'blue_choice': True
                }
            yield pages.RFWaitForSelector
            yield pages.RFResults

            if self.subsession.round_number <= Constants.pt1_num_rounds and self.player.selected:
                yield pages.DictatorTask, {
                    'amount_keep': c(250),
                    'amount_give': c(250)
                }
                yield pages.DictatorResultsDecider

            yield pages.FeedbackDeciders

        if self.subsession.round_number == Constants.num_rounds:
            yield pages.EnvironmentPage3
