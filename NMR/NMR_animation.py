import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

speed = 1
arrow_length = 1
theta_real = np.pi / 16
radius = np.sin(theta_real) / arrow_length
sphere_radius = arrow_length
n = 100 // speed  # NUMBER OF FRAMES


def get_arrow(phi):
    x = 0
    y = 0
    z = 0
    u = radius * np.sin(phi)
    v = radius * np.cos(phi)
    w = 0.5 * arrow_length
    return x, y, z, u, v, w


def rotation_x(angle):
    Rx = [[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]]
    return np.array(Rx)


def rotation_z(angle):
    Rz = [[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]]
    return np.array(Rz)


# Draw Sphere
def get_sphere(rot_angle):
    theta_construct = np.linspace(rot_angle, 2 * np.pi + rot_angle, 20)
    phi_construct = np.linspace(-theta_real, np.pi - theta_real, 10)
    phi_construct, theta_construct = np.meshgrid(phi_construct, theta_construct)
    x = 0.25 * sphere_radius * np.cos(theta_construct) * np.sin(phi_construct)
    y = 0.25 * sphere_radius * np.sin(theta_construct) * np.sin(phi_construct)
    z = 0.25 * sphere_radius * np.cos(phi_construct)
    return x, y, z


sphere = ax.plot_surface(*get_sphere(0))
quiver = ax.quiver(*get_arrow(0), normalize=True, pivot='tail', capstyle='butt')

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)


def update(phi):
    global quiver
    quiver.remove()
    quiver = ax.quiver(*get_arrow(phi))

    global sphere
    sphere.remove()
    sphere = ax.plot_surface(*get_sphere(-phi), color="b")


# Plot the animated rotating arrow
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, n), interval=0.0005)
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.axis('off')
plt.show()
