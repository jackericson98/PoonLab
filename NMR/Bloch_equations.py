import numpy as np

# Variables
M0 = [1, 1, 0]  # Initial Magnetization vector
B0 = 1  # Static Magnetic Field Strength
B_hat = [0, 0, B0]  # Static Magnetic Field Direction (currently misleading)
T1 = 60  # Longitudinal Relaxation Constant
T2 = 40  # Transverse Relaxation Constant
dt = T1/100  # Time Step
gamma = 1  # Gyromagnetic Ratio
num_its = 100  # Number of animation frames
w0 = gamma * B0  # Larmor Frequency
quiver_length = 1  # Length of the vector representing spin (should have a formula ... Spin mag?)


# Solution of the Bloch equations with T1, T2 --> infinity
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


# Actual Bloch Equations
def bloch_eq(x_data, y_data, z_data):
    global T1, T2, B_hat, dt
    Bx, By, Bz = B_hat
    Mx = x_data
    My = y_data
    Mz = z_data
    dMxdt = (-1/T2) * Mx + (gamma * Bz) * My + (-gamma * By) * Mz
    dMydt = (-gamma * Bz) * Mx + (-1/T2) * My + (gamma * Bx) * Mz
    dMzdt = (gamma * By) * Mx + (-gamma * Bx) * My + (-1/T1) * Mz

    return dMxdt * dt, dMydt * dt, dMzdt * dt


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
        new_x = bloch_eq(x_data[i], y_data[i], z_data[i])[0] + new_x
        new_y = bloch_eq(x_data[i], y_data[i], z_data[i])[1] + new_y
        new_z = bloch_eq(x_data[i], y_data[i], z_data[i])[2] + new_z
        x_data.append(new_x)
        y_data.append(new_y)
        z_data.append(new_z)
        # lineData[:, index] = lineData[:, index-1] + step

    return x_data, y_data, z_data
