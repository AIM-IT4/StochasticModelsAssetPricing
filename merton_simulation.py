
import numpy as np
import matplotlib.pyplot as plt

# Merton model parameters
r = 0.05
sigma = 0.3
lambda_jump = 0.5
mu_Y = -0.05
delta_Y = 0.15
T = 1.0
K = 100
S0 = 100
dt = 0.01
n_steps = int(T/dt)
n_simulations = 10000

def simulate_merton(r, sigma, lambda_jump, mu_Y, delta_Y, T, S0, dt, n_simulations):
    # ... (same as above)

# Simulate paths
S_merton = simulate_merton(r, sigma, lambda_jump, mu_Y, delta_Y, T, S0, dt, n_simulations)

# ... (rest of the Merton simulation code as above)
