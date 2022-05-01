import random

from . import *

class PlayerBot(Bot):

    def play_round(self):
        yield Hexaco, {
            'o_aesthetic': random.randint(1, 5), 
            'c_organization': random.randint(1, 5), 
            'a_forgiveness': random.randint(1, 5), 
            'x_selfesteem': random.randint(1, 5), 
            'e_fear': random.randint(1, 5),
            'h_sincerity': random.randint(1, 5), 
            'o_inquisitive': random.randint(1, 5), 
            'c_diligence': random.randint(1, 5), 
            'a_gentleness': random.randint(1, 5), 
            'x_boldness': random.randint(1, 5), 
            'e_anxiety': random.randint(1, 5),
            'h_fair': random.randint(1, 5), 
            'o_creativity': random.randint(1, 5), 
            'c_perfectionism': random.randint(1, 5), 
            'a_flexibility': random.randint(1, 5), 
            'x_sociability': random.randint(1, 5),
            'e_dependence': random.randint(1, 5), 
            'h_greed': random.randint(1, 5), 
            'o_unconventional': random.randint(1, 5), 
            'c_prudence': random.randint(1, 5), 
            'a_patience': random.randint(1, 5), 
            'x_liveliness': random.randint(1, 5),
            'e_sentimentality': random.randint(1, 5), 
            'h_modesty': random.randint(1, 5)
        }

        yield Questionnaire, {'is_religious': True, 'religion': 'blah'}

        yield Questionnaire2, {
            'question': random.randint(1, 9),
            'viewchange': random.randint(1, 9),
            'growchange': random.randint(1, 9),
            'approachlife': random.randint(1, 9),
            'carryover': random.randint(1, 9),
            'meditation': random.randint(1, 9),
            'prayrelief': random.randint(1, 9),
            'comfort': random.randint(1, 9),
            'prayhappy': random.randint(1, 9),
            'churchmake': random.randint(1, 9),
            'churchtime': random.randint(1, 9),
            'churchsee': random.randint(1, 9),
            'godrevealall': random.randint(1, 9),
            'onlygodreveal': random.randint(1, 9)
        }

