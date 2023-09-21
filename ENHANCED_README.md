
# Monte Carlo Simulations for Heston and Merton Models

This repository contains Python implementations of Monte Carlo simulations for both the Heston stochastic volatility model and the Merton jump-diffusion model. These models are pivotal in the world of quantitative finance for asset pricing and option valuation.

## Introduction

The world of finance has seen various models to explain and predict asset prices. Among them, the Heston and Merton models stand out due to their ability to capture more complex behaviors like stochastic volatility and price jumps, respectively. This repository offers a deep dive into these models, providing both the theoretical equations and their practical Python implementations.

## Heston Model

The Heston model is renowned for its capability to model the stochastic volatility of asset prices.

### Mathematical Formulation:

\[
dS_t = rS_t dt + \sqrt{v_t} S_t dW^S_t
\]
\[
dv_t = \kappa (	heta - v_t) dt + \sigma \sqrt{v_t} dW^v_t
\]

Where:
- \(S_t\): Asset price at time \(t\)
- \(v_t\): Variance of the asset price at time \(t\)
- \(r\): Risk-free rate
- \(\kappa\): Rate of reversion to \(	heta\)
- \(	heta\): Long-term variance
- \(\sigma\): Volatility of volatility
- \(dW^S_t\) and \(dW^v_t\): Wiener processes (Brownian motions) with correlation \(ho\)

### Implementation:

See [heston_simulation.py](heston_simulation.py) for the Python code.

## Merton Model

The Merton model, or the jump-diffusion model, introduces jumps in asset prices, capturing sudden and significant changes.

### Mathematical Formulation:

\[
dS_t = rS_t dt + \sigma S_t dW_t + S_t dJ_t
\]

Where:
- \(dJ_t\): Compound Poisson process (jumps)
- \(N(t)\): Poisson process with intensity \(\lambda\)
- \(Y_i\): i.i.d. random variables for jumps with mean \(\mu_Y\) and standard deviation \(\delta_Y\)

### Implementation:

See [merton_simulation.py](merton_simulation.py) for the Python code.

## Usage

To run the simulations, execute the respective Python files:

```bash
python heston_simulation.py
python merton_simulation.py
```

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
