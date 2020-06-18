from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Competitiveness(Page):
    form_model = 'player'
    form_fields = ['social_status','competitiveness1','competitiveness2','competitiveness3',
                   'competitiveness4','competitiveness5']


# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Competitiveness]
