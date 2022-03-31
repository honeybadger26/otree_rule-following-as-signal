from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'thesis_demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        min=16, max=80,
        label=''
    )

    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        widget=widgets.RadioSelect,
        label=''
    )

    your_study = models.StringField(
        choices=['Psychology', 'Philosophy', 'Politics', 'Economics', 'Other'],
        label=''
    )

    reason = models.StringField(
        choices=['Science', 'Money', 'Other'],
        label=''
    )

    nr_similar_experiments = models.IntegerField(
        min=0, max=20,
        label=''
    )

    other_info = models.StringField(
        choices=['Yes', 'No'],
        label=''
    )

    real_humans = models.StringField(
        choices=['Yes', 'No'],
        label=''
    )

    show_debriefing = models.BooleanField()
