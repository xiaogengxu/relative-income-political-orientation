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
Belief elicitation
"""


class Constants(BaseConstants):
    name_in_url = 'beliefs'
    players_per_group = 3
    num_rounds = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoff_question(self):
        players = self.get_players()
        for p in players:
            import random
            question_list = ["postcode","occupation","education","all"]
            p.payoff_question = random.choice(question_list)


class Player(BasePlayer):
    payoff_question = models.StringField()
    s_postcode = models.IntegerField()
    s_occupation = models.IntegerField()
    s_education = models.IntegerField()
    s_all = models.IntegerField()
    check_slider1 = models.IntegerField(blank=True)
    check_slider2 = models.IntegerField(blank=True)
    check_slider3 = models.IntegerField(blank=True)
    check_slider4 = models.IntegerField(blank=True)
