
# Stochastic Volatility and Jump Diffusion Models

This repository contains Monte Carlo simulations for the Heston and Merton models, which are used for asset pricing in finance.

## Heston Model

The Heston model is a stochastic volatility model defined by the following system of stochastic differential equations:

\[
dS_t = rS_t dt + \sqrt{v_t} S_t dW^S_t
\]
\[
dv_t = \kappa (	heta - v_t) dt + \sigma \sqrt{v_t} dW^v_t
\]

Where:
- \(S_t\) is the asset price at time \(t\)
- \(v_t\) is the variance of the asset price at time \(t\)
- \(r\) is the risk-free rate
- \(\kappa\) is the rate at which \(v_t\) reverts to \(	heta\)
- \(	heta\) is the long-term variance
- \(\sigma\) is the volatility of volatility
- \(dW^S_t\) and \(dW^v_t\) are Wiener processes (Brownian motions) with correlation \(
ho\)

## Merton Model

The Merton model, also known as the jump-diffusion model, is defined by:

\[
dS_t = rS_t dt + \sigma S_t dW_t + S_t dJ_t
\]

Where:
- \(dJ_t\) is a compound Poisson process representing the jumps
- \(N(t)\) is a Poisson process with intensity \(\lambda\)
- \(Y_i\) are i.i.d. random variables with mean \(\mu_Y\) and standard deviation \(\delta_Y\)

For more details, check the respective simulation files.
