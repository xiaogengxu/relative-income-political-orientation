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


author = 'Your name here'

doc = """
Informed consent
"""


class Constants(BaseConstants):
    name_in_url = 'infor_consent'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    consent = models.BooleanField(
        choices = [(True, 'I understand and consent.'), (False, 'I do not consent.')],
        widget=widgets.RadioSelect,
        label=''
    )
    consent2 = models.BooleanField(
        choices = [(True, 'I understand and consent.'), (False, 'I do not consent.')],
        widget=widgets.RadioSelect,
        label=''
    )