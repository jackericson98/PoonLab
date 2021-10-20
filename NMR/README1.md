# NMR Python Project

A set of different analysis and visualization tools for Nuclear Magnetic 
Resonance data. 

## How to use:

**nmratom.py:** Describe an atom experiencing NMR 
phenomena (larmor precession, relaxation, rf pulse)

**Single_Relaxation_ani.py:** Creates an animation of the magnetic 
moment of a perturbed atomic nucleus as it relaxes.

**full_spectrum_relaxation_ani.py:** Takes a full spectrum of NMR 
peak volume data and returns a 3D animation of the relaxation of the 
peaks. Currently, the decay of each peak has the same test relaxation 
constant. 

**relaxation_curve_fit.py:** Takes relaxation data, creates a line
of best fit and returns a plot with the relaxation constant. Has a 
class that creates test relaxation data. 

**print2data.py:** POKY calculates peak volume and outputs 
values in the form:
>peak @ 112.041  7.498 lw  9.009 14.206 vol 9.778e+09 rms 16.3%
Isolated

Translates that to data values (peak location, line width values, volume, root mean square)

