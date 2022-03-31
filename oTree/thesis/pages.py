from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random


class Round(Page):

    timeout_seconds = 1

    def vars_for_template(self) -> dict:
        role = 'After the other players made their decisions, you will choose at least one of' \
               ' them for stage 3 or not.' if self.player.role() == 'selector' else 'You will ' \
                'make a number of decisions that will influence whether you will be chosen by another player for ' \
                'stage 3 or not.'
        return {
            'role': role
        }


class Role(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class EnvironmentPage1(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class EnvironmentPage2(Page):

    form_model = 'player'
    form_fields = ['understood31',
                   'understood32',
                   'understood33',
                   'understood34',
                   'comprehension7',
                   'comprehension8']

    def is_displayed(self):
        return self.subsession.round_number == 2

    def error_message(self, values):
        if self.player.comprehension7 != 1 or self.player.comprehension8 != 3:
            return 'At least one answer is wrong. Please try again.'


class EnvironmentPage3(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'money_earned': self.participant.payoff.to_real_world_currency(self.session)
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class PayoffsWaitPage(WaitPage):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        self.group.set_payoffs()


########################################
# STAGE 1: RULE-FOLLOWING
########################################
class RFTask2(Page):

    def is_displayed(self):
        return self.player.role() == 'selector'


class RFTask(Page):
    form_model = 'player'
    form_fields = ['yellow_choice1',
                   'yellow_choice2',
                   'yellow_choice3',
                   'blue_choice1',
                   'blue_choice2',
                   'blue_choice3']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def vars_for_template(self):
        return {
            'role': self.player.role(),
            'partner1': Constants.all_players[0],
            'partner2': Constants.all_players[1],
            'partner3': Constants.all_players[2],
        }

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice1
        self.group.yellow_counter2 += self.player.yellow_choice2
        self.group.yellow_counter3 += self.player.yellow_choice3

        self.group.blue_counter1 += self.player.blue_choice1
        self.group.blue_counter2 += self.player.blue_choice2
        self.group.blue_counter3 += self.player.blue_choice3

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice1 \
            + Constants.endowment_blue*self.player.blue_choice1
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice2 \
            + Constants.endowment_blue*self.player.blue_choice2
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice3 \
            + Constants.endowment_blue*self.player.blue_choice3

        self.player.yellow_choice1 = 0
        self.player.yellow_choice2 = 0
        self.player.yellow_choice3 = 0
        self.player.blue_choice1 = 0
        self.player.blue_choice2 = 0
        self.player.blue_choice3 = 0

        self.player.balls += 1


class RFResults1Selector(Page):
    def is_displayed(self):
        return self.player.role() == 'selector'


class RFResults1(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 = 0
        self.group.yellow_counter2 = 0
        self.group.yellow_counter3 = 0
        self.group.blue_counter1 = 0
        self.group.blue_counter2 = 0
        self.group.blue_counter3 = 0

        self.player.balls = 1

    def vars_for_template(self):
        return {
            'role': self.player.role(),
            'partner1': Constants.all_players[0],
            'partner2': Constants.all_players[1],
            'partner3': Constants.all_players[2],
        }


class RFResults2(Page):

    form_model = 'group'
    form_fields = ['select1',
                   'select2',
                   'select3']

    def is_displayed(self):
        return self.player.role() == 'selector'

    def error_message(self, values):
        print('values is', values)
        if values["select1"] is not True and values["select2"] is not True and values["select3"] is not True:
            return 'Select at least one partner.'


class RFResults21(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'


########################################
# STAGE 2: SELECTION TASK
########################################
class SelectionTask(Page):
    form_model = 'group'
    form_fields = ['select1',
                   'select2',
                   'select3']

    def error_message(self, values):
        print('values is', values)
        if values["select1"] is not True and values["select2"] is not True and values["select3"] is not True:
            return 'Select at least one partner.'


class SelectionResults(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'


########################################
# STAGE 3.A: DICTATOR TASK
########################################
class DictatorTask1(Page):
    form_model = 'group'
    form_fields = ['dictator_choice11',
                   'dictator_choice12']

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[0] \
               and self.group.select1 is True

    def error_message(self, values):
        print('values is', values)
        if self.group.dictator_choice11 + self.group.dictator_choice12 != Constants.endowment_stage_three \
                or self.group.dictator_choice11 is None or self.group.dictator_choice12 is None:
            return 'The points have to sum up to ' + str(Constants.endowment_stage_three)

    def vars_for_template(self):
        return {
            'player': Constants.all_players[0]
        }


class DictatorTask2(Page):
    form_model = 'group'
    form_fields = ['dictator_choice21',
                   'dictator_choice22']

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[1] \
               and self.group.select2 is True

    def error_message(self, values):
        print('values is', values)
        if self.group.dictator_choice21 + self.group.dictator_choice22 != Constants.endowment_stage_three \
                or self.group.dictator_choice21 is None or self.group.dictator_choice22 is None:
            return 'The MU have to sum up to ' + str(Constants.endowment_stage_three)

    def vars_for_template(self):
        return {
            'player': Constants.all_players[1]
        }


class DictatorTask3(Page):
    form_model = 'group'
    form_fields = ['dictator_choice31',
                   'dictator_choice32']

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[2] \
               and self.group.select3 is True

    def error_message(self, values):
        print('values is', values)
        if (self.group.dictator_choice31 + self.group.dictator_choice32) != Constants.endowment_stage_three \
                or self.group.dictator_choice31 is None or self.group.dictator_choice32 is None:
            return 'The MU have to sum up to ' + str(Constants.endowment_stage_three)

    def vars_for_template(self):
        return {
            'player': Constants.all_players[2]
        }


class DictatorResults(Page):

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.role() == 'selector'

    def vars_for_template(self):
        earning1 = self.group.dictator_earning12 - Constants.selection_fee if self.group.select1 \
            is True else 0
        earning2 = self.group.dictator_choice22 - Constants.selection_fee if self.group.select2 \
            is True else 0
        earning3 = self.group.dictator_choice32 - Constants.selection_fee if self.group.select3 \
            is True else 0
        dictator1 = 'A player chose to keep ' + str(self.group.dictator_choice11) + ' and give ' \
                    + str(self.group.dictator_choice12) + ' to you. Therefore, you earned ' + \
                    str(earning1) + ' during this interaction.' if self.group.select1 is True else ''
        dictator2 = 'A player chose to keep ' + str(self.group.dictator_choice21) + ' and give ' \
                    + str(self.group.dictator_choice22) + ' to you. Therefore, you earned ' + \
                    str(earning2) + ' during this interaction.' if self.group.select2 is True else ''
        dictator3 = 'A player chose to keep ' + str(self.group.dictator_choice31) + ' and give ' \
                    + str(self.group.dictator_choice32) + 'to you. Therefore, you earned ' + \
                    str(earning3) + ' during this interaction.' if self.group.select3 is True else ''
        return {
            'dictator1': dictator1,
            'dictator2': dictator2,
            'dictator3': dictator3,
            'earning1': earning1,
            'earning2': earning2,
            'earning3': earning3
        }


########################################
# STAGE 3.B: DIE ROLL TASK
########################################

class DieRollTaskEnd11(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 1


class DieRollTaskEnd12(Page):

    form_model = 'group'
    form_fields = ['dieroll_end1']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 1


class DieRollTaskEnd21(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 2


class DieRollTaskEnd22(Page):

    form_model = 'group'
    form_fields = ['dieroll_end2']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 2


class DieRollTaskEnd31(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 3


class DieRollTaskEnd32(Page):

    form_model = 'group'
    form_fields = ['dieroll_end3']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 3


class DieRollTaskEnd41(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 4


class DieRollTaskEnd42(Page):

    form_model = 'group'
    form_fields = ['dieroll_end4']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 4


class DieRollTask11(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 1 and self.group.select1 is True


class DieRollTask21(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 2 and self.group.select2 is True


class DieRollTask31(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 3 and self.group.select3 is True


class DieRollTask12(Page):
    form_model = 'group'
    form_fields = ['die_roll1']

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[0] \
               and self.group.select1 is True


class DieRollTask22(Page):
    form_model = 'group'
    form_fields = ['die_roll2']

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[1] \
               and self.group.select2 is True


class DieRollTask32(Page):
    form_model = 'group'
    form_fields = ['die_roll3']

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[2] \
               and self.group.select3 is True


class DieRollResults1(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[0] \
               and self.group.select1 is True

    def vars_for_template(self):
        points = 'So, both you and the other player earn ' + str(Constants.dieroll_points[self.group.die_roll1-1]) + '.' \
            if self.group.die_roll1 is not None else ''
        return {
            'points': points
        }


class DieRollResults2(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[1] \
               and self.group.select2 is True

    def vars_for_template(self):
        points = 'So, both you and the other player earn ' + str(Constants.dieroll_points[self.group.die_roll2-1]) + '.' \
            if self.group.die_roll2 is not None else ''
        return {
            'points': points
        }


class DieRollResults3(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == Constants.all_players[2] \
               and self.group.select3 is True

    def vars_for_template(self):
        points = 'So, both you and the other player earn ' + str(Constants.dieroll_points[self.group.die_roll3-1]) + '.' \
            if self.group.die_roll3 is not None else ''
        return {
            'points': points
        }


class DieRollResults4(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.role() == 'selector'

    def vars_for_template(self):
        die_roll1 = 'A player rolled a ' + str(self.group.die_roll1) + '.' if self.group.die_roll1 is not None else ''
        die_roll2 = 'A player rolled a ' + str(self.group.die_roll2) + '.' if self.group.die_roll2 is not None else ''
        die_roll3 = 'A player rolled a ' + str(self.group.die_roll3) + '.' if self.group.die_roll3 is not None else ''
        earning1 = Constants.dieroll_points[self.group.die_roll1-1] if self.group.select1 \
            is True else 0
        earning2 = Constants.dieroll_points[self.group.die_roll2-1] if self.group.select2 \
            is True else 0
        earning3 = Constants.dieroll_points[self.group.die_roll3-1] if self.group.select3 \
            is True else 0
        points1 = 'So, both you and the other player earn ' + str(earning1) + \
                  '.' if self.group.die_roll1 is not None else ''
        points2 = 'So, both you and the other player earn ' + str(earning2) + \
                  '.' if self.group.die_roll2 is not None else ''
        points3 = 'So, both you and the other player earn ' + str(earning3) + \
                  '.' if self.group.die_roll3 is not None else ''
        return {
            'die_roll1': die_roll1,
            'die_roll2': die_roll2,
            'die_roll3': die_roll3,
            'points1': points1,
            'points2': points2,
            'points3': points3
        }


page_sequence = [
    Role,
    EnvironmentPage1,
    EnvironmentPage2,
    Round,
    RFTask2,
    RFTask,
    RFTask,
    RFResults21,
    ResultsWaitPage,
    RFResults2,
    ResultsWaitPage,
    RFResults1,
    RFResults1Selector,
    DictatorTask1,
    DictatorTask2,
    DictatorTask3,
    DieRollTask11,
    DieRollTask21,
    DieRollTask31,
    DieRollTask12,
    DieRollTask22,
    DieRollTask32,
    ResultsWaitPage,
    DictatorResults,
    DieRollResults1,
    DieRollResults2,
    DieRollResults3,
    DieRollResults4,
    EnvironmentPage3,
    DieRollTaskEnd11,
    DieRollTaskEnd12,
    DieRollTaskEnd21,
    DieRollTaskEnd22,
    DieRollTaskEnd31,
    DieRollTaskEnd32,
    DieRollTaskEnd41,
    DieRollTaskEnd42,
    PayoffsWaitPage
]
