import numpy as np

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

def utility_derivative_2(wealth,  gamma):
    return -gamma / wealth ** (gamma + 1)

def marginal_utility_function(wealth, gamma):
    if gamma >= 0:
        return 1 / wealth ** gamma

print("Task 1:")
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

print("Gamma = 0,9:")
expected_wealth2 = 0.5 * 1 + 0.5 * 999999
print("Expected Wealth: " + str(expected_wealth2) + " Euros.")
expected_happiness2 = 0.5 * utility_function(1, 0.9) + 0.5 * utility_function(999999, 0.9)
certainty_equivalent2 = inverse_utility(expected_happiness2, 0.9)
print("Certainty Equivalent: " + str(certainty_equivalent2) + " Euros.")
risk_premium2 = expected_wealth2 - certainty_equivalent2
print("Risk Premium: " + str(risk_premium2) + " Euros.")
risk_premium_percentage2 = risk_premium2 / 10
print("Risk Premium Percentage: " + str(risk_premium_percentage2) + " Percent.")

#Part 2

print("-----------------------------------")
print("Task 2:")

exact_expected_relative_happiness = 0.5 * utility_function(999999 / 1000, 0.5) + 0.5 * utility_function(1 / 1000, 0.5)
expected_relative_return = 0.5 * ((999999 - 1000) / 1000) + 0.5 * ((1 - 1000) / 1000)
variance_relative_return = 0.5 * ((((999999 - 1000) / 1000) - expected_relative_return) ** 2 + (((1 - 1000) / 1000) - expected_relative_return) ** 2)
approx_expected_relative_happiness = utility_function(1 + expected_relative_return, 0.5) + 0.5 * utility_derivative_2(1 + expected_relative_return, 0.5) * variance_relative_return

print("Exact expected happiness: " + str(exact_expected_relative_happiness))
print("Approximmated expected happiness " + str(approx_expected_relative_happiness))
