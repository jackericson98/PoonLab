import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Bloch_equations import *

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

# Moving parts defined
quiver = ax.quiver(0, 0, 0, *M0)
quiver_xy = ax.quiver(0, 0, 0, quiver_length, 0, 0, color='black')
quiver_z = ax.quiver(0, 0, 0, 0, 0, 0)
time = ax.text(1, 0, 1, "Time (in ps) = %d" % 0)
xy_text = ax.text(1, 0, .8, "Transverse Magnetization = %f" % 1)
z_text = ax.text(1, 0, .6, "Longitudinal Magnetization = %f" % 0)


# Animation function defined
def update(frame):

    data = relaxation(frame)
    xy_mag = np.sqrt(data[0] ** 2 + data[1] ** 2)
    global quiver, quiver_z, quiver_xy, time, xy_text, z_text

    quiver.remove()
    quiver_xy.remove()
    quiver_z.remove()
    time.remove()
    xy_text.remove()
    z_text.remove()

    quiver = ax.quiver(0, 0, 0, *data, lw=2, length=quiver_length)
    quiver_xy = ax.quiver(1, 0, 0, xy_mag, 0, 0, lw=2, length=quiver_length, color='red')
    quiver_z = ax.quiver(1, 0, 0, 0, 0, data[2], lw=2, length=quiver_length, color='purple')

    time = ax.text(1, 0, 1, "Time = %d" % frame)
    xy_text = ax.text(1, 0, .8, "Transverse Magnetization = %.2f" % xy_mag)
    z_text = ax.text(1, 0, .6, "Longitudinal Magnetization = %.2f" % data[2])


# Plot stuff
ani = FuncAnimation(fig, update, frames=np.linspace(0, 20*np.pi/w0, 5*num_its), interval=0.5)
ax.quiver(-quiver_length, quiver_length, 0, 0.5 * quiver_length, 0, 0, color='black')
ax.quiver(-quiver_length, quiver_length, 0, 0, -0.5 * quiver_length, 0, color='black')
ax.quiver(-quiver_length, quiver_length, 0, 0, 0, 0.5 * quiver_length, color='black')
ax.text(-quiver_length, quiver_length - 0.7 * quiver_length, 0, "X")
ax.text(-quiver_length + 0.7 * quiver_length, quiver_length, 0, "Y")
ax.text(-quiver_length, quiver_length, 0.7 * quiver_length, "Z")


ax.set_title("NMR Relaxation")
ax.set_xlim(-1, 1.5)
ax.set_ylim(-1, 1.5)
ax.set_zlim(-1, 1)
ax.axis('off')

plt.show()