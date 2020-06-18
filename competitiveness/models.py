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
Competitiveness and concern for social status
"""

def make_field_compete(label):
    return models.StringField(
        choices=['Strongly disagree','Disagree','Neutral','Agree','Strongly agree'],
        label=label,
        widget=widgets.RadioSelectHorizontal
    )


class Constants(BaseConstants):
    name_in_url = 'competitiveness'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    social_status = models.StringField(
            label="Social status is primarily determined by financial success.",
            choices=['Strongly disagree','Disagree','Slightly disagree','Neutral','Slightly agree',
                     'Agree','Strongly agree'],
            widget=widgets.RadioSelectHorizontal
    )

    competitiveness1 = make_field_compete("I enjoy working in situations involving competition with others.")
    competitiveness2 = make_field_compete("It is important to me to perform better than others on a task.")
    competitiveness3 = make_field_compete("I feel that winning is important in both work and games.")
    competitiveness4 = make_field_compete("It annoys me when other people perform better than I do.")
    competitiveness5 = make_field_compete("I try harder when I’m in competition with other people.")