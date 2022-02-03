from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Political_orientation(Page):
    form_model = 'player'
    form_fields = ['political_right', 'check_political_right', 'political_liberal',
                   'check_political_liberal', 'party']

    def error_message(self, values):
        if not values['check_political_right'] or not values['check_political_liberal'] or \
                not values['party']:
            return 'Please answer all questions on this page.'


page_sequence = [Political_orientation]
