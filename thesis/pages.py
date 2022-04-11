from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
import time


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
        return self.subsession.round_number == (Constants.num_rounds/2)+1

    def error_message(self, values):
        solutions = dict(
            comprehension7=1,
            comprehension8=3
        )
            
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'This answer is wrong'
        
        return error_messages


class EnvironmentPage3(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'money_earned': self.participant.payoff.to_real_world_currency(self.session)
        }


class FeedbackDeciders(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'

    def vars_for_template(self):
        total_points = self.player.amount_keep if self.player.field_maybe_none('amount_keep') is not None else c(0)

        if self.player.id_in_group == 1:
            total_points += self.group.payoff_rf1
        elif self.player.id_in_group == 2:
            total_points += self.group.payoff_rf2
        elif self.player.id_in_group == 3:
            total_points += self.group.payoff_rf3

        return { 'points_total': total_points }


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
class RFTaskStart(Page):

    def is_displayed(self):
        return self.player.role() == 'selector'


class RFTask(Page):
    form_model = 'player'
    form_fields = ['yellow_choice', 'blue_choice']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def vars_for_template(self):
        total_points = 0

        if self.player.id_in_group == 1:
            total_points = self.group.payoff_rf1
        elif self.player.id_in_group == 2:
            total_points = self.group.payoff_rf2
        elif self.player.id_in_group == 3:
            total_points = self.group.payoff_rf3

        return {
            'ball_count': self.player.yellow_count + self.player.blue_count + 1,
            'total_points': total_points
        }

    def before_next_page(self):
        payoff = 0

        if self.player.yellow_choice:
            self.player.yellow_count += 1
            self.player.yellow_score += Constants.endowment_yellow
            payoff = Constants.endowment_yellow
        elif self.player.blue_choice:
            self.player.blue_count += 1
            self.player.blue_score += Constants.endowment_blue
            payoff = Constants.endowment_blue

        if self.player.id_in_group == 1:
            self.group.payoff_rf1 += payoff
        elif self.player.id_in_group == 2:
            self.group.payoff_rf2 += payoff
        elif self.player.id_in_group == 3:
            self.group.payoff_rf3 += payoff


class RFResults1(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'

    def vars_for_template(self):
        results = []

        for p in self.group.get_players():
            if p.role() == 'partner':
                results.append({
                    'id': p.id_in_group,
                    'blue_count': p.blue_count,
                    'selected': p.selected
                })

        return { 'results': sorted(results, key=lambda r: r['blue_count']) }


class RFResults21(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'


########################################
# STAGE 2: SELECTION TASK
########################################
class RFResults2(Page):

    form_model = 'group'
    form_fields = ['select1', 'select2', 'select3']

    def is_displayed(self):
        return self.player.role() == 'selector'

    def vars_for_template(self):
        results = []

        for p in self.group.get_players():
            if p.role() == 'partner':
                results.append({
                    'id': p.id_in_group,
                    'blue_count': int(p.blue_count),
                    'payoff': p.blue_score + p.yellow_score,
                    'field': 'select' + str(p.id_in_group)
                })

        return { 'results': sorted(results, key=lambda p: p['blue_count']) }

    def error_message(self, values):
        if values["select1"] is not True and \
            values["select2"] is not True and \
            values["select3"] is not True:
            return 'Select at least one partner.'

    def before_next_page(self):
        for p in self.group.get_players():
            p.selected = \
                (p.id_in_group == 1 and self.group.select1) or \
                (p.id_in_group == 2 and self.group.select2) or \
                (p.id_in_group == 3 and self.group.select3)



class StageThreeSelector(Page):
    def is_displayed(self):
        return self.player.role() == 'selector'


########################################
# STAGE 3.A: DICTATOR TASK
########################################
class DictatorTask(Page):
    form_model = 'player'
    form_fields = ['amount_keep', 'amount_give']

    def is_displayed(self):
        return \
            self.round_number <= Constants.num_rounds/2 and \
            self.player.role() == 'partner' and \
            self.player.selected

    def error_message(self, values):
        if values['amount_keep'] + values['amount_give'] != Constants.endowment_stage_three:
            return 'The points have to add up to ' + str(Constants.endowment_stage_three)


class DictatorResults(Page):

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.role() == 'selector'

    def vars_for_template(self):
        results = []
        earnings_total = Constants.endowment_selection
        selected_count = 0

        for p in self.group.get_players():
            if p.role() == 'partner' and p.selected:
                earnings = p.amount_give - Constants.selection_fee if p.selected else c(0)
                earnings_total += earnings
                selected_count += 1 if p.selected else 0

                results.append({
                    'id': p.id_in_group,
                    'blue_count': p.blue_count,
                    'amount_keep': p.amount_keep,
                    'amount_give': p.amount_give,
                    'earnings': earnings
                })

        return { 
            'results': sorted(results, key=lambda r: r['blue_count']),
            'earning_total': earnings_total,
            'selected_num': selected_count
        }


class DictatorResultsDecider(Page):

    def is_displayed(self):
        return \
            self.round_number <= Constants.num_rounds/2 and \
            self.player.role() == 'partner' and \
            self.player.selected


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
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 1 \
               and self.group.select1 is True


class DieRollTask22(Page):
    form_model = 'group'
    form_fields = ['die_roll2']

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 2 \
               and self.group.select2 is True


class DieRollTask32(Page):
    form_model = 'group'
    form_fields = ['die_roll3']

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 3 \
               and self.group.select3 is True


class DieRollResults1(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 1 \
               and self.group.select1 is True

    def vars_for_template(self):
        points = 'So, both you and the selector earn ' + str(Constants.dieroll_points[self.group.die_roll1-1]) + '.' \
            if self.group.field_maybe_none('die_roll1') is not None else ''
        return {
            'points': points
        }


class DieRollResults2(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 2 \
               and self.group.select2 is True

    def vars_for_template(self):
        points = 'So, both you and the selector earn ' + str(Constants.dieroll_points[self.group.die_roll2-1]) + '.' \
            if self.group.field_maybe_none('die_roll2') is not None else ''
        return {
            'points': points
        }


class DieRollResults3(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 3 \
               and self.group.select3 is True

    def vars_for_template(self):
        points = 'So, both you and the selector earn ' + str(Constants.dieroll_points[self.group.die_roll3-1]) + '.' \
            if self.group.field_maybe_none('die_roll3') is not None else ''
        return {
            'points': points
        }


class DieRollResults4(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.role() == 'selector'

    def vars_for_template(self):
        die_roll1 = 'One decider rolled a ' + str(self.group.die_roll1) + '.' if self.group.field_maybe_none('die_roll1') is not None else ''
        die_roll2 = 'One decider rolled a ' + str(self.group.die_roll2) + '.' if self.group.field_maybe_none('die_roll2') is not None else ''
        die_roll3 = 'One decider rolled a ' + str(self.group.die_roll3) + '.' if self.group.field_maybe_none('die_roll3') is not None else ''
        selected1 = 1 if self.group.select1 else 0
        selected2 = 1 if self.group.select2 else 0
        selected3 = 1 if self.group.select3 else 0
        selected_num = selected1 + selected2 + selected3
        earning1 = Constants.dieroll_points[self.group.die_roll1-1] - Constants.selection_fee if self.group.select1 \
            is True else 0
        earning2 = Constants.dieroll_points[self.group.die_roll2-1] - Constants.selection_fee if self.group.select2 \
            is True else 0
        earning3 = Constants.dieroll_points[self.group.die_roll3-1] - Constants.selection_fee if self.group.select3 \
            is True else 0
        earning_total = Constants.endowment_selection + earning1 + earning2 + earning3
        points1 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter1) + \
                  ' times reported a ' + str(self.group.die_roll1) + '. So, you earn ' \
                  + str(earning1) + ' for this interaction.' if self.group.field_maybe_none('die_roll1') is not None else ''
        points2 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter2) + \
                  ' times reported a ' + str(self.group.die_roll2) + '. So, you earn ' \
                  + str(earning2) + ' for this interaction.' if self.group.field_maybe_none('die_roll2') is not None else ''
        points3 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter3) + \
                  ' times reported a ' + str(self.group.die_roll3) + '. So, you earn ' \
                  + str(earning3) + ' for this interaction.' if self.group.field_maybe_none('die_roll3') is not None else ''

        dieroll_tuples = [
            [int(self.group.blue_counter1), str(points1)],
            [int(self.group.blue_counter2), str(points2)],
            [int(self.group.blue_counter3), str(points3)],
        ]
        sorted_dieroll = sorted(dieroll_tuples, key=lambda d: d[0])
        return {
            'dieroll_results': [ x[1] for x in sorted_dieroll if x[1] is not None ],
            'die_roll1': die_roll1,
            'die_roll2': die_roll2,
            'die_roll3': die_roll3,
            'points1': points1,
            'points2': points2,
            'points3': points3,
            'earning_total': earning_total,
            'selected_num': selected_num,
        }


page_sequence = [
    EnvironmentPage1,
    Role,
    # EnvironmentPage2,
    RFTaskStart
] + [
    RFTask for i in range(15) # TODO: make this not hardcoded
] + [
    RFResults21,
    ResultsWaitPage,
    RFResults2,
    ResultsWaitPage,
    RFResults1,
    StageThreeSelector,
    DictatorTask,
#    DieRollTask11,
#    DieRollTask21,
#    DieRollTask31,
#    DieRollTask12,
#    DieRollTask22,
#    DieRollTask32,
    ResultsWaitPage,
    DictatorResults,
    DictatorResultsDecider,
#    DieRollResults1,
#    DieRollResults2,
#    DieRollResults3,
#    DieRollResults4,
    FeedbackDeciders,
    EnvironmentPage3,
#    DieRollTaskEnd11,
#    DieRollTaskEnd12,
#    DieRollTaskEnd21,
#    DieRollTaskEnd22,
#    DieRollTaskEnd31,
#    DieRollTaskEnd32,
#    DieRollTaskEnd41,
#    DieRollTaskEnd42,
    PayoffsWaitPage,
]
