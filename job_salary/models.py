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
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'job_salary'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    if_employed = models.BooleanField(
        choices=[[True, 'I am currently employed.'], [False, 'I am currently not employed.']],
        widget=widgets.RadioSelect,
        label='Are you currently employed?'
    )
    how_long = models.StringField(
        label='How long have you held this job?',
        choices=['Less than one year','One to three years','Three to five years','Five to ten years'
            ,'More than ten years'],
        widget=widgets.RadioSelect
    )
    wage_satisfied = models.StringField(
        label='How satisfied are you with your wage/salary on this job?',
        choices=['Not at all satisfied', 'Not too satisfied', 'Somewhat satisfied', 'Very satisfied'],
        widget=widgets.RadioSelect
    )
    job_satisfied = models.StringField(
        label='How satisfied are you with this job?',
        choices=['Not at all satisfied', 'Not too satisfied', 'Somewhat satisfied', 'Very satisfied'],
        widget=widgets.RadioSelect
    )
    fair_wage = models.StringField(
        label='Do you agree or disagree that your wage is set fairly in relation to others with your '
              'primary employer?',
        choices=['Stronly disagree', 'Disagree', 'Agree', 'Strongly agree'],
        widget=widgets.RadioSelect
    )
    leave_job = models.StringField(
        label='How likely is it that you will voluntarily leave your job during the next year?',
        choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'],
        widget=widgets.RadioSelect
    )
    search_job = models.StringField(
        label='How likely is it that you will seriously search for an alternative to your primary job while working '
              'there, whether or not it leads to an offer?',
        choices=['Very unlikely', 'Somewhat unlikely', 'Somewhat likely', 'Very likely'],
        widget=widgets.RadioSelect
    )
    unem_or_out_labor = models.BooleanField(
        choices=[[True, 'Unemployed'],[False, 'Out of the labor force']],
        widget=widgets.RadioSelect,
        label='Are you unemployed  or out of the labor force?'
    )
    how_long_unem = models.StringField(
        label='How long have you been unemployed?',
        choices=['Less than one year', 'One to three years', 'Three to five years', 'Five to ten years'
            , 'More than ten years'],
        widget=widgets.RadioSelect
    )
    how_long_out_labor = models.StringField(
        label='How long have you been out of labor force?',
        choices=['Less than one year', 'One to three years', 'Three to five years', 'Five to ten years'
            , 'More than ten years'],
        widget=widgets.RadioSelect
    )
