from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range,
)
import random
import array as arr


author = 'Sebastian Simon'

doc = """
In this app, four players take part in a three-stage experiment including three stages: the bucket game, a 
partner selection stage, and two environments comprised of a dictator game and a die roll game. These three stages 
repeat 20 times. 
"""


class Constants(BaseConstants):
    name_in_url = 'thesis'
    players_per_group = 4
    pt1_num_rounds = 1
    pt2_num_rounds = 1
    num_rounds = pt1_num_rounds + pt2_num_rounds # TODO: Default is 30
    payoff_round1 = random.randint(1, pt1_num_rounds)
    payoff_round2 = random.randint(pt1_num_rounds+1, num_rounds)
    rftask_num_rounds = 15

    rf_instructions = 'thesis/InstructionsRF.html'
    rf_instructions2 = 'thesis/InstructionsRF2.html'
    selection_instructions = 'thesis/InstructionsSelection.html'
    selection_instructions2 = 'thesis/InstructionsSelection2.html'
    dictator_instructions = 'thesis/InstructionsDictator.html'
    dictator_instructions2 = 'thesis/InstructionsDictator2.html'
    dictator_instructions3 = 'thesis/InstructionsDictator3.html'

    endowment_selection = c(450)
    endowment_stage_three = c(500)
    endowment_yellow = c(15)
    endowment_blue = c(5)
    selection_fee = c(150)

    partner_selector = 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def make_selected_player_field():
        return models.BooleanField(
            label='Select this decider for Stage 3',
            widget=widgets.CheckboxInput,
            blank=True
        )

    # TODO: remove these
    select1 = make_selected_player_field()
    select2 = make_selected_player_field()
    select3 = make_selected_player_field()

    #Payoffs
    payoff_rf1 = models.CurrencyField(initial=0)
    payoff_rf2 = models.CurrencyField(initial=0)
    payoff_rf3 = models.CurrencyField(initial=0)

    def get_selected_count(self, round_num):
        count = 0
        g = self.in_round(round_num)

        for p in g.get_players():
            if p.selected:
                count += 1

        return count

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)

        #keep
        dictator111 = p1.in_round(Constants.payoff_round1).amount_keep if p1.in_round(Constants.payoff_round1).field_maybe_none('amount_keep') is not None else c(0)
        dictator121 = p2.in_round(Constants.payoff_round1).amount_keep if p2.in_round(Constants.payoff_round1).field_maybe_none('amount_keep') is not None else c(0)
        dictator131 = p3.in_round(Constants.payoff_round1).amount_keep if p3.in_round(Constants.payoff_round1).field_maybe_none('amount_keep') is not None else c(0)

        #give
        dictator211 = p1.in_round(Constants.payoff_round1).amount_give if p1.in_round(Constants.payoff_round1).field_maybe_none('amount_give') is not None else c(0)
        dictator212 = p1.in_round(Constants.payoff_round2).amount_give if p1.in_round(Constants.payoff_round2).field_maybe_none('amount_give') is not None else c(0)
        dictator221 = p2.in_round(Constants.payoff_round1).amount_give if p2.in_round(Constants.payoff_round1).field_maybe_none('amount_give') is not None else c(0)
        dictator222 = p2.in_round(Constants.payoff_round2).amount_give if p2.in_round(Constants.payoff_round2).field_maybe_none('amount_give') is not None else c(0)
        dictator231 = p3.in_round(Constants.payoff_round1).amount_give if p3.in_round(Constants.payoff_round1).field_maybe_none('amount_give') is not None else c(0)
        dictator232 = p3.in_round(Constants.payoff_round2).amount_give if p3.in_round(Constants.payoff_round2).field_maybe_none('amount_give') is not None else c(0)
        dictator = dictator211 + dictator212 + dictator221 + dictator222 + dictator231 + dictator232

        selected_count = \
            self.get_selected_count(Constants.payoff_round1) + \
            self.get_selected_count(Constants.payoff_round2)

        p1.payoff = self.in_round(Constants.payoff_round1).payoff_rf1 + self.in_round(Constants.payoff_round2).payoff_rf1 + dictator111
        p2.payoff = self.in_round(Constants.payoff_round1).payoff_rf2 + self.in_round(Constants.payoff_round2).payoff_rf2 + dictator121
        p3.payoff = self.in_round(Constants.payoff_round1).payoff_rf3 + self.in_round(Constants.payoff_round2).payoff_rf3 + dictator131
        p4.payoff = (Constants.endowment_selection * 2) - (Constants.selection_fee * selected_count) + dictator

class Player(BasePlayer):

    def role(self):
        return 'selector' if self.id_in_group == Constants.partner_selector else 'partner'

    def get_select_display(self):
        return 'selected' if self.selected else 'not selected'

    def make_bucket_choice_field():
        return models.IntegerField(
            initial=0,
            blank=True
        )

    def make_understood_field(label):
        return models.BooleanField(
            label='I herewith confirm that I have read and understood the information of ' + label + '.',
            widget=widgets.CheckboxInput
        )

    yellow_choice = models.BooleanField()
    blue_choice = models.BooleanField()

    yellow_count = models.IntegerField(initial=0)
    blue_count = models.IntegerField(initial=0)
    
    yellow_score = models.CurrencyField(initial=0)
    blue_score = models.CurrencyField(initial=0)

    selected = models.BooleanField(
        label='Select this decider for Stage 3',
        widget=widgets.CheckboxInput,
        initial=False
    )

    amount_keep = models.CurrencyField(
        choices=[c(250), c(300), c(350), c(400), c(450), c(500)],
        label='Keep for yourself'
    )

    amount_give = models.CurrencyField(
        choices=[c(0), c(50), c(100), c(150), c(200), c(250)],
        label='Give to selector'
    )

    understood3 = make_understood_field('"Part 2"')
    understood31 = make_understood_field('stage 1')
    understood32 = make_understood_field('stage 2')
    understood33 = make_understood_field('stage 3')
    understood34 = make_understood_field('the "Feedback in Part 1" section')

    comprehension7 = models.IntegerField(
        choices=[
            [1, '0 points each'],
            [2, '150 points each'],
            [3, '250 points each']
        ],
        label='')

    comprehension8 = models.IntegerField(
        choices=[
            [1, '0 points each'],
            [2, '150 points each'],
            [3, '250 points each']
        ],
        label=''
    )
