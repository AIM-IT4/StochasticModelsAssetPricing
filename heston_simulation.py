
import numpy as np
import matplotlib.pyplot as plt



# Heston model simulation parameters
r = 0.05  # risk-free rate
kappa = 2.0  # rate of reversion to theta
theta = 0.04  # long-term variance
sigma = 0.3  # volatility of volatility
rho = -0.6  # correlation between asset and variance processes
T = 1.0  # time to maturity
K = 100  # strike price of European call option
S0 = 100  # initial asset price
v0 = 0.04  # initial variance
dt = 0.01  # time step
n_steps = int(T/dt)
n_simulations = 10000

# Function to simulate the Heston model paths using the Euler-Maruyama method
def simulate_heston(r, kappa, theta, sigma, rho, T, S0, v0, dt, n_simulations):
    n_steps = int(T/dt)
    S = np.zeros((n_simulations, n_steps))
    v = np.zeros((n_simulations, n_steps))
    
    # Cholesky decomposition for correlated Brownian motions
    chol = np.linalg.cholesky([[1, rho], [rho, 1]])
    
    S[:, 0] = S0
    v[:, 0] = v0
    
    for t in range(1, n_steps):
        dW = np.dot(chol, np.random.normal(size=(2, n_simulations))).T
        dW_S = dW[:, 0]
        dW_v = dW[:, 1]
        
        # Euler-Maruyama method for Heston model
        S[:, t] = S[:, t-1] + r*S[:, t-1]*dt + np.sqrt(v[:, t-1])*S[:, t-1]*dW_S*np.sqrt(dt)
        v[:, t] = v[:, t-1] + kappa*(theta - np.maximum(v[:, t-1], 0))*dt + sigma*np.sqrt(np.maximum(v[:, t-1], 0))*dW_v*np.sqrt(dt)
        v[:, t] = np.maximum(v[:, t], 0)  # Ensure non-negative variance
        
    return S, v

# Simulate paths
S, v = simulate_heston(r, kappa, theta, sigma, rho, T, S0, v0, dt, n_simulations)

# Compute European call option payoff
payoffs = np.maximum(S[:, -1] - K, 0)
call_price = np.exp(-r*T) * np.mean(payoffs)

# Plot integrated variance vs realized asset price
integrated_variance = np.cumsum(v, axis=1) * dt
realized_asset = S[:, -1]

plt.figure(figsize=(10, 6))
plt.scatter(realized_asset, integrated_variance[:, -1], alpha=0.5, s=5)
plt.xlabel("Realized Asset Price")
plt.ylabel("Integrated Variance")
plt.title("Integrated Variance vs Realized Asset Price")
plt.grid(True)
plt.show()

# Plot simulated paths and histogram
plt.figure(figsize=(14, 6))

# 1. Simulated paths
plt.subplot(1, 2, 1)
for i in range(10):
    plt.plot(np.linspace(0, T, n_steps), S[i, :], lw=1)
plt.xlabel("Time")
plt.ylabel("Asset Price")
plt.title("Simulated Asset Price Paths")
plt.grid(True)

# 2. Rotated histogram to the right
plt.subplot(1, 2, 2)
plt.hist(S[:, -1], bins=50, orientation="horizontal", color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel("Frequency")
plt.ylabel("Asset Price at T")
plt.title("Distribution of Asset Prices at T")
plt.grid(True)

plt.tight_layout()
plt.show()

