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