import random
from otree.api import Currency as c
from . import pages
from ._builtin import Bot
from .models import C

INSTRUCTION_ANSWERS = {
    'understood1': True,
    'understood11': True,
    'understood12': True,
    'understood13': True,
    'understood2': True,
    'understood21': True,
    'understood22': True,
    'understood23': True,
    'understood24': True,
    'comprehension1': 2,
    'comprehension2': 2,
    'comprehension3': 1,
    'comprehension4': 1,
    'comprehension5': 3,
    'comprehension6': 3
}
            
class PlayerBot(Bot):

    def play_round(self):
        if self.subsession.round_number == 1:
            yield pages.Instructions, INSTRUCTION_ANSWERS
            yield pages.EnvironmentPage1
            yield pages.Role

        if self.subsession.round_number == C.PT1_NUM_ROUNDS + 1:
            yield pages.EnvironmentPage2

        if self.player.role() == 'selector':
            yield pages.RFTaskStart
            yield pages.RFSelection, {
                'select1': True,
                'select3': True
            }
            yield pages.StageThreeSelector
            yield pages.DictatorResults

        if self.player.role() == 'partner':
            for _ in range(C.RFTASK_NUM_ROUNDS):
                yellow_choce = random.choice([True, False])
                blue_choce = not yellow_choce
                yield pages.RFTask, {
                    'yellow_choice': yellow_choce,
                    'blue_choice': blue_choce
                }
            yield pages.RFWaitForSelector
            yield pages.RFResults

            if self.player.selected:
                keep_amount = random.choice(C.KEEP_GIVE_AMOUNTS)
                yield pages.DictatorTask, {
                    'amount_keep': keep_amount,
                    'amount_give': C.ENDOWMENT_STAGE_THREE - keep_amount
                }
                yield pages.DictatorResultsDecider

            yield pages.FeedbackDeciders

        if self.subsession.round_number == C.NUM_ROUNDS:
            yield pages.EnvironmentPage3