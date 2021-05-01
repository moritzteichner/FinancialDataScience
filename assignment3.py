import numpy as np
import matplotlib.pyplot as pp

cov_matrix = np.array([[0.4, 0.00128], [0.00128, 0.2]])
returns = np.array([0.08, 0.03])
einheitsvektor = np.array([1,1])

def get_minimum_variance_portfolios(lowerBound, upperBound, number):

    inverse = np.linalg.inv(cov_matrix)
    X = returns.dot(inverse.dot(returns))
    Y = returns.dot(inverse.dot(einheitsvektor))
    Z = einheitsvektor.dot(inverse.dot(einheitsvektor))

    D = X * Z - (Y ** 2)

    g = (1 / D) * (X * inverse.dot(einheitsvektor) - Y * inverse.dot(returns))
    h = (1 / D) * (Z * inverse.dot(returns) - Y * inverse.dot(einheitsvektor))

    increment = (upperBound - lowerBound) / (number - 1)

    weight_matrix = np.zeros((number, 2))
    mu = np.zeros((number, 1))
    sigma = np.zeros((number, 1))

    for x in range(number):
        mu[x] = x * increment + lowerBound
        weight_matrix[x] = np.add(g, h*mu[x])
        sigma[x] = np.sqrt(weight_matrix[x].dot(cov_matrix.dot(weight_matrix[x])))

    return mu, sigma, weight_matrix

result = get_minimum_variance_portfolios(0, 0.2, 400)

pp.plot(result[1], result[0])
pp.show()
