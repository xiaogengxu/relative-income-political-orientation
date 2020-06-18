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
Incentivized tasks
"""

list_euro = list(range(8))


class Constants(BaseConstants):
    name_in_url = 'incentivized_tasks'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donate = models.IntegerField(
        choices=list_euro,
        label="How many euros do you want to donate?"
    )

    lotto = models.IntegerField(
        choices=list_euro,
        label="How many euros do you want use to buy lotto-rows?"
    )