
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


# Function to simulate the Merton model paths using the Euler-Maruyama method
def simulate_merton(r, sigma, lambda_jump, mu_Y, delta_Y, T, S0, dt, n_simulations):
    n_steps = int(T/dt)
    S = np.zeros((n_simulations, n_steps))
    
    S[:, 0] = S0
    
    for t in range(1, n_steps):
        dW = np.random.normal(size=n_simulations)
        
        # Poisson process for jumps
        n_jumps = np.random.poisson(lambda_jump*dt, size=n_simulations)
        
        # Log jump sizes
        Y = np.random.normal(mu_Y, delta_Y, size=n_simulations)
        
        # Euler-Maruyama method for Merton model
        S[:, t] = S[:, t-1] + r*S[:, t-1]*dt + sigma*S[:, t-1]*dW*np.sqrt(dt) + S[:, t-1]*(np.exp(Y) - 1)*n_jumps
        
    return S

# Simulate paths
S_merton = simulate_merton(r, sigma, lambda_jump, mu_Y, delta_Y, T, S0, dt, n_simulations)

# Compute European call option payoff
payoffs_merton = np.maximum(S_merton[:, -1] - K, 0)
call_price_merton = np.exp(-r*T) * np.mean(payoffs_merton)

# Plot simulated paths and histogram
plt.figure(figsize=(14, 6))

# 1. Simulated paths
plt.subplot(1, 2, 1)
for i in range(10):
    plt.plot(np.linspace(0, T, n_steps), S_merton[i, :], lw=1)
plt.xlabel("Time")
plt.ylabel("Asset Price")
plt.title("Simulated Asset Price Paths (Merton Model)")
plt.grid(True)

# 2. Rotated histogram to the right
plt.subplot(1, 2, 2)
plt.hist(S_merton[:, -1], bins=50, orientation="horizontal", color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel("Frequency")
plt.ylabel("Asset Price at T")
plt.title("Distribution of Asset Prices at T (Merton Model)")
plt.grid(True)

plt.tight_layout()
plt.show()

call_price_merton

