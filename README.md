# SPT3G-montepython

**Contributors:** Anton Chudaykin

We present the complete SPT-3G likelihood for the MCMC sampler [Montepython](https://github.com/brinckmann/montepython_public). It includes the measurements of TE/EE power spectrum of the cosmic microwave background (CMB) using 95, 150, and 220 GHz data from the 1500 Square Degrees SPT-3G survey. Our code incorporates astrophysical foregrounds, instrumental calibration, beam uncertainty, bandpower window functions and covariance matrixes.

The original likelihood written for different MCMC sampler CosmoMC was presented in the following paper

* [*Measurements of the E-mode polarization and temperature-E-mode correlation of the CMB from SPT-3G 2018 data*](https://arxiv.org/abs/2101.01684)

Our likelihood was tested with [Montepython v3.4](https://baudren.github.io/montepython.html) and introduced in the paper

* [*Exploring LCDM extensions with SPT-3G and Planck data: 4σ evidence for neutrino masses, full resolution of the Hubble crisis by dark
  energy with phantom crossing, and all that*](https://arxiv.org/abs/2203.03666)

The repo includes: 

* Measurements of the E-mode polarization angular power spectrum (EE) and temperature-E-mode cross power spectrum (TE) over the multipole range 300<l<3000 in three frequency bands centered at 95, 150, and 220 GHz.

# Using the code

You can use SPT3G-likelihood freely, provided that in your publications you cite [arXiv:2203.03666](https://arxiv.org/abs/2203.03666). 
