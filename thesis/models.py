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
    num_rounds = 2 # TODO: Default is 30
    payoff_round1 = random.randint(1, num_rounds/2)
    payoff_round2 = random.randint((num_rounds/2)+1, num_rounds)

    rf_instructions = 'thesis/InstructionsRF.html'
    rf_instructions2 = 'thesis/InstructionsRF2.html'
    selection_instructions = 'thesis/InstructionsSelection.html'
    selection_instructions2 = 'thesis/InstructionsSelection2.html'
    dictator_instructions = 'thesis/InstructionsDictator.html'
    dictator_instructions2 = 'thesis/InstructionsDictator2.html'
    dictator_instructions3 = 'thesis/InstructionsDictator3.html'
    dieroll_instructions = 'thesis/InstructionsDieRoll.html'
    dieroll_instructions2 = 'thesis/InstructionsDieRoll2.html'
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

    def make_selected_player_field():
        return models.BooleanField(
            label='Select this decider for Stage 3',
            widget=widgets.CheckboxInput,
            blank=True
        )

    def make_dictator_choice_keep_field():
        return models.CurrencyField(
            choices=[c(250), c(300), c(350), c(400), c(450), c(500)],
            label='Keep for yourself'
        )

    def make_dictator_choice_give_field():
        return models.CurrencyField(
            choices=[c(0), c(50), c(100), c(150), c(200), c(250)],
            label='Give to selector'
        )

    def make_die_roll_field():
        return models.IntegerField(
            min=1, max=6,
            label='',
            blank=True
        )

    all_players = models.IntegerField(
        initial=random.shuffle([1, 2, 3, 4])
    )

    partner1 = make_partner_number_field(0)
    partner2 = make_partner_number_field(1)
    partner3 = make_partner_number_field(2)

    decider_highest = models.IntegerField(
        initial=0,
        blank=True
    )

    decider_middle = models.IntegerField(
        initial=0,
        blank=True
    )

    decider_lowest = models.IntegerField(
        initial=0,
        blank=True
    )

    # TODO: get rid of these
    yellow_counter1 = make_bucket_counter_field()
    yellow_counter2 = make_bucket_counter_field()
    yellow_counter3 = make_bucket_counter_field()
    blue_counter1 = make_bucket_counter_field()
    blue_counter2 = make_bucket_counter_field()
    blue_counter3 = make_bucket_counter_field()

    select1 = make_selected_player_field()
    select2 = make_selected_player_field()
    select3 = make_selected_player_field()

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

    one = models.CurrencyField(initial=0)
    two = models.CurrencyField(initial=0)
    three = models.CurrencyField(initial=0)
    four= models.CurrencyField(initial=0)
    five = models.CurrencyField(initial=0)

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
        dictator111 = self.in_round(Constants.payoff_round1).dictator_choice11 if self.in_round(Constants.payoff_round1).field_maybe_none('dictator_choice11') is not None else c(0)
        dictator112 = self.in_round(Constants.payoff_round2).dictator_choice11 if self.in_round(Constants.payoff_round2).field_maybe_none('dictator_choice11') is not None else c(0)
        dictator121 = self.in_round(Constants.payoff_round1).dictator_choice21 if self.in_round(Constants.payoff_round1).field_maybe_none('dictator_choice21') is not None else c(0)
        dictator122 = self.in_round(Constants.payoff_round2).dictator_choice21 if self.in_round(Constants.payoff_round2).field_maybe_none('dictator_choice21') is not None else c(0)
        dictator131 = self.in_round(Constants.payoff_round1).dictator_choice31 if self.in_round(Constants.payoff_round1).field_maybe_none('dictator_choice31') is not None else c(0)
        dictator132 = self.in_round(Constants.payoff_round2).dictator_choice31 if self.in_round(Constants.payoff_round2).field_maybe_none('dictator_choice31') is not None else c(0)

        #give
        dictator211 = self.in_round(Constants.payoff_round1).dictator_choice12 if self.in_round(Constants.payoff_round1).field_maybe_none('dictator_choice12') is not None else c(0)
        dictator212 = self.in_round(Constants.payoff_round2).dictator_choice12 if self.in_round(Constants.payoff_round2).field_maybe_none('dictator_choice12') is not None else c(0)
        dictator221 = self.in_round(Constants.payoff_round1).dictator_choice22 if self.in_round(Constants.payoff_round1).field_maybe_none('dictator_choice22') is not None else c(0)
        dictator222 = self.in_round(Constants.payoff_round2).dictator_choice22 if self.in_round(Constants.payoff_round2).field_maybe_none('dictator_choice22') is not None else c(0)
        dictator231 = self.in_round(Constants.payoff_round1).dictator_choice32 if self.in_round(Constants.payoff_round1).field_maybe_none('dictator_choice32') is not None else c(0)
        dictator232 = self.in_round(Constants.payoff_round2).dictator_choice32 if self.in_round(Constants.payoff_round2).field_maybe_none('dictator_choice32') is not None else c(0)
        dictator = dictator211 + dictator212 + dictator221 + dictator222 + dictator231 + dictator232

        dieroll11 = Constants.dieroll_points[self.in_round(Constants.payoff_round1).die_roll1-1] if self.in_round(Constants.payoff_round1).field_maybe_none('die_roll1') is not None else c(0)
        dieroll12 = Constants.dieroll_points[self.in_round(Constants.payoff_round2).die_roll1-1] if self.in_round(Constants.payoff_round2).field_maybe_none('die_roll1') is not None else c(0)
        dieroll21 = Constants.dieroll_points[self.in_round(Constants.payoff_round1).die_roll2-1] if self.in_round(Constants.payoff_round1).field_maybe_none('die_roll2') is not None else c(0)
        dieroll22 = Constants.dieroll_points[self.in_round(Constants.payoff_round2).die_roll2-1] if self.in_round(Constants.payoff_round2).field_maybe_none('die_roll2') is not None else c(0)
        dieroll31 = Constants.dieroll_points[self.in_round(Constants.payoff_round1).die_roll3-1] if self.in_round(Constants.payoff_round1).field_maybe_none('die_roll3') is not None else c(0)
        dieroll32 = Constants.dieroll_points[self.in_round(Constants.payoff_round2).die_roll3-1] if self.in_round(Constants.payoff_round2).field_maybe_none('die_roll3') is not None else c(0)
        dieroll = dieroll11 + dieroll12 + dieroll21 + dieroll22 + dieroll31 + dieroll32

        selected_count = \
            self.get_selected_count(Constants.payoff_round1) + \
            self.get_selected_count(Constants.payoff_round2)

        p1.payoff = self.in_round(Constants.payoff_round1).payoff_rf1 + self.in_round(Constants.payoff_round2).payoff_rf1 + dictator111 + dictator112 + dieroll11 + dieroll12 + Constants.dieroll_points[self.dieroll_end1-1]
        p2.payoff = self.in_round(Constants.payoff_round1).payoff_rf2 + self.in_round(Constants.payoff_round2).payoff_rf2 + dictator121 + dictator122 + dieroll21 + dieroll22 + Constants.dieroll_points[self.dieroll_end2-1]
        p3.payoff = self.in_round(Constants.payoff_round1).payoff_rf3 + self.in_round(Constants.payoff_round2).payoff_rf3 + dictator131 + dictator132 + dieroll31 + dieroll32 + Constants.dieroll_points[self.dieroll_end3-1]
        p4.payoff = (Constants.endowment_selection * 2) - (Constants.selection_fee * selected_count) + dictator + dieroll + Constants.dieroll_points[self.dieroll_end4-1]

        self.one = self.in_round(Constants.payoff_round1).payoff_rf1 + self.in_round(Constants.payoff_round2).payoff_rf1
        self.two = dictator111 + dictator112
        self.three = dieroll11 + dieroll12
        self.four = Constants.dieroll_points[self.dieroll_end1-1]
        self.five = self.one + self.two + self.three + self.four


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

    continue_env1 = models.BooleanField()
    continue_env2 = models.BooleanField()

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
