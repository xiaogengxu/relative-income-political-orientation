from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Beliefs(Page):
    form_model = "player"
    form_fields = ['s_postcode','s_occupation','s_education','s_all',
                   'check_slider1','check_slider2','check_slider3','check_slider4']

    def check_slider1_error_message(self, value):
        if not value:
            return 'Please touch and move the slider in the first question.'

    def check_slider2_error_message(self, value):
        if not value:
            return 'Please touch and move the slider in the second question.'

    def check_slider3_error_message(self, value):
        if not value:
            return 'Please touch and move the slider in the third question.'

    def check_slider4_error_message(self, value):
        if not value:
            return 'Please touch and move the slider in the fourth question'

    def before_next_page(self):
        self.participant.vars['belief_postcode'] = self.player.s_postcode
        self.participant.vars['belief_occupation'] = self.player.s_occupation
        self.participant.vars['belief_education'] = self.player.s_education
        self.participant.vars['belief_all'] = self.player.s_all

# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Beliefs]
