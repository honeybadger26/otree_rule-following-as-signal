from otree.api import Currency as c
from ._builtin import Page, WaitPage
from .models import C

class Instructions(Page):
    form_model = 'player'
    form_fields = ['understood1', 'understood11', 'understood12', 'understood13', 'understood2',
        'understood21', 'understood22', 'understood23', 'understood24', 'comprehension1',
        'comprehension2', 'comprehension3', 'comprehension4', 'comprehension5', 'comprehension6']

    def is_displayed(self):
        return self.subsession.round_number == 1

    def error_message(self, values):
        solutions = dict(
            comprehension1=2,
            comprehension2=2,
            comprehension3=1,
            comprehension4=1,
            comprehension5=3,
            comprehension6=3
        )
            
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'This answer is wrong'
        
        return error_messages


class EnvironmentPage1(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class EnvironmentPage2(Page):

    def is_displayed(self):
        return self.subsession.round_number == C.PT1_NUM_ROUNDS + 1


class Role(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class RFTaskStart(Page):

    def is_displayed(self):
        return self.player.role() == 'selector'


class RFTask(Page):
    form_model = 'player'
    form_fields = ['yellow_choice', 'blue_choice']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        if self.player.yellow_choice:
            self.player.yellow_count += 1
        elif self.player.blue_choice:
            self.player.blue_count += 1

        self.player.set_rf_payoff()


class RFWaitForSelector(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'


class RFSelectorPayoffWaitPage(WaitPage):
    
    def after_all_players_arrive(self):
        self.group.set_selector_initial_payoff()


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
                    'payoff': p.payoff,
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


class RFDeciderPayoffWaitPage(WaitPage):
    
    def after_all_players_arrive(self):
        self.group.set_deciders_chosen_payoffs()


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


class StageThreeSelector(Page):
    def is_displayed(self):
        return self.player.role() == 'selector'


class DictatorTask(Page):
    form_model = 'player'
    form_fields = ['amount_keep', 'amount_give']

    def is_displayed(self):
        return self.player.role() == 'partner' and self.player.selected

    def error_message(self, values):
        if values['amount_keep'] + values['amount_give'] != C.ENDOWMENT_STAGE_THREE:
            return 'The points have to add up to ' + str(C.ENDOWMENT_STAGE_THREE)


class DictatorPayoffsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_dictator_payoffs()


class DictatorResults(Page):

    def is_displayed(self):
        return self.player.role() == 'selector'

    def vars_for_template(self):
        results = []

        for p in self.group.get_players():
            if p.role() == 'partner' and p.selected:
                results.append({
                    'id': p.id_in_group,
                    'blue_count': p.blue_count,
                    'amount_keep': p.amount_keep,
                    'amount_give': p.amount_give,
                    'earnings': p.amount_give - C.SELECTION_FEE if p.selected else c(0)
                })

        return { 'results': sorted(results, key=lambda r: r['blue_count']), }


class DictatorResultsDecider(Page):

    def is_displayed(self):
        return self.player.role() == 'partner' and self.player.selected


class FeedbackDeciders(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'


class EnvironmentPage3(Page):

    def is_displayed(self):
        return self.subsession.round_number == C.NUM_ROUNDS

    def vars_for_template(self):
        return { 'money_earned': self.participant.payoff.to_real_world_currency(self.session) }


class PayoffsWaitPage(WaitPage):

    def is_displayed(self):
        return self.subsession.round_number == C.NUM_ROUNDS

    def after_all_players_arrive(self):
        self.group.set_final_payoffs()


page_sequence = [
    Instructions,
    EnvironmentPage1,
    EnvironmentPage2,
    Role,
    RFTaskStart
] + [
    RFTask for i in range(C.RFTASK_NUM_ROUNDS)
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
