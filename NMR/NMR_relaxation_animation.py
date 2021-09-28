"""The point of this file is to be able to input your data and receive a plot"""

from print2data import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

# Controllable Variables
speed = 1


# Exponential decay function
def decay(vol_array, iteration):
    old_data = vol_array
    new_data = []
    decay_constant = 2
    for i in range(len(vol_array)):
        decay_value = np.exp(-iteration * decay_constant)
        new_point = old_data[i] * decay_value
        new_data.append(new_point)
    return new_data


vol_data = ax.scatter(w1, w2, vol)


# Frame update function
def update(iteration):
    global vol_data
    vol_data.remove()
    vol_data = ax.scatter(w1, w2, decay(vol, iteration), color='red')


# Plot calls
ax.set_xlabel('Hydrogen Chemical Shift (ppm)')
ax.set_ylabel('Nitrogen Chemical Shift (ppm)')
ax.set_zlabel('Intensity (rms)')
ax.set_title('HSQC Relaxation')
z_max = np.max(vol)
ax.set_zlim(0, z_max)

ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100 // speed), interval=0.0005)

plt.show()
