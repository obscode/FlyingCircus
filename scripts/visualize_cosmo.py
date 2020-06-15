#!/usr/bin/env python
'''This script demonstrates how you can create interactive plots with
matplotlib. Specifically, it gives you two diagrams:  a 2D confidence
plot similar to the ones you'll see in supernova (SN) cosmology papers.
The other is the "fit" based on the parameters \Omage_m (matter) and
\Omega_\Lambda (dark energy). As you click and drag around the parameter
space, the fit will update accordingly, so you can see how entering 
regions of high probability correspond to good fits to the data.

We fit real SN data from Betoule et al. (2014). These are redshift
and distances from typeIa supernovae binned into 31 redshift bins.
To make the fitting faster (for smooth animation), we use the power-law
expansion of the luminosity-distance relation, up to 3rd order in
redshift.

This also illustrates how different redshift ranges change the shape
of the confidence ellipsoids. Usually we think of SN Ia data as 
constraining the deceleration, so the value of q_0:
   
   q_0 = 0.5(Omega_m - 2*Omega_l)
   
and so in an Omega_l vs Omega_m space, the major axis of the ellipses
should have roughly a a slope of 1/2. But that's only true at low-z,
where you can igmore the z^3 terms. At higher-z, z^3 becomes important
and the "cosmic jerk" now is also needed to fit, so the ellipses no
longer follow a slope of 1/2.'''


from matplotlib import pyplot as plt
from numpy import *   # Don't judge me!
from matplotlib import rcParams
import os
rcParams['font.size'] = 18

# The Betoule et al. (2014) data set. These are binned into several redshifts
# cov.dat is the covariance matrix. We'll just use the diagonal for errors
z,mu = loadtxt(os.path.join('data','Betoule_2014.t1.dat'), unpack=True)
cov = loadtxt(os.path.join('data','Betoule_2014.cov.dat'))
# The errors are the sqrt of the diagonal of the covariance matrix
emu = sqrt(diag(cov))

def dlum(z, h0, om, ol):
   '''Taylor series approximationg of luminosity distance up to z^3.
   Args:
      z (float/array):  redshift
      h0 (float): Hubble constant in km/s/Mpc
      om (float): matter density parameter (Omega-matter)
      ol (float): dark energy parameter (Omega-Lambda)
   Returns:
      float/array:  luminosity distance in Mpc
   '''
   q0 = 0.5*(om - 2*ol)
   j0 = om + ol
   ok = om + ol - 1
   return 3e5*z/h0*(1 + 0.5*(1-q0)*z - 1./6*(1-q0-3*q0**2+j0+ok)*z*z)

def muz(z, h0, om, ol):
   '''Distance modulus corresponding to the luminosity distance.
   Args:
      z (float/array):  redshift
      h0 (float): Hubble constant in km/s/Mpc
      om (float): matter density parameter (Omega-matter)
      ol (float): dark energy parameter (Omega-Lambda)
   Returns:
      float/array:  distane modulus, m-M'''
   dl = dlum(z, h0, om, ol)
   return 5*log10(dl) + 25

# Key bindings for interactive plots
def bind_click(event):
   '''What we do when the mouse-button is clicked.'''
   global buttondown
   buttondown = True

def bind_motion(event):
   '''What we do when the mouse is in motion and buttondown=True'''
   global buttondown, zs, m
   if not buttondown: return
   if not event.inaxes: return

   # Get current parameters from position in graph
   OM = event.xdata
   OL = event.ydata
   # Udpate the fit, and the legend
   m.set_ydata(muz(zs, 71, OM, OL) - muz(zs, 71, 0.3, 0.0))
   m.set_label('$\Omega_m = {:.2f}, \Omega_\Lambda = {:.2f}$'.format(OM,OL))
   m.axes.legend(fontsize=10, loc='upper left')
   # forces an update.  do this, or nothing happens!
   fig2.canvas.draw()

def bind_release(event):
   '''What we do when the mouse button is released'''
   global buttondown
   buttondown = False


###  Main part of the script.

# The Omega_m, Omega_L plot
fig1 = plt.figure(figsize=(6,8))
fig1.subplots_adjust(left=0.15)
ax1 = fig1.add_subplot(111)
ax1.set_xlabel('$\Omega_m$')
ax1.set_ylabel('$\Omega_\Lambda$')
buttondown = False

# Create the chi-square surface. Just compute it over a finite grid of 
# parameter values
OLs = linspace(0, 1.5, 100)
OMs = linspace(0, 1.0, 100)
chisqs = zeros((100,100))
# Change the list in the enumerate to set different redshift cuts
proxy = []   # needed to label contours
labs = []
for k,zmax in enumerate([0.5, 1.5]):
   # choose a different color each time
   cmap = ['Greens_r', 'Reds_r', 'Blues_r'][k]
   gids = less(z, zmax)
   for i in range(100):
      for j in range(100):
         # observed - model residuals
         delt = mu[gids] - muz(z[gids], 71, OMs[i], OLs[j])
         chisqs[j,i] = sum(power(delt/emu[gids],2))
   # Filled contours are all the rage! 
   cts = plt.contourf(OMs, OLs, chisqs, 
         levels=[chisqs.min()+2.3, chisqs.min()+6.17],
         cmap=cmap, origin='lower', extend='min')
   # This is so something shows up in the legend.
   proxy.append(plt.Rectangle((0,0), 1,1, 
      fc=cts.collections[1].get_facecolor()[0]))
   labs.append("z < {:.1f}".format(zmax))
ax1.legend(proxy, labs, fontsize=12, loc='lower right')

# Draw some constant-q0 lines
xx = linspace(0,1,100)
for q in [-0.25, -0.5, -0.75, -1.0]:
   ax1.plot(xx, xx/2 - q, '-', color='k', alpha=0.3)
   ax1.text(0.8, 0.8/2-q+0.02, "$q_0 = {:.2f}$".format(q), color='k', alpha=0.3,
         rotation=25, fontsize=10)

# Plot of Hubble residuals relative to a base model with Omega_m=0.3, 
# Omega_L=0.0. Easier to see the effects that way
fig2 = plt.figure()
fig2.subplots_adjust(left=0.18, bottom=0.14)
ax2 = fig2.add_subplot(111)
ax2.errorbar(z, mu-muz(z, 71, 0.3, 0.0), fmt='o', yerr=emu, label='JLA')
ax2.axhline(0, label='$\Omega_m = 0.3, \Omega_\Lambda=0.0$')
ax2.set_xlabel('Redshift')
ax2.set_ylabel('$\Delta \mu$ (mag)')
zs = linspace(0.001, z.max(), 100)
m, = ax2.plot(zs, 0*zs, label="$\Omega_m = 0.30, \Omega_\Lambda=0.00$")
ax2.legend(fontsize=10, loc='upper left')

# Connect the canvas events to the functions we set up
fig1.canvas.mpl_connect('button_press_event', bind_click)
fig1.canvas.mpl_connect('button_release_event', bind_release)
fig1.canvas.mpl_connect('motion_notify_event', bind_motion)

plt.show()
