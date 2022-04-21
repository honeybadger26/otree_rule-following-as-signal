from otree.api import *

# Models #

class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label='Surname, First Name')

    consent = models.BooleanField(
        label='I consent to participate in this study.',
        widget=widgets.CheckboxInput)

    read = models.BooleanField(
        label='I herewith confirm that I have read and understood the information '
              'above.',
        widget=widgets.CheckboxInput)

# Pages #

class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['consent']


class InformationBrochure(Page):
    form_model = 'player'
    form_fields = ['read']


page_sequence = [
    InformedConsent,
    InformationBrochure,
]
