
import numpy as np
import matplotlib.pyplot as plt

# Heston model parameters
r = 0.05
kappa = 2.0
theta = 0.04
sigma = 0.3
rho = -0.6
T = 1.0
K = 100
S0 = 100
v0 = 0.04
dt = 0.01
n_steps = int(T/dt)
n_simulations = 10000

def simulate_heston(r, kappa, theta, sigma, rho, T, S0, v0, dt, n_simulations):
    # ... (same as above)

# Simulate paths
S, v = simulate_heston(r, kappa, theta, sigma, rho, T, S0, v0, dt, n_simulations)

# ... (rest of the Heston simulation code as above)
