# Extra Notebooks

In this folder you'll find more example notebooks that we've put together.
Here is a brief synopsis of each:

* BuggyPrograms.ipynb:  A good deal of time is spent debugging. Here's some
  code that has common mistakes. Try to find them all!

* NLLS.ipynm:  Fit a spectral line with non-linear least-squares (NLLS).
  Uses scipy's ``curve_fit`` and ``matplotlib`` to visualize the results.

* Emcee.ipynb:  Fit a spectral line with MCMC using the ``emcee`` package.
  Some discussion of Bayesian methods. 

* Skyfit.ipynb: fit real data of sky background levels and try to model the 
  contribution from the moon. Uses scipy to fit the model and bokeh to
  visualize the multi-dimensional data set.


Just a safe place to put our ipython notebook tutorials for the summer python
sessions held at the Carnegie Observatories.

The notebooks make reference to the data files that are also located in this repository.
There are also some extra notebooks that can be useful for seeing how to do
stuff. These are located in the MoreNotebooks folder.

To download this repository to your computer, run:

```   git clone https://github.com/obscode/FlyingCircus.git```
   
This will create a folder (`FlyingCircus`). Change to this folder and run the `jupyter` notebook viewer:

```   jupyter-notebook```
   
You should now get a browser from which you can select and launch the various `ipython` notebook files (`*.ipynb`).
