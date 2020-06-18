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
Political preferences
"""


def make_field1(label):
    return models.StringField(
        choices=["Hardly ever", "Only some of the time", "Sometimes", "Most of the time", "Just about always"],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


def make_field2(label):
    return models.StringField(
        choices=["Strongly disagree", "Disagree", "Neither disagree nor agree", "Agree", "Strongly agree"],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )


class Constants(BaseConstants):
    name_in_url = 'political_pref'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    migration = models.StringField(
        label="There are different opinions about immigrants from other countries living in (respondent’s country). "
              "(By “immigrants” we mean people who come to settle in (respondent’s country). Do you think the number "
              "of immigrants to (respondent’s country) nowadays should be:",
        choices=["reduced a lot", "reduced a little", "remain the same as it is", "increased a little",
                 "increased a lot"],
        widget=widgets.RadioSelectHorizontal
    )

    trade = models.StringField(
        label="(Respondent’s country) should limit the import of foreign products in order to protect its national "
              "economy:",
        choices=["agree strongly", "agree", "neither agree nor disagree", "disagree", "disagree strongly"],
        widget=widgets.RadioSelectHorizontal
    )

    trust_institution1 = make_field1("1. How much of the time do you think you can trust government or public agencies "
                                     "to do what is right?")

    trust_institution2 = make_field1("2. How much of the time do you think you can trust men and women in political "
                                     "professions, who either hold or are running for public office?")

    trust_institution3 = make_field1(
        "3. How much of the time do you think you can trust the police to do what is right")

    income_tax1 = models.IntegerField()

    income_tax2 = models.IntegerField()

    income_tax3 = models.IntegerField()

    check_tax1 = models.IntegerField(blank=True)

    check_tax2 = models.IntegerField(blank=True)

    check_tax3 = models.IntegerField(blank=True)

    inheritance_tax_h = models.BooleanField(
        label="4. Currently, spouses and direct heirs face a tax of 19% on each additional dollar of inheritance "
              "after 1 million euros. Should this inheritance tax rate be increased or decreased?",
        choices=[[True,"Increased"],[False,"Decreased"]],
        widget=widgets.RadioSelectHorizontal
    )

    inheritance_tax_l = models.BooleanField(
        label="5. Currently, spouses and direct heirs are not liable for taxes for inheritances smaller than "
              "20,000 euros. Should this limit be increased or decreased?",
        choices=[[True,"Increased"],[False,"Decreased"]],
        widget=widgets.RadioSelectHorizontal
    )

    wealth_tax = models.StringField(
        label="6. Finland abolished its wealth tax in 2006. Would you support its reinstatement?",
        choices=["Strongly oppose","Oppose","Neither oppose nor support","Support","Strongly support"],
        widget=widgets.RadioSelectHorizontal
    )

    tax_balance = make_field2("7. The national government should adjust spending or taxes to balance its budget from "
                              "year to year.")

    spend_infrastructure = make_field2("8. The national government should spend more on infrastructure projects, "
                                 "including clean energy.")

    spend_edu = make_field2("9. The national government should spend more on education.")

    spend_social = make_field2("10. The national government should spend more on universal social services, "
                               "like the national pension plan.")

    spend_welfare = make_field2("11. The national government should spend more on programs that target "
                                "the poorest Finns, like welfare services.")

    spend_inc_diff = make_field2("12. The national government should spend more on programs that reduce regional "
                                 "income differences. [FNES]")

    activation_policy = models.StringField(
        label="1. “Activation policies” help ensure that Finns without jobs continue to look for them.",
        choices=["Strongly disagree","Disagree","Neither agree nor disagree","Agree","Strongly agree"],
        widget=widgets.RadioSelectHorizontal
    )

    universal_income = models.StringField(
        label="2. A “universal basic income” would reduce the incentive to work too much.",
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree", "Agree", "Strongly agree"],
        widget=widgets.RadioSelectHorizontal
    )