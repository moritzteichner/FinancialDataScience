import numpy as np
import matplotlib.pyplot as pp

cov_matrix = np.array([[0.0256, 0.00128], [0.00128, 0.0016]])
returns = np.array([0.08, 0.03])
einheitsvektor = np.array([1,1])
inverse = np.linalg.inv(cov_matrix)

def get_minimum_variance_portfolios(lowerBound, upperBound, number):


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

print("100th PF:")
print(result[2][199])
print(result[0][199])
print(result[1][199])

def get_mvp_arithmetically():
    weights = inverse.dot(einheitsvektor) / (einheitsvektor.T.dot(inverse.dot(einheitsvektor)))
    m = weights.dot(returns)
    s = np.sqrt(weights.dot(cov_matrix.dot(weights)))
    print("Arith:")
    print(weights)
    print(m)
    print(s)

def get_minimum_variance_Portfolio():
    minimum = result[1][0]
    index = 0
    for x in range(400):
        if (result[1][x] < minimum):
            minimum = result[1][x]
            index = x
    print("MVP:")
    print(result[2][index])
    print(result[0][index])
    print(minimum)


def get_tangency_portfolio():
    maximum = (result[0][0] - 0.02) / result[1][0]
    index = 0
    for x in range(400):
        if ((result[0][x] - 0.02) / result[1][x] > maximum):
            maximum = (result[0][x] - 0.02) / result[1][x]
            index = x
    print("TP:")
    print(maximum)
    print(result[0][index])
    print(result[1][index])
    print(result[2][index])

    cal = 0.02 + (result[0][index] - 0.02) / result[1][index] * result[1]
    pp.plot(result[1], cal)

get_minimum_variance_Portfolio()
get_mvp_arithmetically()
get_tangency_portfolio()
pp.plot(result[1], result[0])
pp.show()
