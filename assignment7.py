# Import packages for econometric analysis

import numpy as np
import pandas as pd

# Load plotting library

import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

#set the seed
np.random.seed(123)

def simulateJumpDiffusion(m, s0, r, lam, sig, T, a, b):
    result = np.empty(m)
    for x in range(m):
        Z1 = np.random.normal(0, 1)
        K = np.random.poisson(lam)
        Z2 = np.random.normal(0, 1)

        result[x] = s0 * np.exp(
            (r - lam * a - 0.5 * (sig ** 2)) * T + (sig * np.sqrt(T) * Z1) + a * K * T + b * np.sqrt(K * T) * Z2)

    return result

m = 1000000    # number of paths in simulation
S_0 = 120
r = 0.04
lam = 2
sig = 0.5
T = 0.25
a = 0.1
b = 0.2

s1 = simulateJumpDiffusion(m, S_0, r, lam, sig, T, a, b)
E_s1 = np.mean(s1)
print(E_s1)