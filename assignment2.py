import numpy as np
import matplotlib.pyplot as pp


def utility_function(wealth, gamma):
    if gamma == 1:
        return np.log(wealth)
    elif gamma >= 0:
        return (wealth ** (1 - gamma) - 1) / (1 - gamma)

def inverse_utility(satisfaction, gamma):
    if gamma == 1:
        return np.e ** satisfaction
    else:
        return (satisfaction * (1 - gamma) + 1) ** (1 / (1 - gamma))


def marginal_utility_function(wealth, gamma):
    if gamma >= 0:
        return 1 / wealth ** gamma

#Part 1
print("Gamma = 0,5:")
expected_wealth = 0.5 * 1 + 0.5 * 999999
print("Expected Wealth: " + str(expected_wealth) + " Euros.")
expected_happiness = 0.5 * utility_function(1, 0.5) + 0.5 * utility_function(999999, 0.5)
certainty_equivalent = inverse_utility(expected_happiness, 0.5)
print("Certainty Equivalent: " + str(certainty_equivalent) + " Euros.")
risk_premium = expected_wealth - certainty_equivalent
print("Risk Premium: " + str(risk_premium) + " Euros.")
risk_premium_percentage = risk_premium / 10
print("Risk Premium Percentage: " + str(risk_premium_percentage) + " Percent.")

#Part 2


