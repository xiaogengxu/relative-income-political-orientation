from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Fairness(Page):
    form_model = 'player'
    form_fields = ['q1_fairness','q2_fairness','q3_fairness','q4_fairness','q5_fairness',
                   'q6_fairness','q7_fairness','q8_fairness']


class Deservingness(Page):
    form_model = 'player'
    form_fields = ['q1_deservingness','q2_deservingness','q3_deservingness']


# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Fairness, Deservingness]
