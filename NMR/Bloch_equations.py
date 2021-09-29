import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.animation import ArtistAnimation

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))


# Variables
M0 = [1, 1, 0] # Initial Magnetization vector
B0 = 1  # Static Magnetic Field Strength
B_hat = [0, 0, B0]  # Static Magnetic Field Direction (currently misleading)
T1 = 80  # Longitudinal Relaxation Constant
T2 = 40  # Transverse Relaxation Constant
dt = T1/100  # Time Step
gamma = .5  # Gyromagnetic Ratio
num_its = 100  # Number of animation frames
w0 = gamma * B0  # Larmor Frequency
quiver_length = 1  # Length of the vector representing spin (should have a formula ... Spin mag?)
t = np.linspace(0, 20 * np.pi / w0, 5 * num_its)


def solved_bloch(t):
    global w0, M0
    Mx = M0[0] * np.cos(w0 * t)
    My = -M0[1] * np.sin(w0 * t)
    Mz = 0
    return Mx, My, Mz


def relaxation(t):
    global T2
    Mx = solved_bloch(t)[0] * np.exp(-t/T2)
    My = solved_bloch(t)[1] * np.exp(-t / T2)
    Mz = solved_bloch(t)[2] + B0 * (1 - np.exp(-t/T1))
    return Mx, My, Mz


quiver = ax.quiver(0, 0, 0, *M0, length=quiver_length)
text = ax.text(1, 0, 1, "Time (in ps) = %d" % 0)

def update_solved(frame):

    global quiver, text
    text.remove()
    quiver.remove()
    data = relaxation(frame)
    quiver = ax.quiver(0, 0, 0, *data, lw=2, length=quiver_length)
    text = ax.text(1, 0, 1, "Time (in ps) = %d" % frame)


# Animation
ani = FuncAnimation(fig, update_solved, frames=t, interval=5)

# X, Y, Z Axes indicators
ax.quiver(-quiver_length, quiver_length, 0, 0.5 * quiver_length, 0, 0)
ax.quiver(-quiver_length, quiver_length, 0, 0, -0.5 * quiver_length, 0)
ax.quiver(-quiver_length, quiver_length, 0, 0, 0, 0.5 * quiver_length)
ax.text(-quiver_length, quiver_length - 0.7 * quiver_length, 0, "X")
ax.text(-quiver_length + 0.7 * quiver_length, quiver_length, 0, "Y")
ax.text(-quiver_length, quiver_length, 0.7 * quiver_length, "Z")


ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.axis('off')


def diff_bloch_eq(x_data, y_data, z_data):

    global T1, T2, B_hat, dt

    Bx, By, Bz = B_hat

    Mx = x_data
    My = y_data
    Mz = z_data

    dMx_dt = (-1/T2) * Mx + (gamma * Bz) * My + (-gamma * By) * Mz
    dMy_dt = (-gamma * Bz) * Mx + (-1/T2) * My + (gamma * Bx) * Mz
    dMz_dt = (gamma * By) * Mx + (-gamma * Bx) * My + (-1/T1) * Mz

    return dMx_dt * dt, dMy_dt * dt, dMz_dt * dt


"""Iterable x, y, z, components change by increments of bloch(x, y, z) each iteration"""


def make_data_array(num_frames):

    global M0
    x0 = M0[0]
    y0 = M0[1]
    z0 = M0[2]
    x_data = [x0]
    y_data = [y0]
    z_data = [z0]
    new_x = x0
    new_y = y0
    new_z = z0
    for i in range(num_frames):
        new_x = diff_bloch_eq(x_data[i], y_data[i], z_data[i])[0] + new_x
        new_y = diff_bloch_eq(x_data[i], y_data[i], z_data[i])[1] + new_y
        new_z = diff_bloch_eq(x_data[i], y_data[i], z_data[i])[2] + new_z
        x_data.append(new_x)
        y_data.append(new_y)
        z_data.append(new_z)

    return x_data, y_data, z_data


def update_diff(frame):

    global quiver, num_its
    x_data, y_data, z_data = make_data_array(num_its)
    quiver.remove()
    quiver = ax.quiver(0, 0, 0, x_data[frame], y_data[frame], z_data[frame])
    ax.text(1, 0, 1, "Time (in ps): \f", frame)
#
#
# ani = FuncAnimation(fig, update, frames=num_its, interval=0.0005)
plt.show()