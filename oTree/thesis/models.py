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
    num_rounds = 2
    payoff_round1 = 1
    payoff_round2 = 2

    rf_instructions = 'thesis/InstructionsRF.html'
    selection_instructions = 'thesis/InstructionsSelection.html'
    dictator_instructions = 'thesis/InstructionsDictator.html'
    dieroll_instructions = 'thesis/InstructionsDieRoll.html'
    dieroll_instructions_end = 'thesis/InstructionsDieRollEnd.html'

    endowment_selection = c(450)
    endowment_stage_three = c(500)
    endowment_yellow = c(15)
    endowment_blue = c(5)
    multiplier = 1
    dieroll_points = [c(0), c(50), c(100), c(150), c(200), c(250)]

    selection_fee = c(150)

    all_players = [1, 2, 3, 4]
    partner_selector = all_players[3]
    select_partners = all_players.pop(partner_selector-1)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_payoff(self):
        buyer = self.get_player_by_role('buyer')
        print(buyer.decision)

    def make_partner_number_field(number):
        return models.IntegerField(
            initial=Constants.all_players[number],
            blank=True
        )

    def make_bucket_counter_field():
        return models.IntegerField(
            initial=0,
            blank=True
        )

    def make_selected_player_field(label):
        return models.BooleanField(
            choices=[
                [True, 'selected'],
                [False, 'not selected']
                ],
            label=label,
            widget=widgets.CheckboxInput,
            blank=True
        )

    def make_dictator_choice_keep_field():
        return models.CurrencyField(
            choices=[c(250), c(300), c(350), c(400), c(450), c(500)],
            label='',
            initial=0
        )

    def make_dictator_choice_give_field():
        return models.CurrencyField(
            choices=[c(250), c(200), c(150), c(100), c(50), c(0)],
            label='',
            initial=0
        )

    def make_die_roll_field():
        return models.IntegerField(
            min=1, max=6,
            label='You just rolled the dice. What is the result of the roll?'
        )

    all_players = models.IntegerField(
        initial=random.shuffle([1, 2, 3, 4])
    )

    partner1 = make_partner_number_field(0)
    partner2 = make_partner_number_field(1)
    partner3 = make_partner_number_field(2)

    yellow_counter1 = make_bucket_counter_field()
    yellow_counter2 = make_bucket_counter_field()
    yellow_counter3 = make_bucket_counter_field()
    blue_counter1 = make_bucket_counter_field()
    blue_counter2 = make_bucket_counter_field()
    blue_counter3 = make_bucket_counter_field()

    select1 = make_selected_player_field('The first one')
    select2 = make_selected_player_field('The second one')
    select3 = make_selected_player_field('The third one')

    dictator_choice11 = make_dictator_choice_keep_field()
    dictator_choice21 = make_dictator_choice_keep_field()
    dictator_choice31 = make_dictator_choice_keep_field()
    dictator_choice12 = make_dictator_choice_give_field()
    dictator_choice22 = make_dictator_choice_give_field()
    dictator_choice32 = make_dictator_choice_give_field()

    die_roll1 = make_die_roll_field()
    die_roll2 = make_die_roll_field()
    die_roll3 = make_die_roll_field()

    dieroll_end1 = make_die_roll_field()
    dieroll_end2 = make_die_roll_field()
    dieroll_end3 = make_die_roll_field()
    dieroll_end4 = make_die_roll_field()

    #Payoffs

    payoff_rf1 = models.CurrencyField(initial=0)
    payoff_rf2 = models.CurrencyField(initial=0)
    payoff_rf3 = models.CurrencyField(initial=0)

    payoff_dictator4 = models.CurrencyField(initial=0)
    payoff_dieroll4 = models.CurrencyField(initial=0)

    payoff1 = models.CurrencyField()
    payoff2 = models.CurrencyField()
    payoff3 = models.CurrencyField()
    payoff4 = models.CurrencyField()

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)
        dictator111 = self.in_round(Constants.payoff_round1).dictator_choice11 if self.select1 is True else c(0)
        dictator112 = self.in_round(Constants.payoff_round2).dictator_choice11 if self.select1 is True else c(0)
        dictator121 = self.in_round(Constants.payoff_round1).dictator_choice21 if self.select2 is True else c(0)
        dictator122 = self.in_round(Constants.payoff_round2).dictator_choice21 if self.select2 is True else c(0)
        dictator131 = self.in_round(Constants.payoff_round1).dictator_choice31 if self.select3 is True else c(0)
        dictator132 = self.in_round(Constants.payoff_round2).dictator_choice31 if self.select3 is True else c(0)
        dieroll11 = Constants.dieroll_points[self.in_round(Constants.payoff_round1).die_roll1-1] if self.in_round(Constants.payoff_round1).die_roll1 is not None else c(0)
        dieroll12 = Constants.dieroll_points[self.in_round(Constants.payoff_round2).die_roll1-1] if self.in_round(Constants.payoff_round2).die_roll1 is not None else c(0)
        dieroll21 = Constants.dieroll_points[self.in_round(Constants.payoff_round1).die_roll2-1] if self.in_round(Constants.payoff_round1).die_roll2 is not None else c(0)
        dieroll22 = Constants.dieroll_points[self.in_round(Constants.payoff_round2).die_roll2-1] if self.in_round(Constants.payoff_round2).die_roll2 is not None else c(0)
        dieroll31 = Constants.dieroll_points[self.in_round(Constants.payoff_round1).die_roll3-1] if self.in_round(Constants.payoff_round1).die_roll3 is not None else c(0)
        dieroll32 = Constants.dieroll_points[self.in_round(Constants.payoff_round2).die_roll3-1] if self.in_round(Constants.payoff_round2).die_roll3 is not None else c(0)
        dieroll = dieroll11 + dieroll12 + dieroll21 + dieroll22 + dieroll31 + dieroll32
        select11 = 1 if self.in_round(Constants.payoff_round1).select1 is True else 0
        select12 = 1 if self.in_round(Constants.payoff_round2).select1 is True else 0
        select21 = 1 if self.in_round(Constants.payoff_round1).select2 is True else 0
        select22 = 1 if self.in_round(Constants.payoff_round2).select2 is True else 0
        select31 = 1 if self.in_round(Constants.payoff_round1).select3 is True else 0
        select32 = 1 if self.in_round(Constants.payoff_round2).select3 is True else 0
        select1 = select11 + select21 + select31
        select2 = select12 + select22 + select32
        dictator211 = self.in_round(Constants.payoff_round1).dictator_choice12 if self.select1 is True else c(0)
        dictator212 = self.in_round(Constants.payoff_round2).dictator_choice12 if self.select1 is True else c(0)
        dictator221 = self.in_round(Constants.payoff_round1).dictator_choice22 if self.select2 is True else c(0)
        dictator222 = self.in_round(Constants.payoff_round2).dictator_choice22 if self.select2 is True else c(0)
        dictator231 = self.in_round(Constants.payoff_round1).dictator_choice32 if self.select3 is True else c(0)
        dictator232 = self.in_round(Constants.payoff_round2).dictator_choice32 if self.select3 is True else c(0)
        dictator1 = dictator211 + dictator221 + dictator231
        dictator2 = dictator212 + dictator222 + dictator232
        p1.payoff = self.in_round(Constants.payoff_round1).payoff_rf1 + self.in_round(Constants.payoff_round2).payoff_rf1 + dictator111 + dictator112 + dieroll11 + dieroll12 + Constants.dieroll_points[self.dieroll_end1-1]
        p2.payoff = self.in_round(Constants.payoff_round1).payoff_rf2 + self.in_round(Constants.payoff_round2).payoff_rf2 + dictator121 + dictator122 + dieroll21 + dieroll22 + Constants.dieroll_points[self.dieroll_end2-1]
        p3.payoff = self.in_round(Constants.payoff_round1).payoff_rf3 + self.in_round(Constants.payoff_round2).payoff_rf3 + dictator131 + dictator132 + dieroll31 + dieroll32 + Constants.dieroll_points[self.dieroll_end3-1]
        p4.payoff = (Constants.endowment_selection * 2) - (Constants.selection_fee * (select1 + select2)) + dictator1 + dictator2 + dieroll + Constants.dieroll_points[self.dieroll_end4-1]


class Player(BasePlayer):

    def role(self):
        if self.id_in_group == Constants.partner_selector:
            return 'selector'
        else:
            return 'partner'

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

    yellow_choice1 = make_bucket_choice_field()
    yellow_choice2 = make_bucket_choice_field()
    yellow_choice3 = make_bucket_choice_field()
    blue_choice1 = make_bucket_choice_field()
    blue_choice2 = make_bucket_choice_field()
    blue_choice3 = make_bucket_choice_field()

    balls = models.IntegerField(
        initial=1,
        blank=True)

    continue_env1 = models.BooleanField()
    continue_env2 = models.BooleanField()

    understood3 = make_understood_field('"Part 2"')
    understood31 = make_understood_field('stage 1')
    understood32 = make_understood_field('stage 2')
    understood33 = make_understood_field('stage 3')
    understood34 = make_understood_field('the "End of a Round in Part 1" section')

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








