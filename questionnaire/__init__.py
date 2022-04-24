from otree.api import *

NINE_POINT_CHOICES = [
    [1, 'Strongly disagree'],
    [2, ''],
    [3, ''],
    [4, ''],
    [5, ''],
    [6, ''],
    [7, ''],
    [8, ''],
    [9, 'Strongly agree'],
]
FIVE_POINT_CHOICES = [
    [1, 'Strongly disagree'],
    [2, 'Disagree'],
    [3, 'Neutral (neight agree, nor disagree)'],
    [4, 'Agree'],
    [5, 'Strongly agree'],
]
FIVE_POINT_CHOICES_REVERSED = [
    [i+1, FIVE_POINT_CHOICES[len(FIVE_POINT_CHOICES)-i-1][1]] for i in range(len(FIVE_POINT_CHOICES))
]

class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def createpointques(choices, label):
    return models.IntegerField(
        label=label,
        choices=choices,
        widget=widgets.RadioSelect)

class Player(BasePlayer):
    is_religious = models.BooleanField(
        label='Do you identify with a religion and/or spiritual group?',
        blank=True
    )
    religion = models.StringField(
        label='If yes, then what religion/spiritual group?',
        blank=True
    )

    question = createpointques(NINE_POINT_CHOICES,
        'I am constantly questioning my religious beliefs.')
    viewchange = createpointques(NINE_POINT_CHOICES,
        'There are many religious issues on which my views are still changing.')
    growchange = createpointques(NINE_POINT_CHOICES,
        'As I grow and change I expect my religion also to grow and change.')
    approachlife = createpointques(NINE_POINT_CHOICES,
        'My religious beliefs are what really lie behind my whole approach to life.')
    carryover = createpointques(NINE_POINT_CHOICES,
        'I try hard to carry my religion over into all my other dealings in life. ')
    meditation = createpointques(NINE_POINT_CHOICES,
        'It is important for me to spend periods of time in private thought and meditation.')
    prayrelief = createpointques(NINE_POINT_CHOICES,
        'The purpose of prayer is to gain relief and protection.')
    comfort = createpointques(NINE_POINT_CHOICES,
        'What religion offers me most is comfort when sorrows and misfortune strike.')
    prayhappy = createpointques(NINE_POINT_CHOICES,
        'The purpose of prayer is to secure a happy and peaceful life.')
    churchmake = createpointques(NINE_POINT_CHOICES,
        'I go to Church because it helps me to make friends.')
    churchtime = createpointques(NINE_POINT_CHOICES,
        'I go to Church mostly to spend time with my friends.')
    churchsee = createpointques(NINE_POINT_CHOICES,
        'I go to church mainly because I enjoy seeing the people I know there.')
    godrevealall = createpointques(NINE_POINT_CHOICES,
        'Everything we need to know about living a moral life God has revealed to us.')
    onlygodreveal = createpointques(NINE_POINT_CHOICES,
        'The truth about morality is revealed only by God.')

    o_aesthetic = createpointques(FIVE_POINT_CHOICES,
        'I can look at a painting for a long time.')
    c_organization = createpointques(FIVE_POINT_CHOICES,
        'I make sure that things are in the right spot.')
    a_forgiveness = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I remain unfriendly to someone who was mean to me.')
    x_selfesteem = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'Nobody likes talking with me.')
    e_fear = createpointques(FIVE_POINT_CHOICES,
        'I am afraid of feeling pain.')
    h_sincerity = createpointques(FIVE_POINT_CHOICES,
        'I find it difficult to lie.')
    o_inquisitive = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I think science is boring.')
    c_diligence = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I postpone complicated tasks as long as possible.')
    a_gentleness = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I often express criticism.')
    x_boldness = createpointques(FIVE_POINT_CHOICES,
        'I easily approach strangers.')
    e_anxiety = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I worry less than others.')
    h_fair = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I would like to know how to make lots of money in a dishonest manner.')
    o_creativity = createpointques(FIVE_POINT_CHOICES,
        'I have a lot of imagination. ')
    c_perfectionism = createpointques(FIVE_POINT_CHOICES,
        'I work very precisely.')
    a_flexibility = createpointques(FIVE_POINT_CHOICES,
        'I tend to quickly agree with others.')
    x_sociability = createpointques(FIVE_POINT_CHOICES,
        'I like to talk with others.')
    e_dependence = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I can easily overcome difficulties on my own.')
    h_greed = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I want to be famous.')
    o_unconventional = createpointques(FIVE_POINT_CHOICES,
        'I like people with strange ideas.')
    c_prudence = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I often do things without really thinking.')
    a_patience = createpointques(FIVE_POINT_CHOICES,
        'Even when I’m treated badly, I remain calm.')
    x_liveliness = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I am seldom cheerful.')
    e_sentimentality = createpointques(FIVE_POINT_CHOICES,
        'I have to cry during sad or romantic movies.')
    h_modesty = createpointques(FIVE_POINT_CHOICES_REVERSED,
        'I am entitled to special treatment.')


# PAGES
class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['is_religious', 'religion']

    @staticmethod
    def error_message(player, values):
        if (values['is_religious'] == True) and \
            ((values['religion'] is None) or (values['religion'] == '')):
            return 'Please specify your religin/spiritual group'


class Questionnaire2(Page):
    form_model = 'player'

    @staticmethod
    def is_displayed(player):
        return player.field_maybe_none('is_religious') == True

    @staticmethod
    def get_form_fields(player):
        import random
        form_fields = ['question', 'viewchange', 'growchange', 'approachlife', 'carryover', 'meditation',
            'prayrelief', 'comfort', 'prayhappy', 'churchmake', 'churchtime', 'churchsee',
            'godrevealall', 'onlygodreveal']
        random.shuffle(form_fields)
        return form_fields



class Hexaco(Page):
    form_model = 'player'
    form_fields = [ 'o_aesthetic', 'c_organization', 'a_forgiveness', 'x_selfesteem', 'e_fear',
        'h_sincerity', 'o_inquisitive', 'c_diligence', 'a_gentleness', 'x_boldness', 'e_anxiety',
        'h_fair', 'o_creativity', 'c_perfectionism', 'a_flexibility', 'x_sociability',
        'e_dependence', 'h_greed', 'o_unconventional', 'c_prudence', 'a_patience', 'x_liveliness',
        'e_sentimentality', 'h_modesty' ]


page_sequence = [Questionnaire, Questionnaire2, Hexaco]
