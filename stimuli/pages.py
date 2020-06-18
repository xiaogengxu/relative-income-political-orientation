from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Stimuli(Page):
    form_model = "player"
    # form_fields = ['b_postcode','b_occupation','b_education','b_all']

    def vars_for_template(self):
        b_postcode = self.participant.vars['belief_postcode']
        b_occupation = self.participant.vars['belief_occupation']
        b_education = self.participant.vars['belief_education']
        b_all = self.participant.vars['belief_all']
        return {"b_postcode": b_postcode,
                "b_occupation": b_occupation,
                "b_education": b_education,
                "b_all": b_all,}
        # self.player.b_occupation = self.player.vars['belief_occupation']
        # self.player.b_education = self.player.vars['belief_education']
        # self.player.b_all = self.player.vars['belief_all']

# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Stimuli]
