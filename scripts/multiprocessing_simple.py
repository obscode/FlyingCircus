"""
   File   : multiprocessing_simple.py

   Author : Andrew Emerick
   Email  : aemerick@carnegiescience.edu

   This script provides an introduced to a more advanced
   python module `multiprocessing`, which allows you to take
   advantage of having a computer capable of running more than one
   process at a point in time across multiple cores.

   This is a particularly simple example to demonstrate how it works
   by running a function multiple times across all of the processors
   on your system at once. Unfortunately this is not a good example
   of how powerful of a tool this can be in speeding up analysis
   by a factor of approximately the number of processors you have.

   To give you an idea of when this can be useful, I use this mostly
   when I have to perform the same operations on a large number (>100)
   of independent datasets. For some of my analysis this can take a few to 10 minutes
   per dataset, so running a parallel script on 16-24 processors at once
   (the typical size of the number of processors on a single supercomputer node)
   cuts the run time down from say ~1000 minutes (~17 hours) to only ~42 minutes!!

   This works best / easiest in situations where things can be run completely
   independetly. If the result of a call to the function depends on what is done
   in a previous call, then things can get complicated fast.

   It is maybe worth noting that I believe there are three different python
   modules capable of doing something like this: `multiprocessing`,
   `joblib`, and `threading`. There are differences between them and how they
   operate, but `multiprocessing` is what I'm most familiar with so that
   is what I will use here.

   If you run this a few times, you'll see that the values printed are not
   necessarily in order. This is because when these are running in parallel
   you have no gauruntee that the processes run in sync with each other. This
   is not a problem if everything running is truly independent, but worth
   keeping in mind if this is not the case.

"""

import numpy as np

import multiprocessing
from multiprocessing   import Pool # import separately for convenience


def function_to_run(value):
    """
    This is the function to be run in parallel independently.

    Here, `value` is a number, but this could be a unique filename
    to open data from and do stuff with (for example)
    """

    process_id = multiprocessing.current_process().pid
    print("Hello, I am process %i printing value %i"%(process_id, value))

    return


if __name__ == "__main__":

    # get the number of CPUs on your computer
    n_proc = multiprocessing.cpu_count()

    # arbitrary values to pass to the function
    #   ranging from 1 to n_proc plus a shift
    values = np.arange(1, n_proc+1, 1) + 10

    # start a "pool" of "workers" to run
    # this function
    print("About to start:")


    # Note, the "with" statement basically is the same as
    # saying   pool = Pool(processes = n_proc), but is useful
    # because it automatically cleans up the 'pool' object
    # at the end of the code block.

    with Pool(processes = n_proc) as pool:

        # for demonstration purposes, lets loop over
        # calls to this function a few times:
        for i in [1,2,3]:
            pool.map(function_to_run, values * i)
            print("------------")

    print("All done!")
