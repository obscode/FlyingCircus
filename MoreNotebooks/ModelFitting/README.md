# Model Fitting in Python

I grouped these together since they are very similar. Each notebook solves
the same problem:  fitting an emission line and background, but uses 
3 different methods.

* NNLS.ipynb:  Start here. This notebook creates a fake emission line plus
  noise and fits it with ``scipy.optimize.fit_curve``. It also discusses
  how to visuallize the covariances in the parameters.

* Emcee.ipynb:  Fit the same spectral line with Markov Chain Monte Carlo (MCMC),
  specifically with the ``emcee`` package. Some discussion of Bayesian methods
  and visualizing the parameter space with "corner" plots.

* Pystan.ipynb: Same as Emcee.ipynb, but using the pystan package. Pystan is
  a very powerful MCMC sampler when the dimensions of your parameter space 
  get large (like 100's of parameters).

