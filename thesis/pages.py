from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import random
import time


class Round(Page):

    timeout_seconds = 1

    def before_next_page(self):
        self.player.yellow_choice101 = 0
        self.player.yellow_choice102 = 0
        self.player.yellow_choice103 = 0
        self.player.yellow_choice104 = 0
        self.player.yellow_choice105 = 0
        self.player.yellow_choice106 = 0
        self.player.yellow_choice107 = 0
        self.player.yellow_choice108 = 0
        self.player.yellow_choice109 = 0
        self.player.yellow_choice110 = 0
        self.player.yellow_choice111 = 0
        self.player.yellow_choice112 = 0
        self.player.yellow_choice113 = 0
        self.player.yellow_choice114 = 0
        self.player.yellow_choice115 = 0

        self.player.yellow_choice201 = 0
        self.player.yellow_choice202 = 0
        self.player.yellow_choice203 = 0
        self.player.yellow_choice204 = 0
        self.player.yellow_choice205 = 0
        self.player.yellow_choice206 = 0
        self.player.yellow_choice207 = 0
        self.player.yellow_choice208 = 0
        self.player.yellow_choice209 = 0
        self.player.yellow_choice210 = 0
        self.player.yellow_choice211 = 0
        self.player.yellow_choice212 = 0
        self.player.yellow_choice213 = 0
        self.player.yellow_choice214 = 0
        self.player.yellow_choice215 = 0

        self.player.yellow_choice301 = 0
        self.player.yellow_choice302 = 0
        self.player.yellow_choice303 = 0
        self.player.yellow_choice304 = 0
        self.player.yellow_choice305 = 0
        self.player.yellow_choice306 = 0
        self.player.yellow_choice307 = 0
        self.player.yellow_choice308 = 0
        self.player.yellow_choice309 = 0
        self.player.yellow_choice310 = 0
        self.player.yellow_choice311 = 0
        self.player.yellow_choice312 = 0
        self.player.yellow_choice313 = 0
        self.player.yellow_choice314 = 0
        self.player.yellow_choice315 = 0

        self.player.blue_choice101 = 0
        self.player.blue_choice102 = 0
        self.player.blue_choice103 = 0
        self.player.blue_choice104 = 0
        self.player.blue_choice105 = 0
        self.player.blue_choice106 = 0
        self.player.blue_choice107 = 0
        self.player.blue_choice108 = 0
        self.player.blue_choice109 = 0
        self.player.blue_choice110 = 0
        self.player.blue_choice111 = 0
        self.player.blue_choice112 = 0
        self.player.blue_choice113 = 0
        self.player.blue_choice114 = 0
        self.player.blue_choice115 = 0

        self.player.blue_choice201 = 0
        self.player.blue_choice202 = 0
        self.player.blue_choice203 = 0
        self.player.blue_choice204 = 0
        self.player.blue_choice205 = 0
        self.player.blue_choice206 = 0
        self.player.blue_choice207 = 0
        self.player.blue_choice208 = 0
        self.player.blue_choice209 = 0
        self.player.blue_choice210 = 0
        self.player.blue_choice211 = 0
        self.player.blue_choice212 = 0
        self.player.blue_choice213 = 0
        self.player.blue_choice214 = 0
        self.player.blue_choice215 = 0

        self.player.blue_choice301 = 0
        self.player.blue_choice302 = 0
        self.player.blue_choice303 = 0
        self.player.blue_choice304 = 0
        self.player.blue_choice305 = 0
        self.player.blue_choice306 = 0
        self.player.blue_choice307 = 0
        self.player.blue_choice308 = 0
        self.player.blue_choice309 = 0
        self.player.blue_choice310 = 0
        self.player.blue_choice311 = 0
        self.player.blue_choice312 = 0
        self.player.blue_choice313 = 0
        self.player.blue_choice314 = 0
        self.player.blue_choice315 = 0

        self.player.balls = 1


class Role(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class EnvironmentPage1(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class EnvironmentPage2(Page):

    form_model = 'player'
    form_fields = ['understood31',
                   'understood32',
                   'understood33',
                   'understood34',
                   'comprehension7',
                   'comprehension8']

    def is_displayed(self):
        return self.subsession.round_number == (Constants.num_rounds/2)+1

    def error_message(self, values):
        if values['comprehension7'] != 1 or values['comprehension8'] != 3:
            return 'At least one answer is wrong. Please try again.'


class EnvironmentPage3(Page):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'money_earned': self.participant.payoff.to_real_world_currency(self.session)
        }


class FeedbackDeciders(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'

    def vars_for_template(self):
        dictator1 = self.group.dictator_choice11 if self.group.dictator_choice11 is not None else 0
        dictator2 = self.group.dictator_choice21 if self.group.dictator_choice21 is not None else 0
        dictator3 = self.group.dictator_choice31 if self.group.dictator_choice31 is not None else 0
        dictator41 = self.group.dictator_choice12 if self.group.dictator_choice12 is not None else 0
        dictator42 = self.group.dictator_choice22 if self.group.dictator_choice22 is not None else 0
        dictator43 = self.group.dictator_choice32 if self.group.dictator_choice32 is not None else 0
        dictator4 = dictator41 + dictator42 + dictator43
        dieroll1 = Constants.dieroll_points[self.group.die_roll1-1] if self.group.die_roll1 is not None else 0
        dieroll2 = Constants.dieroll_points[self.group.die_roll2-1] if self.group.die_roll2 is not None else 0
        dieroll3 = Constants.dieroll_points[self.group.die_roll3-1] if self.group.die_roll3 is not None else 0
        dieroll4 = dieroll1 + dieroll2 + dieroll3
        select1 = 1 if self.group.select1 else 0
        select2 = 1 if self.group.select2 else 0
        select3 = 1 if self.group.select3 else 0
        select_num = select1 + select2 + select3
        points_total1 = self.group.payoff_rf1 + dictator1 \
            if self.subsession.round_number <= Constants.num_rounds/2 \
            else self.group.payoff_rf1 + dieroll1
        points_total2 = self.group.payoff_rf2 + dictator2 \
            if self.subsession.round_number <= Constants.num_rounds/2 \
            else self.group.payoff_rf2 + dieroll2
        points_total3 = self.group.payoff_rf3 + dictator3 \
            if self.subsession.round_number <= Constants.num_rounds/2 \
            else self.group.payoff_rf3 + dieroll3
        points_total4 = (Constants.endowment_selection * select_num) - (Constants.selection_fee * select_num) + dictator4 \
            if self.subsession.round_number <= Constants.num_rounds/2 \
            else (Constants.endowment_selection * select_num) - (Constants.selection_fee * select_num) + dieroll4
        return {
            'points_total1': points_total1,
            'points_total2': points_total2,
            'points_total3': points_total3,
            'points_total4': points_total4
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class PayoffsWaitPage(WaitPage):

    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        self.group.set_payoffs()


########################################
# STAGE 1: RULE-FOLLOWING
########################################
class RFTask2(Page):

    def is_displayed(self):
        return self.player.role() == 'selector'


class RFTask(Page):
    form_model = 'player'
    form_fields = ['yellow_choice101',
                   'yellow_choice201',
                   'yellow_choice301',
                   'blue_choice101',
                   'blue_choice201',
                   'blue_choice301']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice101
        self.group.yellow_counter2 += self.player.yellow_choice201
        self.group.yellow_counter3 += self.player.yellow_choice301

        self.group.blue_counter1 += self.player.blue_choice101
        self.group.blue_counter2 += self.player.blue_choice201
        self.group.blue_counter3 += self.player.blue_choice301

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice101 \
            + Constants.endowment_blue*self.player.blue_choice101
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice201 \
            + Constants.endowment_blue*self.player.blue_choice201
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice301 \
            + Constants.endowment_blue*self.player.blue_choice301

        self.player.balls += 1 if self.player.balls != 15 else 0


class RFTask21(Page):
    form_model = 'player'
    form_fields = ['yellow_choice102',
                   'yellow_choice202',
                   'yellow_choice302',
                   'blue_choice102',
                   'blue_choice202',
                   'blue_choice302']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice102
        self.group.yellow_counter2 += self.player.yellow_choice202
        self.group.yellow_counter3 += self.player.yellow_choice302

        self.group.blue_counter1 += self.player.blue_choice102
        self.group.blue_counter2 += self.player.blue_choice202
        self.group.blue_counter3 += self.player.blue_choice302

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice102 \
            + Constants.endowment_blue*self.player.blue_choice102
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice202 \
            + Constants.endowment_blue*self.player.blue_choice202
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice302 \
            + Constants.endowment_blue*self.player.blue_choice302

        self.player.balls += 1


class RFTask3(Page):
    form_model = 'player'
    form_fields = ['yellow_choice103',
                   'yellow_choice203',
                   'yellow_choice303',
                   'blue_choice103',
                   'blue_choice203',
                   'blue_choice303']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice103
        self.group.yellow_counter2 += self.player.yellow_choice203
        self.group.yellow_counter3 += self.player.yellow_choice303

        self.group.blue_counter1 += self.player.blue_choice103
        self.group.blue_counter2 += self.player.blue_choice203
        self.group.blue_counter3 += self.player.blue_choice303

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice103 \
            + Constants.endowment_blue*self.player.blue_choice103
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice203 \
            + Constants.endowment_blue*self.player.blue_choice203
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice303 \
            + Constants.endowment_blue*self.player.blue_choice303

        self.player.balls += 1


class RFTask4(Page):
    form_model = 'player'
    form_fields = ['yellow_choice104',
                   'yellow_choice204',
                   'yellow_choice304',
                   'blue_choice104',
                   'blue_choice204',
                   'blue_choice304']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice104
        self.group.yellow_counter2 += self.player.yellow_choice204
        self.group.yellow_counter3 += self.player.yellow_choice304

        self.group.blue_counter1 += self.player.blue_choice104
        self.group.blue_counter2 += self.player.blue_choice204
        self.group.blue_counter3 += self.player.blue_choice304

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice104 \
            + Constants.endowment_blue*self.player.blue_choice104
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice204 \
            + Constants.endowment_blue*self.player.blue_choice204
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice304 \
            + Constants.endowment_blue*self.player.blue_choice304

        self.player.balls += 1


class RFTask5(Page):
    form_model = 'player'
    form_fields = ['yellow_choice105',
                   'yellow_choice205',
                   'yellow_choice305',
                   'blue_choice105',
                   'blue_choice205',
                   'blue_choice305']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice105
        self.group.yellow_counter2 += self.player.yellow_choice205
        self.group.yellow_counter3 += self.player.yellow_choice305

        self.group.blue_counter1 += self.player.blue_choice105
        self.group.blue_counter2 += self.player.blue_choice205
        self.group.blue_counter3 += self.player.blue_choice305

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice105 \
            + Constants.endowment_blue*self.player.blue_choice105
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice205 \
            + Constants.endowment_blue*self.player.blue_choice205
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice305 \
            + Constants.endowment_blue*self.player.blue_choice305

        self.player.balls += 1


class RFTask6(Page):
    form_model = 'player'
    form_fields = ['yellow_choice106',
                   'yellow_choice206',
                   'yellow_choice306',
                   'blue_choice106',
                   'blue_choice206',
                   'blue_choice306']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice106
        self.group.yellow_counter2 += self.player.yellow_choice206
        self.group.yellow_counter3 += self.player.yellow_choice306

        self.group.blue_counter1 += self.player.blue_choice106
        self.group.blue_counter2 += self.player.blue_choice206
        self.group.blue_counter3 += self.player.blue_choice306

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice106 \
            + Constants.endowment_blue*self.player.blue_choice106
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice206 \
            + Constants.endowment_blue*self.player.blue_choice206
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice306 \
            + Constants.endowment_blue*self.player.blue_choice306

        self.player.balls += 1


class RFTask7(Page):
    form_model = 'player'
    form_fields = ['yellow_choice107',
                   'yellow_choice207',
                   'yellow_choice307',
                   'blue_choice107',
                   'blue_choice207',
                   'blue_choice307']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice107
        self.group.yellow_counter2 += self.player.yellow_choice207
        self.group.yellow_counter3 += self.player.yellow_choice307

        self.group.blue_counter1 += self.player.blue_choice107
        self.group.blue_counter2 += self.player.blue_choice207
        self.group.blue_counter3 += self.player.blue_choice307

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice107 \
            + Constants.endowment_blue*self.player.blue_choice107
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice207 \
            + Constants.endowment_blue*self.player.blue_choice207
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice307 \
            + Constants.endowment_blue*self.player.blue_choice307

        self.player.balls += 1


class RFTask8(Page):
    form_model = 'player'
    form_fields = ['yellow_choice108',
                   'yellow_choice208',
                   'yellow_choice308',
                   'blue_choice108',
                   'blue_choice208',
                   'blue_choice308']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice108
        self.group.yellow_counter2 += self.player.yellow_choice208
        self.group.yellow_counter3 += self.player.yellow_choice308

        self.group.blue_counter1 += self.player.blue_choice108
        self.group.blue_counter2 += self.player.blue_choice208
        self.group.blue_counter3 += self.player.blue_choice308

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice108 \
            + Constants.endowment_blue*self.player.blue_choice108
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice208 \
            + Constants.endowment_blue*self.player.blue_choice208
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice308 \
            + Constants.endowment_blue*self.player.blue_choice308

        self.player.balls += 1


class RFTask9(Page):
    form_model = 'player'
    form_fields = ['yellow_choice109',
                   'yellow_choice209',
                   'yellow_choice309',
                   'blue_choice109',
                   'blue_choice209',
                   'blue_choice309']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice109
        self.group.yellow_counter2 += self.player.yellow_choice209
        self.group.yellow_counter3 += self.player.yellow_choice309

        self.group.blue_counter1 += self.player.blue_choice109
        self.group.blue_counter2 += self.player.blue_choice209
        self.group.blue_counter3 += self.player.blue_choice309

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice109 \
            + Constants.endowment_blue*self.player.blue_choice109
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice209 \
            + Constants.endowment_blue*self.player.blue_choice209
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice309 \
            + Constants.endowment_blue*self.player.blue_choice309

        self.player.balls += 1


class RFTask10(Page):
    form_model = 'player'
    form_fields = ['yellow_choice110',
                   'yellow_choice210',
                   'yellow_choice310',
                   'blue_choice110',
                   'blue_choice210',
                   'blue_choice310']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice110
        self.group.yellow_counter2 += self.player.yellow_choice210
        self.group.yellow_counter3 += self.player.yellow_choice310

        self.group.blue_counter1 += self.player.blue_choice110
        self.group.blue_counter2 += self.player.blue_choice210
        self.group.blue_counter3 += self.player.blue_choice310

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice110 \
            + Constants.endowment_blue*self.player.blue_choice110
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice210 \
            + Constants.endowment_blue*self.player.blue_choice210
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice310 \
            + Constants.endowment_blue*self.player.blue_choice310

        self.player.balls += 1


class RFTask11(Page):
    form_model = 'player'
    form_fields = ['yellow_choice111',
                   'yellow_choice211',
                   'yellow_choice311',
                   'blue_choice111',
                   'blue_choice211',
                   'blue_choice311']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice111
        self.group.yellow_counter2 += self.player.yellow_choice211
        self.group.yellow_counter3 += self.player.yellow_choice311

        self.group.blue_counter1 += self.player.blue_choice111
        self.group.blue_counter2 += self.player.blue_choice211
        self.group.blue_counter3 += self.player.blue_choice311

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice111 \
            + Constants.endowment_blue*self.player.blue_choice111
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice211 \
            + Constants.endowment_blue*self.player.blue_choice211
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice311 \
            + Constants.endowment_blue*self.player.blue_choice311

        self.player.balls += 1


class RFTask12(Page):
    form_model = 'player'
    form_fields = ['yellow_choice112',
                   'yellow_choice212',
                   'yellow_choice312',
                   'blue_choice112',
                   'blue_choice212',
                   'blue_choice312']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice112
        self.group.yellow_counter2 += self.player.yellow_choice212
        self.group.yellow_counter3 += self.player.yellow_choice312

        self.group.blue_counter1 += self.player.blue_choice112
        self.group.blue_counter2 += self.player.blue_choice212
        self.group.blue_counter3 += self.player.blue_choice312

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice112 \
            + Constants.endowment_blue*self.player.blue_choice112
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice212 \
            + Constants.endowment_blue*self.player.blue_choice212
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice312 \
            + Constants.endowment_blue*self.player.blue_choice312

        self.player.balls += 1


class RFTask13(Page):
    form_model = 'player'
    form_fields = ['yellow_choice113',
                   'yellow_choice213',
                   'yellow_choice313',
                   'blue_choice113',
                   'blue_choice213',
                   'blue_choice313']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice113
        self.group.yellow_counter2 += self.player.yellow_choice213
        self.group.yellow_counter3 += self.player.yellow_choice313

        self.group.blue_counter1 += self.player.blue_choice113
        self.group.blue_counter2 += self.player.blue_choice213
        self.group.blue_counter3 += self.player.blue_choice313

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice113 \
            + Constants.endowment_blue*self.player.blue_choice113
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice213 \
            + Constants.endowment_blue*self.player.blue_choice213
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice313 \
            + Constants.endowment_blue*self.player.blue_choice313

        self.player.balls += 1


class RFTask14(Page):
    form_model = 'player'
    form_fields = ['yellow_choice114',
                   'yellow_choice214',
                   'yellow_choice314',
                   'blue_choice114',
                   'blue_choice214',
                   'blue_choice314']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice114
        self.group.yellow_counter2 += self.player.yellow_choice214
        self.group.yellow_counter3 += self.player.yellow_choice314

        self.group.blue_counter1 += self.player.blue_choice114
        self.group.blue_counter2 += self.player.blue_choice214
        self.group.blue_counter3 += self.player.blue_choice314

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice114 \
            + Constants.endowment_blue*self.player.blue_choice114
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice214 \
            + Constants.endowment_blue*self.player.blue_choice214
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice314 \
            + Constants.endowment_blue*self.player.blue_choice314

        self.player.balls += 1


class RFTask15(Page):
    form_model = 'player'
    form_fields = ['yellow_choice115',
                   'yellow_choice215',
                   'yellow_choice315',
                   'blue_choice115',
                   'blue_choice215',
                   'blue_choice315']

    def is_displayed(self):
        return self.player.role() == 'partner'

    def before_next_page(self):
        self.group.yellow_counter1 += self.player.yellow_choice115
        self.group.yellow_counter2 += self.player.yellow_choice215
        self.group.yellow_counter3 += self.player.yellow_choice315

        self.group.blue_counter1 += self.player.blue_choice115
        self.group.blue_counter2 += self.player.blue_choice215
        self.group.blue_counter3 += self.player.blue_choice315

        self.group.payoff_rf1 += Constants.endowment_yellow*self.player.yellow_choice115 \
            + Constants.endowment_blue*self.player.blue_choice115
        self.group.payoff_rf2 += Constants.endowment_yellow*self.player.yellow_choice215 \
            + Constants.endowment_blue*self.player.blue_choice215
        self.group.payoff_rf3 += Constants.endowment_yellow*self.player.yellow_choice315 \
            + Constants.endowment_blue*self.player.blue_choice315

        self.player.balls += 1


class RFResults1(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'

    def vars_for_template(self):
        counter_tuples = [
            [int(self.group.blue_counter1), str(self.group.select1), 1],
            [int(self.group.blue_counter2), str(self.group.select2), 2],
            [int(self.group.blue_counter3), str(self.group.select3), 3],
        ]
        sorted_counter = sorted(counter_tuples, key=lambda counter: counter[0])
        self.group.decider_highest = sorted_counter[2][2]
        self.group.partner_middle = sorted_counter [1][2]
        self.group.partner_lowest = sorted_counter [0][2]
        return {
            'lowest_counter': 'You chose the blue bucket ' + str(sorted_counter[0][0]) + ' times and were ' if self.player.id_in_group == sorted_counter[0][2] else 'Another decider chose the blue bucket ' + str(sorted_counter[0][0]) + ' times and was ',
            'lowest_select': sorted_counter[0][1],
            'middle_counter': 'You chose the blue bucket ' + str(sorted_counter[1][0]) + ' times and were ' if self.player.id_in_group == sorted_counter[1][2] else 'Another decider chose the blue bucket ' + str(sorted_counter[1][0]) + ' times and was ',
            'middle_select': sorted_counter[1][1],
            'highest_counter': 'You chose the blue bucket ' + str(sorted_counter[2][0]) + ' times and were ' if self.player.id_in_group == sorted_counter[2][2] else 'Another decider chose the blue bucket ' + str(sorted_counter[2][0]) + ' times and was ',
            'highest_select': sorted_counter[2][1],
        }


class RFResults21(Page):

    def is_displayed(self):
        return self.player.role() == 'partner'


########################################
# STAGE 2: SELECTION TASK
########################################
class RFResults2(Page):

    form_model = 'group'
    form_fields = ['select1',
                   'select2',
                   'select3']

    def is_displayed(self):
        return self.player.role() == 'selector'

    def vars_for_template(self):
        counter_tuples = [
            [int(self.group.blue_counter1), self.group.payoff_rf1, self.form_fields[0], 1],
            [int(self.group.blue_counter2), self.group.payoff_rf2, self.form_fields[1], 2],
            [int(self.group.blue_counter3), self.group.payoff_rf3, self.form_fields[2], 3],
        ]
        sorted_counter = sorted(counter_tuples, key=lambda counter: counter[0])
        self.group.partner_highest = sorted_counter[2][3]
        self.group.partner_middle = sorted_counter [1][3]
        self.group.partner_lowest = sorted_counter [0][3]
        return {
            'lowest_counter': sorted_counter[0][0],
            'lowest_payoff': sorted_counter[0][1],
            'lowest_select': sorted_counter[0][2],
            'middle_counter': sorted_counter[1][0],
            'middle_payoff': sorted_counter[1][1],
            'middle_select': sorted_counter[1][2],
            'highest_counter': sorted_counter[2][0],
            'highest_payoff': sorted_counter[2][1],
            'highest_select': sorted_counter[2][2],
        }

    def error_message(self, values):
        print('values is', values)
        if values["select1"] is not True and values["select2"] is not True and values["select3"] is not True:
            return 'Select at least one partner.'


class StageThreeSelector(Page):
    def is_displayed(self):
        return self.player.role() == 'selector'


########################################
# STAGE 3.A: DICTATOR TASK
########################################
class DictatorTask1(Page):
    form_model = 'group'
    form_fields = ['dictator_choice11',
                   'dictator_choice12']

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == 1 \
               and self.group.select1 is True

    def error_message(self, values):
        print('values is', values)
        if values['dictator_choice11'] + values['dictator_choice12'] != Constants.endowment_stage_three:
            return 'The points have to add up to ' + str(Constants.endowment_stage_three)


class DictatorTask2(Page):
    form_model = 'group'
    form_fields = ['dictator_choice21',
                   'dictator_choice22']

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == 2 \
               and self.group.select2 is True

    def error_message(self, values):
        print('values is', values)
        if values['dictator_choice21'] + values['dictator_choice22'] != Constants.endowment_stage_three:
            return 'The points have to add up to ' + str(Constants.endowment_stage_three)


class DictatorTask3(Page):
    form_model = 'group'
    form_fields = ['dictator_choice31',
                   'dictator_choice32']

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == 3 \
               and self.group.select3 is True

    def error_message(self, values):
        print('values is', values)
        if values['dictator_choice31'] + values['dictator_choice32'] != Constants.endowment_stage_three:
            return 'The points have to add up to ' + str(Constants.endowment_stage_three)


class DictatorResults(Page):

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.role() == 'selector'

    def vars_for_template(self):
        earning1 = self.group.dictator_choice12 - Constants.selection_fee if self.group.select1 \
            is True else 0
        earning2 = self.group.dictator_choice22 - Constants.selection_fee if self.group.select2 \
            is True else 0
        earning3 = self.group.dictator_choice32 - Constants.selection_fee if self.group.select3 \
            is True else 0
        earning_total = Constants.endowment_selection + earning1 + earning2 + earning3
        selected1 = 1 if self.group.select1 else 0
        selected2 = 1 if self.group.select2 else 0
        selected3 = 1 if self.group.select3 else 0
        selected_num = selected1 + selected2 + selected3
        dictator1 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter1) + \
            ' times decided to keep ' + str(self.group.dictator_choice11) + ' and give ' \
            + str(self.group.dictator_choice12) + ' to you. Therefore, you earned ' + \
            str(earning1) + ' for this interaction.' if self.group.select1 is True else ''
        dictator2 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter2) + \
            ' times decided  to keep ' + str(self.group.dictator_choice21) + ' and give ' \
            + str(self.group.dictator_choice22) + ' to you. Therefore, you earned ' + \
            str(earning2) + ' for this interaction.' if self.group.select2 is True else ''
        dictator3 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter3) + \
            ' times decided  to keep ' + str(self.group.dictator_choice31) + ' and give ' \
            + str(self.group.dictator_choice32) + ' to you. Therefore, you earned ' + \
            str(earning3) + ' for this interaction.' if self.group.select3 is True else ''

        dictator_tuples = [
            [int(self.group.blue_counter1), str(dictator1), 1],
            [int(self.group.blue_counter2), str(dictator2), 2],
            [int(self.group.blue_counter3), str(dictator3), 3],
        ]
        sorted_dictator = sorted(dictator_tuples, key=lambda dictator: dictator[0])
        return {
            'lowest_counter': sorted_dictator[0][1],
            'middle_counter': sorted_dictator[1][1],
            'highest_counter': sorted_dictator[2][1],
            'earning1': earning1,
            'earning2': earning2,
            'earning3': earning3,
            'earning_total': earning_total,
            'selected_num': selected_num
        }


class DictatorResults1(Page):

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == 1 and self.group.select1 is True


class DictatorResults2(Page):

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == 2 and self.group.select2 is True


class DictatorResults3(Page):

    def is_displayed(self):
        return self.round_number <= Constants.num_rounds/2 and self.player.id_in_group == 3 and self.group.select3 is True


########################################
# STAGE 3.B: DIE ROLL TASK
########################################

class DieRollTaskEnd11(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 1


class DieRollTaskEnd12(Page):

    form_model = 'group'
    form_fields = ['dieroll_end1']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 1


class DieRollTaskEnd21(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 2


class DieRollTaskEnd22(Page):

    form_model = 'group'
    form_fields = ['dieroll_end2']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 2


class DieRollTaskEnd31(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 3


class DieRollTaskEnd32(Page):

    form_model = 'group'
    form_fields = ['dieroll_end3']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 3


class DieRollTaskEnd41(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 4


class DieRollTaskEnd42(Page):

    form_model = 'group'
    form_fields = ['dieroll_end4']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds and self.player.id_in_group == 4


class DieRollTask11(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 1 and self.group.select1 is True


class DieRollTask21(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 2 and self.group.select2 is True


class DieRollTask31(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 3 and self.group.select3 is True


class DieRollTask12(Page):
    form_model = 'group'
    form_fields = ['die_roll1']

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 1 \
               and self.group.select1 is True


class DieRollTask22(Page):
    form_model = 'group'
    form_fields = ['die_roll2']

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 2 \
               and self.group.select2 is True


class DieRollTask32(Page):
    form_model = 'group'
    form_fields = ['die_roll3']

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 3 \
               and self.group.select3 is True


class DieRollResults1(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 1 \
               and self.group.select1 is True

    def vars_for_template(self):
        points = 'So, both you and the selector earn ' + str(Constants.dieroll_points[self.group.die_roll1-1]) + '.' \
            if self.group.die_roll1 is not None else ''
        return {
            'points': points
        }


class DieRollResults2(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 2 \
               and self.group.select2 is True

    def vars_for_template(self):
        points = 'So, both you and the selector earn ' + str(Constants.dieroll_points[self.group.die_roll2-1]) + '.' \
            if self.group.die_roll2 is not None else ''
        return {
            'points': points
        }


class DieRollResults3(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 3 \
               and self.group.select3 is True

    def vars_for_template(self):
        points = 'So, both you and the selector earn ' + str(Constants.dieroll_points[self.group.die_roll3-1]) + '.' \
            if self.group.die_roll3 is not None else ''
        return {
            'points': points
        }


class DieRollResults4(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.role() == 'selector'

    def vars_for_template(self):
        die_roll1 = 'One decider rolled a ' + str(self.group.die_roll1) + '.' if self.group.die_roll1 is not None else ''
        die_roll2 = 'One decider rolled a ' + str(self.group.die_roll2) + '.' if self.group.die_roll2 is not None else ''
        die_roll3 = 'One decider rolled a ' + str(self.group.die_roll3) + '.' if self.group.die_roll3 is not None else ''
        selected1 = 1 if self.group.select1 else 0
        selected2 = 1 if self.group.select2 else 0
        selected3 = 1 if self.group.select3 else 0
        selected_num = selected1 + selected2 + selected3
        earning1 = Constants.dieroll_points[self.group.die_roll1-1] - Constants.selection_fee if self.group.select1 \
            is True else 0
        earning2 = Constants.dieroll_points[self.group.die_roll2-1] - Constants.selection_fee if self.group.select2 \
            is True else 0
        earning3 = Constants.dieroll_points[self.group.die_roll3-1] - Constants.selection_fee if self.group.select3 \
            is True else 0
        earning_total = Constants.endowment_selection + earning1 + earning2 + earning3
        points1 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter1) + \
                  ' times reported a ' + str(self.group.die_roll1) + '. So, you earn ' \
                  + str(earning1) + ' for this interaction.' if self.group.die_roll1 is not None else ''
        points2 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter2) + \
                  ' times reported a ' + str(self.group.die_roll2) + '. So, you earn ' \
                  + str(earning2) + ' for this interaction.' if self.group.die_roll2 is not None else ''
        points3 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter3) + \
                  ' times reported a ' + str(self.group.die_roll3) + '. So, you earn ' \
                  + str(earning3) + ' for this interaction.' if self.group.die_roll3 is not None else ''

        dieroll_tuples = [
            [int(self.group.blue_counter1), self.group.die_roll1, str(points1), 1],
            [int(self.group.blue_counter2), self.group.die_roll2, str(points2), 2],
            [int(self.group.blue_counter3), self.group.die_roll3, str(points3), 3],
        ]
        sorted_dieroll = sorted(dieroll_tuples, key=lambda dieroll: dieroll[0])
        return {
            'lowest_counter': sorted_dieroll[0][2],
            'middle_counter': sorted_dieroll[1][2],
            'highest_counter': sorted_dieroll[2][2],
            'die_roll1': die_roll1,
            'die_roll2': die_roll2,
            'die_roll3': die_roll3,
            'points1': points1,
            'points2': points2,
            'points3': points3,
            'earning_total': earning_total,
            'selected_num': selected_num,
        }


page_sequence = [
    EnvironmentPage1,
    Role,
    EnvironmentPage2,
    Round,
    RFTask2,
    RFTask,
    RFTask21,
    RFTask3,
    RFTask4,
    RFTask5,
    RFTask6,
    RFTask7,
    RFTask8,
    RFTask9,
    RFTask10,
    RFTask11,
    RFTask12,
    RFTask13,
    RFTask14,
    RFTask15,
    RFResults21,
    ResultsWaitPage,
    RFResults2,
    ResultsWaitPage,
    RFResults1,
    StageThreeSelector,
    DictatorTask1,
    DictatorTask2,
    DictatorTask3,
    DieRollTask11,
    DieRollTask21,
    DieRollTask31,
    DieRollTask12,
    DieRollTask22,
    DieRollTask32,
    ResultsWaitPage,
    DictatorResults,
    DictatorResults1,
    DictatorResults2,
    DictatorResults3,
    DieRollResults1,
    DieRollResults2,
    DieRollResults3,
    DieRollResults4,
    FeedbackDeciders,
    EnvironmentPage3,
    DieRollTaskEnd11,
    DieRollTaskEnd12,
    DieRollTaskEnd21,
    DieRollTaskEnd22,
    DieRollTaskEnd31,
    DieRollTaskEnd32,
    DieRollTaskEnd41,
    DieRollTaskEnd42,
    PayoffsWaitPage,
]
