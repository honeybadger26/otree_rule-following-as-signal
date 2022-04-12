from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
)
import random

author = 'Sebastian Simon'

doc = """
In this app, four players take part in a three-stage experiment including three stages: the bucket game, a 
partner selection stage, and two environments comprised of a dictator game and a die roll game. These three stages 
repeat 20 times. 
"""

class C(BaseConstants):
    NAME_IN_URL = 'thesis'
    PLAYERS_PER_GROUP = 4
    PT1_NUM_ROUNDS = 1
    PT2_NUM_ROUNDS = 1
    NUM_ROUNDS = PT1_NUM_ROUNDS + PT2_NUM_ROUNDS # TODO: Default is 30
    PAYOFF_ROUND1 = random.randint(1, PT1_NUM_ROUNDS)
    PAYOFF_ROUND2 = random.randint(PT1_NUM_ROUNDS+1, NUM_ROUNDS)
    RFTASK_NUM_ROUNDS = 15

    ENDOWMENT_SELECTION = c(450)
    ENDOWMENT_STAGE_THREE = c(500)
    SELECTION_FEE = c(150)
    KEEP_AMOUNTS = [c(250), c(300), c(350), c(400), c(450), c(500)]
    GIVE_AMOUNTS = [c(0), c(50), c(100), c(150), c(200), c(250)]

    PARTNER_SELECTOR = 4


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    num_selected = models.IntegerField(initial=0)

    def make_selected_player_field():
        return models.BooleanField(
            label='Select this decider for Stage 3',
            widget=widgets.CheckboxInput,
            blank=True,
            initial=False
        )

    # TODO: remove these?
    select1 = make_selected_player_field()
    select2 = make_selected_player_field()
    select3 = make_selected_player_field()

    def set_selector_initial_payoff(self):
        self.get_player_by_id(4).payoff += C.ENDOWMENT_SELECTION

    def set_deciders_chosen_payoffs(self):
        for p in self.get_players():
            if p.id_in_group == 4:
                continue

            if (p.id_in_group == 1 and self.select1) or \
                (p.id_in_group == 2 and self.select2) or \
                (p.id_in_group == 3 and self.select3):
                self.num_selected += 1
                p.selected = True
                p.payoff += C.ENDOWMENT_STAGE_THREE

        self.get_player_by_id(4).payoff -= self.num_selected * C.SELECTION_FEE

    def set_dictator_payoffs(self):
        amount_given = c(0)

        for p in self.get_players():
            if p.field_maybe_none('amount_give') is not None:
                p.payoff -= p.amount_give
                amount_given += p.amount_give
        
        self.get_player_by_id(4).payoff += amount_given

    def set_final_payoffs(self):
        for p in self.get_players():
            p.participant.payoff = 0
            p.payoff = \
                p.in_round(C.PAYOFF_ROUND1).payoff + \
                p.in_round(C.PAYOFF_ROUND2).payoff
        

class Player(BasePlayer):

    def role(self):
        return 'selector' if self.id_in_group == C.PARTNER_SELECTOR else 'partner'

    def get_select_display(self):
        return 'selected' if self.selected else 'not selected'

    def make_understood_field(label):
        return models.BooleanField(
            label='I herewith confirm that I have read and understood the information of ' + label + '.',
            widget=widgets.CheckboxInput
        )

    def set_rf_payoff(self):
        endowment_yellow = c(0)
        endowment_blue = c(0)

        if self.subsession.round_number <= C.PT1_NUM_ROUNDS:
            endowment_yellow = c(self.session.config['pt1_endowment_yellow'])
            endowment_blue = c(self.session.config['pt1_endowment_blue'])
        elif self.subsession.round_number <= C.NUM_ROUNDS:
            endowment_yellow = c(self.session.config['pt2_endowment_yellow'])
            endowment_blue = c(self.session.config['pt2_endowment_blue'])

        if self.yellow_choice:
            self.payoff += endowment_yellow
        elif self.blue_choice:
            self.payoff += endowment_blue

    def get_current_ball_num(self):
            return self.yellow_count + self.blue_count + 1

    yellow_choice = models.BooleanField()
    blue_choice = models.BooleanField()

    yellow_count = models.IntegerField(initial=0)
    blue_count = models.IntegerField(initial=0)
    
    selected = models.BooleanField(
        label='Select this decider for Stage 3',
        widget=widgets.CheckboxInput,
        initial=False)

    amount_keep = models.CurrencyField(
        choices=[c(250), c(300), c(350), c(400), c(450), c(500)],
        label='Keep for yourself')

    amount_give = models.CurrencyField(
        choices=[c(0), c(50), c(100), c(150), c(200), c(250)],
        label='Give to selector')

    understood1 = make_understood_field('the general instructions')
    understood11 = make_understood_field('the "Roles" section')
    understood12 = make_understood_field('the "General Structure" section')
    understood13 = make_understood_field('the "Payment" section')
    understood2 = make_understood_field('"Part 1"')
    understood21 = make_understood_field('stage 1')
    understood22 = make_understood_field('stage 2')
    understood23 = make_understood_field('stage 3')
    understood24 = make_understood_field('the "End of a Round in Part 1" section')
    understood3 = make_understood_field('"Part 2"')
    understood31 = make_understood_field('stage 1')
    understood32 = make_understood_field('stage 2')
    understood33 = make_understood_field('stage 3')
    understood34 = make_understood_field('the "Feedback in Part 1" section')

    comprehension1 = models.IntegerField(
        choices=[
            [1, '2 stages'],
            [2, '3 stages'],
            [3, '4 stages']
            ],
        label='')

    comprehension2 = models.IntegerField(
        choices=[
            [1, 'Place each ball into the yellow bucket'],
            [2, 'Place each ball into the blue bucket']
        ],
        label=''
    )

    comprehension3 = models.IntegerField(
        choices=[
            [1, 'Between 1 and 3'],
            [2, 'Between 0 and 3'],
            [3, 'Only 1'],
        ],
        label='')

    comprehension4 = models.IntegerField(
        choices=[
            [1, 'He or she will not take part in stage 3'],
            [2, 'He or she will do the task alone'],
        ],
        label='')

    comprehension5 = models.IntegerField(
        choices=[
            [1, 'Nothing'],
            [2, '100 points'],
            [3, '150 points'],
        ],
        label='')

    comprehension6 = models.IntegerField(
        choices=[
            [1, '100 points'],
            [2, '250 points'],
            [3, '500 points'],
        ],
        label='')

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
        label='')