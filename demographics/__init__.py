from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.IntegerField(
        min=16, max=80,
        label='Your age')

    gender = models.StringField(
        choices=['Male', 'Female', 'Other'],
        widget=widgets.RadioSelectHorizontal,
        label='Your gender')

    your_study = models.StringField(
        choices=[
            'Business/Marketing',
            'Economics', 
            'Engineering',
            'Medicine/Health sciences',
            'Natural sciences',
            'Philosophy', 
            'Politics', 
            'Psychology', 
            'Social Sciences',
            'Other',
            'Not a student',
        ],
        label='Your field of study')

    nr_similar_experiments = models.IntegerField(
        min=0, max=20,
        label='How many experiments have you done in MonLEE in the past?')


class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'your_study',
        'nr_similar_experiments',
    ]

page_sequence = [Demographics]
