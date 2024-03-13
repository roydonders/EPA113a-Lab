# # remove model from import because of circular dependencie
from model import BangladeshModel
from components import Vehicle


# This class represents a scenario with probabilities for bridge quality
class Scenario:
    # Class variable to keep track of the next scenario ID
    next_scenario_id = 0

    def __init__(self, a, b, c, d, scenario_id=None):
        # bridge quality categories
        self.category_a_probability = a
        self.category_b_probability = b
        self.category_c_probability = c
        self.category_d_probability = d

        # Automatically assign a unique scenario ID
        self.scenario_id = Scenario.next_scenario_id
        # Increment the next scenario ID for the next scenario
        Scenario.next_scenario_id += 1

    def get_probability(self, s):
        """
        Returns the probability associated with the given category.

        Parameters:
        - s (str): A string representing the category ('A', 'B', 'C', or 'D').

        Returns:
        - float: The probability associated with the given category.

        Raises:
        - ValueError: If the input `s` is not 'A', 'B', 'C', or 'D'.
        """
        if s == 'A':
            return self.category_a_probability
        elif s == 'B':
            return self.category_b_probability
        elif s == 'C':
            return self.category_c_probability
        elif s == 'D':
            return self.category_d_probability
        else:
            raise ValueError("Invalid input. s must be 'A', 'B', 'C', or 'D'.")

    def __str__(self):
        s_id = str(self.scenario_id)
        return f"s{s_id}"


# This class is responsible for creating scenarios
class ScenarioCreator:
    scenarios = []

    # allows for specifying the number of scenarios to create
    def __init__(self, n = 9, create_scenarios_lab_2 = True):
        # number of scenarios
        self.num_scenarios = n

        if (create_scenarios_lab_2):
            self.scenarios = self.create_lab2_scenarios()

    # method creates scenarios for the lab assignment based on predefined probabilities.
    # Warning: hardcoding - should we perhaps read this in from excel file?
    def create_lab2_scenarios(self):
        s0 = Scenario(0,0,0,0)
        s1 = Scenario(0,0,0,0.05)
        s2 = Scenario(0,0,0,0.1)
        s3 = Scenario(0,0,0.05,0.1)
        s4 = Scenario(0,0,0.1,0.2)
        s5 = Scenario(0,0.05,0.1,0.2)
        s6 = Scenario(0,0.1,0.2,0.4)
        s7 = Scenario(0.05,0.1,0.2,0.4)
        s8 = Scenario(0.1,0.2,0.4,0.8)
        #scenario_list = [s0]
        scenario_list = [s0,s1,s2,s3,s4,s5,s6,s7,s8]
        return scenario_list





