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
x_axis1 = np.arange(1, 500000, 1000)
x_axis2 = np.arange(500000, 999999, 1000)

curve1_1 = utility_function(x_axis1, 0.8)
curve1_2 = utility_function(x_axis2, 0.8)
marginal_curve1 = marginal_utility_function(x_axis, 0.8)

curve2_1 = utility_function(x_axis1, 0.1)
curve2_2 = utility_function(x_axis2, 0.1)
marginal_curve2 = marginal_utility_function(x_axis, 0.1)

pp.subplot(1, 2, 1)
pp.plot(x_axis1, curve1_1, color="red")
pp.plot(x_axis2, curve1_2, color="green")

pp.plot(x_axis1, curve2_1, color="red")
pp.plot(x_axis2, curve2_2, color="green")

pp.xlabel("W_T in Euros")
pp.ylabel("U(W_T)")

pp.subplot(1, 2, 2)
pp.plot(x_axis, marginal_curve1, color="blue")
pp.plot(x_axis, marginal_curve2, color="black")
pp.xlabel("W_T in Euros")
pp.ylabel("U'(W_T)")
pp.show()
