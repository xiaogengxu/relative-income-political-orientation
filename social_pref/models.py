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
Social preferences
"""


def make_field(label):
    return models.IntegerField(
        choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Constants(BaseConstants):
    name_in_url = 'social_pref'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    patience = make_field("(Self-assessment:) How willing are you to give up something that is beneficial for you "
                          "today in order to benefit more from that in the future?")

    risk_taking = make_field("(Self-assessment:) Please tell me, in general, how willing or unwilling you are to take "
                             "risks. Please use a scale from 0 to 10, where 0 means “completely unwilling to take "
                             "risks” and a 10 means you are “very willing to take risks”.")

    positive_reciprocity = make_field("(Self-assessment:)When someone does me a favor I am willing to return it.")

    negative_reciprocity1 = make_field("(Self-assessment:) If I am treated very unjustly, I will take revenge at the "
                                       "first occasion, even if there is a cost to do so.")

    negative_reciprocity2 = make_field("(Willingness to act:) How willing are you to punish someone who treats you "
                                       "unfairly, even if there may be costs for you?")

    negative_reciprocity3 = make_field("(Willingness to act:) How willing are you to punish someone who treats others "
                                       "unfairly, even if there may be costs for you?")

    altruism = make_field("(Willingness to act:) How willing are you to give to good causes without expecting anything "
                          "in return?")

    trust = make_field("(Self-assessment:) I assume that people have only the best intentions.")
