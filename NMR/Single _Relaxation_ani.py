import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from nmratom import *
import numpy as np

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

# ----------------------- Set Up --------------------------
# Atom defined. Initial position and type
p = NMRAtom([0, 1, 1], 'N')

# Initial state of animated parts
main_quiver = ax.quiver(0, 0, 0, *p.relaxation(0))
quiver_xy = ax.quiver(0, 0, 0, *p.relaxation(0)[:2], 0, color='black')
quiver_z = ax.quiver(0, 0, 0, 0, 0, 0)
time = ax.text(1, 0, 1, "Time (in ps) = %d" % 0)
xy_text = ax.text(1, 0, .8, "Transverse Magnetization = %f" % 1)
z_text = ax.text(1, 0, .6, "Longitudinal Magnetization = %f" % 0)

# Number of iterations in the animated function
cum_time = 1000


# ---------------------- Animation Function --------------------
# Animation function
def update(frame):

    # Call variables
    global main_quiver, quiver_z, quiver_xy, time, xy_text, z_text, p

    # Create Data
    data = p.relaxation(frame)
    xy_mag = np.sqrt(data[0] ** 2 + data[1] ** 2)

    # Remove last frame
    main_quiver.remove()
    quiver_xy.remove()
    quiver_z.remove()
    time.remove()
    xy_text.remove()
    z_text.remove()

    # Quivers
    main_quiver = ax.quiver(0, 0, 0, *data, lw=2)
    quiver_xy = ax.quiver(1, 0, 0, xy_mag, 0, 0, lw=2, color='red')
    quiver_z = ax.quiver(1, 0, 0, 0, 0, data[2], lw=2, color='purple')

    # Text
    time = ax.text(1, 0, 1, "Time = %d" % frame)
    xy_text = ax.text(1, 0, .8, "Transverse Magnetization = %.2f" % xy_mag)
    z_text = ax.text(1, 0, .6, "Longitudinal Magnetization = %.2f" % data[2])


# -------------------------- Plot -------------------------------

# Animation Function plot
ani = FuncAnimation(fig, update, frames=cum_time, interval=5)

# Coordinate compass defined
axis_quiver_length = 1
ax.quiver(-axis_quiver_length, axis_quiver_length, 0, 0.5 * axis_quiver_length, 0, 0, color='black')
ax.quiver(-axis_quiver_length, axis_quiver_length, 0, 0, -0.5 * axis_quiver_length, 0, color='black')
ax.quiver(-axis_quiver_length, axis_quiver_length, 0, 0, 0, 0.5 * axis_quiver_length, color='black')
ax.text(-axis_quiver_length, axis_quiver_length - 0.7 * axis_quiver_length, 0, "X")
ax.text(-axis_quiver_length + 0.7 * axis_quiver_length, axis_quiver_length, 0, "Y")
ax.text(-axis_quiver_length, axis_quiver_length, 0.7 * axis_quiver_length, "Z")

# Plot info
ax.set_title("NMR Relaxation")
ax.set_xlim(-1, 1.5)
ax.set_ylim(-1, 1.5)
ax.set_zlim(-1, 1)
ax.axis('off')


plt.show()
