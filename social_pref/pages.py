from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Social_pref(Page):
    form_model = 'player'
    form_fields = ['patience','risk_taking','positive_reciprocity','negative_reciprocity1',
                   'negative_reciprocity2','negative_reciprocity3','altruism','trust']


# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Social_pref]
