from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 0.02,
    'participation_fee': 500*0.02,
    'doc': "",
}

SESSION_CONFIGS = [
    {
        'name': 'all',
        'display_name': "All",
        'num_demo_participants': 4,
        'app_sequence': [
            'instructions',
            'rfas',
            'questionnaire',
            'demographics',
            'debriefing',
            'payment_info'
        ],
        'endowment_selection': 450,
        'endowment_stage3': 500,
        'selection_fee': 150,
        'pt1_endowment_yellow': 15,
        'pt1_endowment_blue': 5,
        'pt2_endowment_yellow': 15,
        'pt2_endowment_blue': 15,
    },
    {
        'name': 'instructions',
        'display_name': "Instructions",
        'num_demo_participants': 1,
        'app_sequence': ['instructions'],
    },
    {
        'name': 'rfas',
        'display_name': "Rule Following As Signal",
        'num_demo_participants': 4,
        'app_sequence': ['rfas'],
        'endowment_selection': 450,
        'endowment_stage3': 500,
        'selection_fee': 150,
        'pt1_endowment_yellow': 15,
        'pt1_endowment_blue': 5,
        'pt2_endowment_yellow': 15,
        'pt2_endowment_blue': 15,
    },
    {
        'name': 'questionnaire',
        'display_name': "Questionnaire",
        'num_demo_participants': 1,
        'app_sequence': ['questionnaire'],
    },
    {
        'name': 'demographics',
        'display_name': "Demographic Questions",
        'num_demo_participants': 1,
        'app_sequence': ['demographics'],
    },
    {
        'name': 'debriefing',
        'display_name': "Debriefing",
        'num_demo_participants': 1,
        'app_sequence': ['debriefing'],
    },
    # {
    #     'name': 'payment_info',
    #     'display_name': "Payment Info",
    #     'num_demo_participants': 1,
    #     'app_sequence': ['payment_info'],
    # },
]
# see the end of this file for the inactive session configs

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'AUD'
USE_POINTS = True
POINTS_DECIMAL_PLACES = 0
POINTS_CUSTOM_NAME = 'points'

ROOMS = [
    {
        'name': 'econ101',
        'display_name': 'Econ 101 class',
        'participant_label_file': '_rooms/econ101.txt',
    },
    {
        'name': 'live_demo',
        'display_name': 'Room for live demo (no participant labels)',
    },
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are various games implemented with 
oTree. These games are open
source, and you can modify them as you wish.
"""

# don't share this with anybody.
SECRET_KEY = 'wr=f)ewj**tq@66!+9&l&k&8#dho8rawspxz3osiudb*-ldy_b'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# inactive session configs
###{
###    'name': 'dictator',
###    'display_name': "Dictator Game",
###    'num_demo_participants': 2,
###    'app_sequence': ['dictator'],
###},
###{
###    'name': 'survey',
###    'num_demo_participants': 1,
###    'app_sequence': ['survey', 'payment_info'],
###},
###{
###    'name': 'quiz',
###    'num_demo_participants': 1,
###    'app_sequence': ['quiz'],
###},
### {
###     'name': 'trust',
###     'display_name': "Trust Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust', 'payment_info'],
### },
###{
###    'name': 'public_goods',
###    'display_name': "Public Goods",
###    'num_demo_participants': 3,
###    'app_sequence': ['public_goods', 'payment_info'],
###},
###{
###    'name': 'trust_simple',
###    'display_name': "Trust Game (simple version from tutorial)",
###    'num_demo_participants': 2,
###    'app_sequence': ['trust_simple'],
###},
###{
###    'name': 'trust',
###    'display_name': "Trust Game",
###    'num_demo_participants': 2,
###    'app_sequence': ['trust', 'payment_info'],
###},
###{
###    'name': 'guess_two_thirds',
###    'display_name': "Guess 2/3 of the Average",
###    'num_demo_participants': 3,
###    'app_sequence': ['guess_two_thirds', 'payment_info'],
###},
### {
###     'name': 'prisoner',
###     'display_name': "Prisoner's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['prisoner', 'payment_info'],
### },
### {
###     'name': 'ultimatum',
###     'display_name': "Ultimatum (randomized: strategy vs. direct response)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
### },
### {
###     'name': 'ultimatum_strategy',
###     'display_name': "Ultimatum (strategy method treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': True,
### },
### {
###     'name': 'ultimatum_non_strategy',
###     'display_name': "Ultimatum (direct response treatment)",
###     'num_demo_participants': 2,
###     'app_sequence': ['ultimatum', 'payment_info'],
###     'use_strategy_method': False,
### },
### {
###     'name': 'vickrey_auction',
###     'display_name': "Vickrey Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['vickrey_auction', 'payment_info'],
### },
### {
###     'name': 'volunteer_dilemma',
###     'display_name': "Volunteer's Dilemma",
###     'num_demo_participants': 3,
###     'app_sequence': ['volunteer_dilemma', 'payment_info'],
### },
### {
###     'name': 'cournot',
###     'display_name': "Cournot Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'cournot', 'payment_info'
###     ],
### },
### {
###     'name': 'principal_agent',
###     'display_name': "Principal Agent",
###     'num_demo_participants': 2,
###     'app_sequence': ['principal_agent', 'payment_info'],
### },
### {
###     'name': 'dictator',
###     'display_name': "Dictator Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['dictator', 'payment_info'],
### },
### {
###     'name': 'matching_pennies',
###     'display_name': "Matching Pennies",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'matching_pennies',
###     ],
### },
### {
###     'name': 'traveler_dilemma',
###     'display_name': "Traveler's Dilemma",
###     'num_demo_participants': 2,
###     'app_sequence': ['traveler_dilemma', 'payment_info'],
### },
### {
###     'name': 'bargaining',
###     'display_name': "Bargaining Game",
###     'num_demo_participants': 2,
###     'app_sequence': ['bargaining', 'payment_info'],
### },
### {
###     'name': 'common_value_auction',
###     'display_name': "Common Value Auction",
###     'num_demo_participants': 3,
###     'app_sequence': ['common_value_auction', 'payment_info'],
### },
### {
###     'name': 'bertrand',
###     'display_name': "Bertrand Competition",
###     'num_demo_participants': 2,
###     'app_sequence': [
###         'bertrand', 'payment_info'
###     ],
### },
### {
###     'name': 'real_effort',
###     'display_name': "Real-effort transcription task",
###     'num_demo_participants': 1,
###     'app_sequence': [
###         'real_effort',
###     ],
### },
### {
###     'name': 'lemon_market',
###     'display_name': "Lemon Market Game",
###     'num_demo_participants': 3,
###     'app_sequence': [
###         'lemon_market', 'payment_info'
###     ],
### },
### {
###     'name': 'public_goods_simple',
###     'display_name': "Public Goods (simple version from tutorial)",
###     'num_demo_participants': 3,
###     'app_sequence': ['public_goods_simple', 'payment_info'],
### },
### {
###     'name': 'trust_simple',
###     'display_name': "Trust Game (simple version from tutorial)",
###     'num_demo_participants': 2,
###     'app_sequence': ['trust_simple'],
### },
