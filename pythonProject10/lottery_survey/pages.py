from otree.api import Page
from .models import Constants
import random


class Roulette(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        # Randomly select one of the 45 rounds
        selected_round = random.randint(1, Constants.num_rounds)
        player_in_selected_round = self.player.in_round(selected_round)

        # Get the scenario and round information for the selected round
        scenario_index = (selected_round - 1) // 9
        round_in_scenario = (selected_round - 1) % 9
        scenario = Constants.scenarios[scenario_index]

        # Safely get the alpha value, use a default if it's None
        alpha = player_in_selected_round.field_maybe_none('alpha')
        if alpha is None:
            alpha = 0.5  # Default value if alpha is not set

        p = round(scenario['p_values'][round_in_scenario], 2)
        one_minus_p = round(1 - p, 2)
        x1_l = scenario['x1_l_values'][round_in_scenario]
        x1_h = scenario['x1_h_values'][round_in_scenario]
        x2_l = scenario['x2_l_values'][round_in_scenario]
        x2_h = scenario['x2_h_values'][round_in_scenario]

        expected_value = (p * (alpha * x1_l + (1 - alpha) * x2_h) + one_minus_p * (alpha * x1_h + (1 - alpha) * x2_l))

        return {
            'selected_round': selected_round,
            'alpha': round(alpha, 2),
            'p': p,
            'one_minus_p': one_minus_p,
            'x1_l': round(x1_l, 1),
            'x1_h': round(x1_h, 1),
            'x2_l': round(x2_l, 1),
            'x2_h': round(x2_h, 1),
            'expected_value': round(expected_value, 2),
            'Constants': Constants  # Add this line to include Constants in the context
        }


class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['consent_age', 'consent_read', 'consent_participate']
    def is_displayed(self):
        return self.round_number == 1


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1



class LotterySurvey(Page):
    form_model = 'player'
    form_fields = ['alpha']

    def vars_for_template(self):
        scenario_index = (self.round_number - 1) // 9
        round_in_scenario = (self.round_number - 1) % 9
        scenario = Constants.scenarios[scenario_index]
        vars_dict = {
            'round_number': self.round_number,
            'num_rounds': Constants.num_rounds,
            'scenario_number': scenario_index + 1,
            'round_in_scenario': round_in_scenario + 1,
            'p': scenario['p_values'][round_in_scenario],
            'one_minus_p': self.player.one_minus_p,
            'x1_l': scenario['x1_l_values'][round_in_scenario],
            'x1_h': scenario['x1_h_values'][round_in_scenario],
            'x2_l': scenario['x2_l_values'][round_in_scenario],
            'x2_h': scenario['x2_h_values'][round_in_scenario],
        }
        print("Debug - vars_for_template:", vars_dict)
        return vars_dict


class ConsentForm(Page):
    form_model = 'player'
    form_fields = ['consent_age', 'consent_read', 'consent_participate']

    def is_displayed(self):
        return self.round_number == 1
    def error_message(self, values):
        if not (values['consent_age'] and values['consent_read'] and values['consent_participate']):
            return 'Debe aceptar todos los elementos de consentimiento para continuar.'

class example(Page):
    def is_displayed(self):
        return self.round_number == 1

class example2(Page):
    def is_displayed(self):
        return self.round_number == 1

class welcome(Page):
    def is_displayed(self):
        return self.round_number == 1

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1



class SurveyIntroduc(Page):
    template_name = 'investment_game/SurveyIntroduc.html'

    def is_displayed(self):
        return self.round_number == Constants.individual_rounds + 4


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age_check', 'gender', 'career', 'native_language', 'university_year', 'gpa', 'smoker', 'alcohol', 'drugs', 'weekly_spending']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_linda', 'crt_bat', 'crt_widget', 'crt_lake', 'crt_double']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class FinancialLiteracy(Page):
    form_model = 'player'
    form_fields = ['fin_change', 'fin_lottery', 'fin_sale', 'fin_disease', 'fin_cardealer', 'fin_interest']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class RiskAttitudes(Page):
    form_model = 'player'
    form_fields = ['risk_general', 'risk_driving', 'risk_career', 'risk_health']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class DecisionMakingScenarios(Page):
    form_model = 'player'
    form_fields = ['scenario_jar', 'monty_hall']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class MatrixReasoning(Page):
    form_model = 'player'
    form_fields = ['Matrix_B06', 'Matrix_B09', 'Matrix_B11', 'Matrix_C02', 'Matrix_C05',
                   'Matrix_C12', 'Matrix_D05', 'Matrix_D07', 'Matrix_E07']
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class EndPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        self.player.exit_survey_completed = True
    pass



page_sequence = [
                 welcome,
                 Introduction,
                 example,
                 example2,
                 LotterySurvey,
                 Roulette,
                 SurveyIntroduc,
                 Demographics,
                 CognitiveReflectionTest,
                 FinancialLiteracy,
                 RiskAttitudes,
              #   MatrixReasoning,
                 DecisionMakingScenarios,
                 EndPage
                 ]