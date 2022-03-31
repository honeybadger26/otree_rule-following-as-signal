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
    num_rounds = 30
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
            choices=[
                [True, 'selected'],
                [False, 'not selected']
                ],
            label='select this decider for Stage 3',
            widget=widgets.CheckboxInput,
            blank=True
        )

    def make_dictator_choice_keep_field():
        return models.CurrencyField(
            choices=[c(250), c(300), c(350), c(400), c(450), c(500)],
            label=''
        )

    def make_dictator_choice_give_field():
        return models.CurrencyField(
            choices=[c(0), c(50), c(100), c(150), c(200), c(250)],
            label=''
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

    partner_highest = models.IntegerField(
        initial=0,
        blank=True
    )

    partner_middle = models.IntegerField(
        initial=0,
        blank=True
    )

    partner_lowest = models.IntegerField(
        initial=0,
        blank=True
    )

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

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)

        #keep
        dictator111 = self.in_round(Constants.payoff_round1).dictator_choice11 if self.in_round(Constants.payoff_round1).dictator_choice11 is not None else c(0)
        dictator112 = self.in_round(Constants.payoff_round2).dictator_choice11 if self.in_round(Constants.payoff_round2).dictator_choice11 is not None else c(0)
        dictator121 = self.in_round(Constants.payoff_round1).dictator_choice21 if self.in_round(Constants.payoff_round1).dictator_choice21 is not None else c(0)
        dictator122 = self.in_round(Constants.payoff_round2).dictator_choice21 if self.in_round(Constants.payoff_round2).dictator_choice21 is not None else c(0)
        dictator131 = self.in_round(Constants.payoff_round1).dictator_choice31 if self.in_round(Constants.payoff_round1).dictator_choice31 is not None else c(0)
        dictator132 = self.in_round(Constants.payoff_round2).dictator_choice31 if self.in_round(Constants.payoff_round2).dictator_choice31 is not None else c(0)

        #give
        dictator211 = self.in_round(Constants.payoff_round1).dictator_choice12 if self.in_round(Constants.payoff_round1).dictator_choice12 is not None else c(0)
        dictator212 = self.in_round(Constants.payoff_round2).dictator_choice12 if self.in_round(Constants.payoff_round2).dictator_choice12 is not None else c(0)
        dictator221 = self.in_round(Constants.payoff_round1).dictator_choice22 if self.in_round(Constants.payoff_round1).dictator_choice22 is not None else c(0)
        dictator222 = self.in_round(Constants.payoff_round2).dictator_choice22 if self.in_round(Constants.payoff_round2).dictator_choice22 is not None else c(0)
        dictator231 = self.in_round(Constants.payoff_round1).dictator_choice32 if self.in_round(Constants.payoff_round1).dictator_choice32 is not None else c(0)
        dictator232 = self.in_round(Constants.payoff_round2).dictator_choice32 if self.in_round(Constants.payoff_round2).dictator_choice32 is not None else c(0)
        dictator = dictator211 + dictator212 + dictator221 + dictator222 + dictator231 + dictator232

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
        select = select11 + select21 + select31 + select12 + select22 + select32

        p1.payoff = self.in_round(Constants.payoff_round1).payoff_rf1 + self.in_round(Constants.payoff_round2).payoff_rf1 + dictator111 + dictator112 + dieroll11 + dieroll12 + Constants.dieroll_points[self.dieroll_end1-1]
        p2.payoff = self.in_round(Constants.payoff_round1).payoff_rf2 + self.in_round(Constants.payoff_round2).payoff_rf2 + dictator121 + dictator122 + dieroll21 + dieroll22 + Constants.dieroll_points[self.dieroll_end2-1]
        p3.payoff = self.in_round(Constants.payoff_round1).payoff_rf3 + self.in_round(Constants.payoff_round2).payoff_rf3 + dictator131 + dictator132 + dieroll31 + dieroll32 + Constants.dieroll_points[self.dieroll_end3-1]
        p4.payoff = (Constants.endowment_selection * 2) - (Constants.selection_fee * select) + dictator + dieroll + Constants.dieroll_points[self.dieroll_end4-1]

        self.one = self.in_round(Constants.payoff_round1).payoff_rf1 + self.in_round(Constants.payoff_round2).payoff_rf1
        self.two = dictator111 + dictator112
        self.three = dieroll11 + dieroll12
        self.four = Constants.dieroll_points[self.dieroll_end1-1]
        self.five = self.one + self.two + self.three + self.four


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

    yellow_choice101 = make_bucket_choice_field()
    yellow_choice102 = make_bucket_choice_field()
    yellow_choice103 = make_bucket_choice_field()
    yellow_choice104 = make_bucket_choice_field()
    yellow_choice105 = make_bucket_choice_field()
    yellow_choice106 = make_bucket_choice_field()
    yellow_choice107 = make_bucket_choice_field()
    yellow_choice108 = make_bucket_choice_field()
    yellow_choice109 = make_bucket_choice_field()
    yellow_choice110 = make_bucket_choice_field()
    yellow_choice111 = make_bucket_choice_field()
    yellow_choice112 = make_bucket_choice_field()
    yellow_choice113 = make_bucket_choice_field()
    yellow_choice114 = make_bucket_choice_field()
    yellow_choice115 = make_bucket_choice_field()

    yellow_choice201 = make_bucket_choice_field()
    yellow_choice202 = make_bucket_choice_field()
    yellow_choice203 = make_bucket_choice_field()
    yellow_choice204 = make_bucket_choice_field()
    yellow_choice205 = make_bucket_choice_field()
    yellow_choice206 = make_bucket_choice_field()
    yellow_choice207 = make_bucket_choice_field()
    yellow_choice208 = make_bucket_choice_field()
    yellow_choice209 = make_bucket_choice_field()
    yellow_choice210 = make_bucket_choice_field()
    yellow_choice211 = make_bucket_choice_field()
    yellow_choice212 = make_bucket_choice_field()
    yellow_choice213 = make_bucket_choice_field()
    yellow_choice214 = make_bucket_choice_field()
    yellow_choice215 = make_bucket_choice_field()

    yellow_choice301 = make_bucket_choice_field()
    yellow_choice302 = make_bucket_choice_field()
    yellow_choice303 = make_bucket_choice_field()
    yellow_choice304 = make_bucket_choice_field()
    yellow_choice305 = make_bucket_choice_field()
    yellow_choice306 = make_bucket_choice_field()
    yellow_choice307 = make_bucket_choice_field()
    yellow_choice308 = make_bucket_choice_field()
    yellow_choice309 = make_bucket_choice_field()
    yellow_choice310 = make_bucket_choice_field()
    yellow_choice311 = make_bucket_choice_field()
    yellow_choice312 = make_bucket_choice_field()
    yellow_choice313 = make_bucket_choice_field()
    yellow_choice314 = make_bucket_choice_field()
    yellow_choice315 = make_bucket_choice_field()

    blue_choice101 = make_bucket_choice_field()
    blue_choice102 = make_bucket_choice_field()
    blue_choice103 = make_bucket_choice_field()
    blue_choice104 = make_bucket_choice_field()
    blue_choice105 = make_bucket_choice_field()
    blue_choice106 = make_bucket_choice_field()
    blue_choice107 = make_bucket_choice_field()
    blue_choice108 = make_bucket_choice_field()
    blue_choice109 = make_bucket_choice_field()
    blue_choice110 = make_bucket_choice_field()
    blue_choice111 = make_bucket_choice_field()
    blue_choice112 = make_bucket_choice_field()
    blue_choice113 = make_bucket_choice_field()
    blue_choice114 = make_bucket_choice_field()
    blue_choice115 = make_bucket_choice_field()

    blue_choice202 = make_bucket_choice_field()
    blue_choice201 = make_bucket_choice_field()
    blue_choice203 = make_bucket_choice_field()
    blue_choice204 = make_bucket_choice_field()
    blue_choice205 = make_bucket_choice_field()
    blue_choice206 = make_bucket_choice_field()
    blue_choice207 = make_bucket_choice_field()
    blue_choice208 = make_bucket_choice_field()
    blue_choice209 = make_bucket_choice_field()
    blue_choice210 = make_bucket_choice_field()
    blue_choice211 = make_bucket_choice_field()
    blue_choice212 = make_bucket_choice_field()
    blue_choice213 = make_bucket_choice_field()
    blue_choice214 = make_bucket_choice_field()
    blue_choice215 = make_bucket_choice_field()

    blue_choice301 = make_bucket_choice_field()
    blue_choice302 = make_bucket_choice_field()
    blue_choice303 = make_bucket_choice_field()
    blue_choice304 = make_bucket_choice_field()
    blue_choice305 = make_bucket_choice_field()
    blue_choice306 = make_bucket_choice_field()
    blue_choice307 = make_bucket_choice_field()
    blue_choice308 = make_bucket_choice_field()
    blue_choice309 = make_bucket_choice_field()
    blue_choice310 = make_bucket_choice_field()
    blue_choice311 = make_bucket_choice_field()
    blue_choice312 = make_bucket_choice_field()
    blue_choice313 = make_bucket_choice_field()
    blue_choice314 = make_bucket_choice_field()
    blue_choice315 = make_bucket_choice_field()

    balls = models.IntegerField(
        initial=1,
        blank=True)

    bucket_num = models.IntegerField(
        initial=1,
        blank=True
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








