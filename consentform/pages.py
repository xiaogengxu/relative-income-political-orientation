from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InformedConsent(Page):
    form_model = 'player'
    form_fields = ['consent']


class InformedConsent2(Page):
    form_model = 'player'
    form_fields = ['consent2']

    def is_displayed(self):
        return not self.player.consent


class NoConsent(Page):
    def is_displayed(self):
        return (not self.player.consent) and (not self.player.consent2)


page_sequence = [InformedConsent, InformedConsent2, NoConsent]
