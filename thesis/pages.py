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


class RFWaitForSelector(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'


class RFResults(Page):

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


########################################
# STAGE 2: SELECTION TASK
########################################
class RFSelection(Page):

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


page_sequence = [
    EnvironmentPage1,
    Role,
    RFTaskStart
] + [
    RFTask for i in range(15) # TODO: make this not hardcoded
] + [
    RFWaitForSelector,
    ResultsWaitPage,
    RFSelection,
    ResultsWaitPage,
    RFResults,
    StageThreeSelector,
    DictatorTask,
    ResultsWaitPage,
    DictatorResults,
    DictatorResultsDecider,
    FeedbackDeciders,
    EnvironmentPage3,
    PayoffsWaitPage,
]
