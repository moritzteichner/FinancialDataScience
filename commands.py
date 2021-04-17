import numpy as np
import matplotlib
import matplotlib.pyplot as pp


def utility_function(wealth, gamma):
    if gamma == 1:
        return np.log(wealth)
    elif gamma >= 0:
        return (wealth ** float(1 - gamma) - 1) / (1 - gamma)

def marginal_utility_function(wealth, gamma):
    if gamma >= 0:
        return (1 / wealth ** gamma)

x_axis = np.arange(1, 999999, 10000)
print(x_axis)
curve = utility_function(x_axis, 0.6)
marginal_curve = marginal_utility_function(x_axis, 0.6)

pp.plot(x_axis, curve)
pp.plot(x_axis, marginal_curve)
pp.show()