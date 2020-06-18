from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Summary(Page):
    form_model = 'player'


# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Summary]
