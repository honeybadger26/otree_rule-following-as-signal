# models.py
class Constants(BaseConstants):
    dieroll_instructions = 'thesis/InstructionsDieRoll.html'
    dieroll_instructions2 = 'thesis/InstructionsDieRoll2.html'
    dieroll_instructions_end = 'thesis/InstructionsDieRollEnd.html'
    dieroll_points = [c(0), c(50), c(100), c(150), c(200), c(250)]

class Group(BaseGroup):

    def make_die_roll_field():
        return models.IntegerField(
            min=1, max=6,
            label='',
            blank=True
        )

    die_roll1 = make_die_roll_field()
    die_roll2 = make_die_roll_field()
    die_roll3 = make_die_roll_field()

    dieroll_end1 = make_die_roll_field()
    dieroll_end2 = make_die_roll_field()
    dieroll_end3 = make_die_roll_field()
    dieroll_end4 = make_die_roll_field() 

# pages.py
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
        solutions = dict(
            comprehension7=1,
            comprehension8=3
        )
            
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'This answer is wrong'
        
        return error_messages

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
            if self.group.field_maybe_none('die_roll1') is not None else ''
        return {
            'points': points
        }


class DieRollResults2(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 2 \
               and self.group.select2 is True

    def vars_for_template(self):
        points = 'So, both you and the selector earn ' + str(Constants.dieroll_points[self.group.die_roll2-1]) + '.' \
            if self.group.field_maybe_none('die_roll2') is not None else ''
        return {
            'points': points
        }


class DieRollResults3(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.id_in_group == 3 \
               and self.group.select3 is True

    def vars_for_template(self):
        points = 'So, both you and the selector earn ' + str(Constants.dieroll_points[self.group.die_roll3-1]) + '.' \
            if self.group.field_maybe_none('die_roll3') is not None else ''
        return {
            'points': points
        }


class DieRollResults4(Page):

    def is_displayed(self):
        return self.round_number > Constants.num_rounds/2 and self.player.role() == 'selector'

    def vars_for_template(self):
        die_roll1 = 'One decider rolled a ' + str(self.group.die_roll1) + '.' if self.group.field_maybe_none('die_roll1') is not None else ''
        die_roll2 = 'One decider rolled a ' + str(self.group.die_roll2) + '.' if self.group.field_maybe_none('die_roll2') is not None else ''
        die_roll3 = 'One decider rolled a ' + str(self.group.die_roll3) + '.' if self.group.field_maybe_none('die_roll3') is not None else ''
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
                  + str(earning1) + ' for this interaction.' if self.group.field_maybe_none('die_roll1') is not None else ''
        points2 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter2) + \
                  ' times reported a ' + str(self.group.die_roll2) + '. So, you earn ' \
                  + str(earning2) + ' for this interaction.' if self.group.field_maybe_none('die_roll2') is not None else ''
        points3 = 'A decider who chose the blue bucket ' + str(self.group.blue_counter3) + \
                  ' times reported a ' + str(self.group.die_roll3) + '. So, you earn ' \
                  + str(earning3) + ' for this interaction.' if self.group.field_maybe_none('die_roll3') is not None else ''

        dieroll_tuples = [
            [int(self.group.blue_counter1), str(points1)],
            [int(self.group.blue_counter2), str(points2)],
            [int(self.group.blue_counter3), str(points3)],
        ]
        sorted_dieroll = sorted(dieroll_tuples, key=lambda d: d[0])
        return {
            'dieroll_results': [ x[1] for x in sorted_dieroll if x[1] is not None ],
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
    EnvironmentPage2,
    DieRollTask11,
    DieRollTask21,
    DieRollTask31,
    DieRollTask12,
    DieRollTask22,
    DieRollTask32,
    DieRollResults1,
    DieRollResults2,
    DieRollResults3,
    DieRollResults4,
    DieRollTaskEnd11,
    DieRollTaskEnd12,
    DieRollTaskEnd21,
    DieRollTaskEnd22,
    DieRollTaskEnd31,
    DieRollTaskEnd32,
    DieRollTaskEnd41,
    DieRollTaskEnd42,
]
