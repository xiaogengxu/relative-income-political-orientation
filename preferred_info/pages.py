from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Preferred_info(Page):
    form_model = "player"
    form_fields = ["preferred_group"]

    def preferred_group_choices(self):
        import random
        options = [('postcode','my income relative to those living in my local area (postcode)'),
             ('education','my income relative to those having the same education as me'),
             ('occupation','my income relative to those working in the same profession as me'),
             ('all','my income relative to all other Finns')]
        random.shuffle(options)
        return options

# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [Preferred_info]
