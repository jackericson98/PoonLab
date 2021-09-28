import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))


# Variables
M0 = [1, 1, 0] # Initial Magnetization vector
B0 = 1  # Static Magnetic Field Strength
B_hat = [0, 0, B0]  # Static Magnetic Field Direction (currently misleading)
T1 = 100  # Longitudinal Relaxation Constant
T2 = 40  # Transverse Relaxation Constant
dt = T1/100  # Time Step
gamma = 1  # Gyromagnetic Ratio
num_its = 100  # Number of animation frames
w0 = gamma * B0  # Larmor Frequency
quiver_length = 1  # Length of the vector representing spin (should have a formula ... Spin mag?)


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
    Mz = solved_bloch(t)[2] + B0 * np.exp(t/T1)
    return Mx, My, Mz


quiver = ax.quiver(0, 0, 0, *M0)


def update(frame):

    global quiver
    quiver.remove()
    data = relaxation(frame)
    quiver = ax.quiver(0, 0, 0, *data, lw=2, length=quiver_length)


ani = FuncAnimation(fig, update, frames=np.linspace(0, 20*np.pi/w0, 5*num_its), interval=0.5)
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


# def diffy_bloch_eq(x_data, y_data, z_data):
#     global T1, T2, B_hat, dt
#     Bx, By, Bz = B_hat
#     Mx = x_data
#     My = y_data
#     Mz = z_data
#     dMxdt = (-1/T2) * Mx + (gamma * Bz) * My + (-gamma * By) * Mz
#     dMydt = (-gamma * Bz) * Mx + (-1/T2) * My + (gamma * Bx) * Mz
#     dMzdt = (gamma * By) * Mx + (-gamma * Bx) * My + (-1/T1) * Mz
#
#     return dMxdt * dt, dMydt * dt, dMzdt * dt
#
#
# """Iterable x, y, z, components change by increments of bloch(x, y, z) each iteration"""
#
#
# def make_data_array(num_frames):
#     global M0_with_tail
#     x0 = M0_with_tail[3]
#     y0 = M0_with_tail[4]
#     z0 = M0_with_tail[5]
#     x_data = [x0]
#     y_data = [y0]
#     z_data = [z0]
#     new_x = x0
#     new_y = y0
#     new_z = z0
#     for i in range(num_frames):
#         new_x = diffy_bloch_eq(x_data[i], y_data[i], z_data[i])[0] + new_x
#         new_y = diffy_bloch_eq(x_data[i], y_data[i], z_data[i])[1] + new_y
#         new_z = diffy_bloch_eq(x_data[i], y_data[i], z_data[i])[2] + new_z
#         x_data.append(new_x)
#         y_data.append(new_y)
#         z_data.append(new_z)
#
#     return x_data, y_data, z_data
#
#
# x, y, z = make_data_array(num_its)
# quiver = ax.quiver(*M0_with_tail)
#
#
# def update(frame):
#
#     global quiver, num_its
#     x_data, y_data, z_data = make_data_array(num_its)
#     quiver.remove()
#     quiver = ax.quiver(0, 0, 0, x_data[frame], y_data[frame], z_data[frame])
#
#
# ani = FuncAnimation(fig, update, frames=num_its, interval=0.0005)
plt.show()