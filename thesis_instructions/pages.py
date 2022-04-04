from ._builtin import Page

UNDERSTOOD_QUESTIONS = ['understood1', 'understood11', 'understood12',
        'understood13', 'understood2', 'understood21', 'understood22', 'understood23',
        'understood24']

class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['consent']


class InformationBrochure(Page):
    form_model = 'player'
    form_fields = ['read']


class Instructions(Page):
    form_model = 'player'
    form_fields = UNDERSTOOD_QUESTIONS + ['comprehension1', 'comprehension2', 'comprehension3',
        'comprehension4', 'comprehension5', 'comprehension6']

    def error_message(self, values):
        for field_name in UNDERSTOOD_QUESTIONS:
            if values[field_name] is None:
                return 'Tick all the boxes in the subsections to show you read and understood the instructions.'

        solutions = dict(
            comprehension1=2,
            comprehension2=2,
            comprehension3=1,
            comprehension4=1,
            comprehension5=3,
            comprehension6=3
        )
            
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'This answer is wrong'
        
        return error_messages


page_sequence = [
    InformedConsent,
    InformationBrochure,
    Instructions,
]
