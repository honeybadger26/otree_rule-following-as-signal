from otree.api import *

# Models #

class C(BaseConstants):
    NAME_IN_URL = 'debriefing'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    show_payoff = models.BooleanField()


# Pages #

class Debriefing(Page):
    pass


page_sequence = [Debriefing]
