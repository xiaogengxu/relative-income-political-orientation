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
Just world beliefs
"""


def make_field(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5, 6, 7],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

class Constants(BaseConstants):
    name_in_url = 'just_world'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q1_fairness = make_field('1. I feel that people generally earn the rewards and punishments that they get '
                               'in this world.')

    q2_fairness = make_field('2. People usually receive the outcomes that they deserve.')

    q3_fairness = make_field('3. People generally deserve the things that they are accorded.')

    q4_fairness = make_field('4. I feel that people usually receive the outcomes that they are due.')

    q5_fairness = make_field('5. People usually use fair procedures in dealing with others.')

    q6_fairness = make_field('6. I feel that people generally use methods that are fair in their evaluations of '
                               'others.')

    q7_fairness = make_field('7. Regardless of the specific outcomes they receive, people are subjected to fair '
                               'procedures.')

    q8_fairness = make_field('8. People are generally subjected to processes that are fair.')

    q1_deservingness = models.BooleanField(
        label='1. Which statement  do you agree with most?',
        choices=[[True,"One's income and position in society is mostly the result of one's individual effort."],
                 [False, "One's income and position in society is to a large extent the outcome of elements outside "
                         "of one's control (for example, including but not limited to family background, luck, "
                         "health issues, etc.)"]],
        widget=widgets.RadioSelect
    )

    q2_deservingness = models.StringField(
        label='2. Do you think that high earners in our society deserve their high incomes?',
        choices=['Hardly ever','Only some of the time','Sometimes','Most of the time',
                 'Just about always'],
        widget=widgets.RadioSelect
    )

    q3_deservingness = models.StringField(
        label='3. Do you think that poor people deserve to be poor in our society?',
        choices=['Hardly ever','Only some of the time','Sometimes','Most of the time',
                 'Just about always'],
        widget=widgets.RadioSelect
    )