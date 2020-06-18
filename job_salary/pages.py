from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Employed(Page):
    form_model = 'player'
    form_fields = ['if_employed']

class Job(Page):
    form_model = 'player'
    form_fields = ['how_long', 'wage_satisfied', 'job_satisfied', 'fair_wage', 'leave_job',
                   'search_job']

    def is_displayed(self):
        return self.player.if_employed

class Unemployed(Page):
    form_model = 'player'
    form_fields = ['unem_or_out_labor']

    def is_displayed(self):
        return not self.player.if_employed

class Length_unemployed(Page):
    form_model = 'player'
    form_fields = ['how_long_unem']

    def is_displayed(self):
        return (not self.player.if_employed) and self.player.unem_or_out_labor

class Length_out_labor(Page):
    form_model = 'player'
    form_fields = ['how_long_out_labor']

    def is_displayed(self):
        return (not self.player.if_employed) and (not self.player.unem_or_out_labor)

# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Employed, Job, Unemployed, Length_unemployed, Length_out_labor]
