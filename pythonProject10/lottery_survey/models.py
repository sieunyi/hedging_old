from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range
)



class Player(BasePlayer):
    # Consent form fields
    consent_age = models.BooleanField(
        label="I am 18 years of age or older."
    )
    consent_read = models.BooleanField(
        label="I have read and understand the information above."
    )
    consent_participate = models.BooleanField(
        label="I want to participate in this research and continue with the study."
    )

    # Survey fields
    age_check = models.BooleanField(
        label="Are you 18 years of age or older?",
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ]
    )
    gender = models.StringField(
        label="What gender do you identify as?",
        choices=['Female', 'Non-binary', 'Male'],
        widget=widgets.RadioSelect
    )
    career = models.StringField(label="What is your major?")
    native_language = models.StringField(label="What is your native language?")
    university_year = models.StringField(label="What year are you in university?",
                                         choices=['First year', 'Second year', 'Third year', 'Fourth year', 'Graduate',
                                                  'Other'], widget=widgets.RadioSelect)
    gpa = models.FloatField(label="What is your current GPA? (0-4, up to 4 decimal places)", min=0, max=4)
    smoker = models.StringField(
        label="Are you a smoker?",
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Prefer not to answer', 'Prefer not to answer']],
        widget=widgets.RadioSelect
    )
    alcohol = models.StringField(
        label="Do you practice excessive alcohol consumption?",
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Prefer not to answer', 'Prefer not to answer']],
        widget=widgets.RadioSelect
    )
    drugs = models.StringField(
        label="Do you use recreational drugs?",
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Prefer not to answer', 'Prefer not to answer']],
        widget=widgets.RadioSelect
    )

    weekly_spending = models.IntegerField(label="What is your weekly spending in USD?")

    # Cognitive Reflection Test
    crt_linda = models.StringField(
        label="Which of the following two alternatives is more likely?",
        choices=[
            'Linda is a bank teller.',
            'Linda is a bank teller and active in the feminist movement.'
        ],
        widget=widgets.RadioSelect
    )
    crt_bat = models.FloatField(label="How much does the ball cost in dollars?")
    crt_widget = models.IntegerField(label="How many minutes would it take 100 machines to make 100 widgets?")
    crt_lake = models.IntegerField(label="How many days would it take to cover half of the lake?")
    crt_double = models.StringField(
        label="In 2021, how much will you be able to buy with your income?:",
        choices=[
            'More than today.',
            'Exactly the same as today.',
            'Less than today.'
        ],
        widget=widgets.RadioSelect
    )

    # Financial Literacy
    fin_change = models.IntegerField(label="")
    fin_lottery = models.IntegerField(label="")
    fin_sale = models.IntegerField(label="")
    fin_cardealer = models.IntegerField(label="")
    fin_interest = models.IntegerField(label="")
    fin_disease = models.IntegerField(label="")

    # Risk Attitudes
    risk_general = models.IntegerField(label="How would you rate your willingness to take risks in general?", min=1,
                                       max=10)
    risk_driving = models.IntegerField(label="How would you rate your willingness to take risks while driving?", min=1,
                                       max=10)
    risk_career = models.IntegerField(
        label="How would you rate your willingness to take risks in your professional career?", min=1, max=10)
    risk_health = models.IntegerField(
        label="How would you rate your willingness to take risks with respect to your health?", min=1, max=10)

    # Decision Making Scenarios
    scenario_jar = models.StringField(
        label="Which jar do you prefer to guess the color of a ball from?",
        choices=[
            'I prefer to guess the color of a ball from jar 1.',
            'I am indifferent.',
            'I prefer to guess the color of a ball from jar 2.'
        ],
        widget=widgets.RadioSelect
    )
    monty_hall = models.StringField(
        label="Is it advantageous for you to change your choice?",
        choices=[
            'I prefer to keep my original choice (Door number 1).',
            'It does not matter if I change or not.',
            'I prefer to switch to Door number 2.'
        ],
        widget=widgets.RadioSelect
    )

    # Timing fields
    decision_time = models.FloatField()
    continue_field = models.StringField(label="")
    exit_survey_completed = models.BooleanField(initial=False)


# Fields from the second Player class
    alpha = models.FloatField(min=0, max=1)
    p = models.FloatField()
    one_minus_p = models.FloatField()
    x1_l = models.FloatField()
    x1_h = models.FloatField()
    x2_h = models.FloatField()
    x2_l = models.FloatField()


class Constants(BaseConstants):
    name_in_url = 'hedging'
    players_per_group = None
    num_rounds = 45
    individual_rounds = 45

    scenarios = [
        {
            'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            'x1_l_values': [-6.0, -4.0, -3.1, -2.4, -2.0, -1.6, -1.3, -1.0, -0.7],
            'x1_h_values': [0.7, 1.0, 1.3, 1.6, 2.0, 2.4, 3.1, 4.0, 6.0],
            'x2_h_values': [0.4, 0.7, 1.1, 1.5, 2.0, 2.6, 3.3, 4.3, 6.3],
            'x2_l_values': [-6.3, -4.3, -3.3, -2.6, -2.0, -1.5, -1.1, -0.7, -0.4]
        },
        {
            'p_values': [0.5] * 9,
            'one_minus_p_values': [0.5] * 9,
            'x1_l_values': [-8, -7, -6, -5, -4, -3, -2, -1, 0],
            'x1_h_values': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'x2_h_values': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'x2_l_values': [-8, -7, -6, -5, -4, -3, -2, -1, 0]
        },
        {
            'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            'x1_l_values': [-6.0, -4.0, -3.1, -2.4, -2.0, -1.6, -1.3, -1.0, -0.7],
            'x1_h_values': [0.7, 1.0, 1.3, 1.6, 2.0, 2.4, 3.1, 4.0, 6.0],
            'x2_h_values': [6.4, 4.0, 3.1, 2.4, 2.0, 1.6, 1.3, 1.0, 0.7],
            'x2_l_values': [-0.7, -1.0, -1.3, -1.6, -2.0, -2.4, -3.1, -4.0, -6.0]
        },
        {
            'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            'x1_l_values': [-6.0, -4.0, -3.1, -2.4, -2.0, -1.6, -1.3, -1.0, -0.7],
            'x1_h_values': [0.7, 1.0, 1.3, 1.6, 2.0, 2.4, 3.1, 4.0, 6.0],
            'x2_h_values': [0.4] * 9,
            'x2_l_values': [-6.3, -4.6, -4.0, -3.7, -3.6, -3.7, -4.0, -4.6, -6.3]
        },
        {
            'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
            'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
            'x1_l_values': [-6.0, -4.0, -3.1, -2.4, -2.0, -1.6, -1.3, -1.0, -0.7],
            'x1_h_values': [0.7, 1.0, 1.3, 1.6, 2.0, 2.4, 3.1, 4.0, 6.0],
            'x2_h_values': [6.3, 4.6, 4.0, 3.7, 3.6, 3.7, 4.0, 4.6, 6.3],
            'x2_l_values': [-0.4] * 9
        }
    ]


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            scenario_index = (player.round_number - 1) // 9
            round_in_scenario = (player.round_number - 1) % 9
            scenario = Constants.scenarios[scenario_index]

            player.p = scenario['p_values'][round_in_scenario]
            player.one_minus_p = scenario['one_minus_p_values'][round_in_scenario]
            player.x1_l = scenario['x1_l_values'][round_in_scenario]
            player.x1_h = scenario['x1_h_values'][round_in_scenario]
            player.x2_h = scenario['x2_h_values'][round_in_scenario]
            player.x2_l = scenario['x2_l_values'][round_in_scenario]


class Group(BaseGroup):
    pass