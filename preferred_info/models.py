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
Preferred information
"""


class Constants(BaseConstants):
    name_in_url = 'preferred_info'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    preferred_group = models.StringField(
        label="",
        choices=(),
        widget=widgets.RadioSelect
    )

