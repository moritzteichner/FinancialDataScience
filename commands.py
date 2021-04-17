import numpy as np
import matplotlib
import matplotlib.pyplot as pp


def utility_function(wealth, gamma):
    if gamma == 1:
        return np.log(wealth)
    elif gamma >= 0:
        return (wealth ** (1 - gamma) - 1) / (1 - gamma)


def marginal_utility_function(wealth, gamma):
    if gamma >= 0:
        return 1 / wealth ** gamma


x_axis = np.arange(1, 999999, 1000)

curve1 = utility_function(x_axis, 0.8)
marginal_curve1 = marginal_utility_function(x_axis, 0.8)

curve2 = utility_function(x_axis, 1)
marginal_curve2 = marginal_utility_function(x_axis, 1)

pp.plot(x_axis, curve1)
pp.plot(x_axis, marginal_curve1)

pp.plot(x_axis, curve2)
pp.plot(x_axis, marginal_curve2)

pp.legend(["U(WT), Gamma=0.8", "U'(WT), Gamma=0.8", "U(WT), Gamma=1", "U'(WT), Gamma=1"])
pp.xlabel("W_T")
pp.show()
