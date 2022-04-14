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
        choices=['Psychology', 'Philosophy', 'Politics', 'Economics', 'Other'],
        label='Your field of study')

    reason = models.StringField(
        choices=['Science', 'Money', 'Other'],
        label='Why did you participate in this study?')

    nr_similar_experiments = models.IntegerField(
        min=0, max=20,
        label='In how many experiments similar to this one did you participate already?')

    other_info = models.StringField(
        choices=['Yes', 'No'],
        label='Did you receive all information about this experiment during the experiment?')

    real_humans = models.StringField(
        choices=['Yes', 'No'],
        label='Do you believe you interacted with real humans?')


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age',
                   'gender',
                   'your_study',
                   'reason',
                   'nr_similar_experiments',
                   'other_info',
                   'real_humans']

page_sequence = [Demographics]
