from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from django.utils.translation import ugettext_lazy as _

import random

author = 'Your name here'

doc = """
Social preferences
"""


class Constants(BaseConstants):
    name_in_url = 'political_orientation'
    players_per_group = 20
    num_rounds = 1

    que_list = ['posi_reci', 'neg_reci', 'trust_seq', 'compete1', 'compete2']
    que_list_act = ['patience_seq', 'altruism_seq', 'risk_taking_seq']


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    political_right = models.IntegerField()
    check_political_right = models.IntegerField(blank=True)

    political_liberal = models.IntegerField()
    check_political_liberal = models.IntegerField(blank=True)

    party = models.StringField(blank=True)

    lang = models.StringField(choices=[('en', 'English'), ('fi', 'suomi'), ('sv', 'svenska')],
                              widget=widgets.RadioSelectHorizontal)
