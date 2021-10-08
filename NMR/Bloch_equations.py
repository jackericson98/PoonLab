import numpy as np

# Variables
M0 = [1, 1, 1]  # Initial Magnetization vector
B0 = 1.  # Static Magnetic Field Strength
B_hat = [0., 0., B0]  # Static Magnetic Field Direction (currently misleading)
B1 = 1 # RF Field Amplitude
T1 = 100  # Longitudinal Relaxation Constant
T2 = 60  # Transverse Relaxation Constant
dt = T1/100  # Time Step
gamma = 1  # Gyromagnetic Ratio
num_its = 100  # Number of animation frames
w0 = gamma * B0  # Larmor Frequency
wrf = 2 # RF Pulse frequency
omega = w0 - wrf
quiver_length = 1  # Length of the vector representing spin (should have a formula ... Spin mag?)
phi = np.pi/4


# Solution of the Bloch equations with T1, T2 --> infinity
def initial_state(t):
    global M0, w0
    Mx = M0[0] * np.cos(w0 * t)
    My = -M0[1] * np.sin(w0 * t)
    Mz = M0[2]
    return Mx, My, Mz


def rf_pulse(t):
    B_rf = [B1*np.cos(wrf * t + phi), B1*np.sin(wrf * t + phi), 0]
    return B_rf

# Equation 1.25 & 1.27 - Mz_0 = the z component of the magnetization of the nucleus at t = 0 after the rf field has been
# applied. This will change depending on how long the rf field was applied for and what the rotation angle alpha is.
# Set to 0 to represent a 90 degree pulse
def relaxation(t):
    global T2, T1
    Mz_0 = 0
    x0, y0, z0 = initial_state(t)
    Mx = x0 * np.exp(-t / T2)
    My = y0 * np.exp(-t / T2)
    Mz = z0 - (z0 - Mz_0) * np.exp(-t / T1)
    return Mx, My, Mz


# Bloch equations from equations 1.30 - 1.33 in the NMR Text
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


def bloch_eq(M_t):
    global omega, T1, T2, phi
    R1, R2 = 1/T1, 1/T2
    evo_mat = [-R2, -omega, w0 * np.sin(2*phi)], [omega, -R2, -w0 * np.cos(phi)], [-w0 * np.sin(phi), w0 * np.cos(phi), -R1]
    dMt_wrt_dt = np.dot(evo_mat, M_t)
    return dMt_wrt_dt


# Arranging the data into x, y, z arrays
def make_data_array(func, num_frames):
    global M0, dt
    M = [M0, ]
    for i in range(1, num_frames):
        new_M = func((M[i-1]))*dt + M[i-1]
        M.append(new_M)
    return M


def make_rel_array(num_its):
    rel_array = []
    for i in range(num_its):
        rel_array.append(relaxation(i))
    return rel_array


