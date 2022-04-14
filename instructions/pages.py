from ._builtin import Page

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
