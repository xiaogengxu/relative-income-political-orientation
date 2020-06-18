from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Migration_trade(Page):
    form_model = 'player'
    form_fields = ['migration', 'trade']


class Trust(Page):
    form_model = 'player'
    form_fields = ['trust_institution1', 'trust_institution2', 'trust_institution3']


class Redistribution(Page):
    form_model = 'player'
    form_fields = ['income_tax1', 'income_tax2', 'income_tax3', 'check_tax1', 'check_tax2', 'check_tax3',
                   'inheritance_tax_h', 'inheritance_tax_l', 'wealth_tax', 'tax_balance',
                   'spend_infrastructure', 'spend_edu', 'spend_social', 'spend_welfare', 'spend_inc_diff']

    def check_tax1_error_message(self, value):
        if not value:
            return 'Please touch and move the slider to your preferred tax rate for the top 1% of all incomes in ' \
                   'Finland.'

    def check_tax2_error_message(self, value):
        if not value:
            return 'Please touch and move the slider to your preferred tax rate for the top 10% of all incomes in ' \
                   'Finland.'

    def check_tax3_error_message(self, value):
        if not value:
            return 'Please touch and move the slider to your preferred tax rate for the bottom 50% of all incomes in ' \
                   'Finland.'


class Labor_market(Page):
    form_model = 'player'
    form_fields = ['activation_policy', 'universal_income']


# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Migration_trade, Trust, Redistribution, Labor_market]
