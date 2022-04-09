from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import sys


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'thesis_instructions'
    players_per_group = None
    num_rounds = 1

    player_instructions = 'thesis_instructions/PlayerInstructions.html'
    selector_instructions = 'thesis_instructions/SelectorInstructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    name = models.StringField(
        label='Surname, First Name'
    )

    consent = models.BooleanField(
        label='I herewith consent to participate in this study.',
        widget=widgets.CheckboxInput
    )

    read = models.BooleanField(
        label='I herewith confirm that I have read and understood the information '
              'above.',
        widget=widgets.CheckboxInput
    )

    continue_consent = models.BooleanField()

    continue_instructions = models.BooleanField()

    continue_experiment = models.BooleanField()

    comprehension1 = models.IntegerField(
        choices=[
            [1, '2 stages'],
            [2, '3 stages'],
            [3, '4 stages']
            ],
        label=''
    )

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

    def make_understood_field(label):
        return models.BooleanField(
            label='I herewith confirm that I have read and understood the information of ' + label + '.',
            widget=widgets.CheckboxInput
        )

    understood1 = make_understood_field('the general instructions')
    understood11 = make_understood_field('the "Roles" section')
    understood12 = make_understood_field('the "General Structure" section')
    understood13 = make_understood_field('the "Payment" section')
    understood2 = make_understood_field('"Part 1"')
    understood21 = make_understood_field('stage 1')
    understood22 = make_understood_field('stage 2')
    understood23 = make_understood_field('stage 3')
    understood24 = make_understood_field('the "End of a Round in Part 1" section')





