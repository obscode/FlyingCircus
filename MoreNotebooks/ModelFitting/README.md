# Model Fitting in Python

I grouped these together since they are very similar. Each notebook solves
the same problem:  fitting an emission line and background, but uses 
3 different methods. I've also added a notebook about fitting data with
errors in both axes.

* NLLS.ipynb:  Start here. This notebook creates a fake emission line plus
  noise and fits it with ``scipy.optimize.fit_curve``. It then discusses
  how to visuallize the covariances in the parameters. Finally it presents
  shows the same fitting using `astropy.modeling`.

* Emcee.ipynb:  Fit the same spectral line with Markov Chain Monte Carlo (MCMC),
  specifically with the ``emcee`` package. Some discussion of Bayesian methods
  and visualizing the parameter space with "corner" plots. This is more
  advanced stuff, but if you want to see what all the Bayesian/MCMC hype is
  about, check it out.

* Pystan.ipynb: Same as Emcee.ipynb, but using the pystan package. Pystan is
  a very powerful MCMC sampler when the dimensions of your parameter space 
  get large (like 100's of parameters). More challenging to work with, but
  worth it if you have that kind of problem to deal with.
  
* Pymc.ipynb:  Yet another implementation of MCMC in python. This one combines
  the power of pystan, but is completely implemented in python (no separate 
  language to learn).

* ErrorsInXandY.ipynb:  a seemingly straightforward problem (fitting a 
  straight line through data with errors in both X and Y) has some very
  subtle issues. There's quite a bit of probability theory in this one, so 
  if that's something you're interested in, enjoy. Uses both emcee and
  pystan, so you should check those out first.

