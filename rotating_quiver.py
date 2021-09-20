import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

speed = 2
arrow_z_component = 4
radius = 1
n = 100 // speed  # NUMBER OF FRAMES


def get_arrow(theta):
    x = -radius * np.sin(theta)
    y = -radius * np.cos(theta)
    z = np.linspace(-0.5 * arrow_z_component, -0.5 * arrow_z_component, n)
    u = 2 * radius * np.sin(theta)
    v = 2 * radius * np.cos(theta)
    w = arrow_z_component
    return x, y, z, u, v, w


# draw sphere
u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

quiver = ax.quiver(*get_arrow(0), normalize=True, pivot='middle')

ax.set_xlim(-1.5 * radius, 1.5 * radius)
ax.set_ylim(-1.5 * radius, 1.5 * radius)
ax.set_zlim(-0.75 * arrow_z_component, 0.75 * arrow_z_component)


def update(theta):
    global quiver
    quiver.remove()
    quiver = ax.quiver(*get_arrow(theta))


# Plot the trail of the arrow and the axes
numpoints = 100
twopi = np.linspace(0, 2 * np.pi, numpoints)
plt.plot(radius * np.cos(twopi), radius * np.sin(twopi),
         np.linspace(0.5 * arrow_z_component, 0.5 * arrow_z_component, numpoints))
plt.plot(-radius * np.cos(twopi), -radius * np.sin(twopi),
         np.linspace(-0.5 * arrow_z_component, -0.5 * arrow_z_component, numpoints))

# Plot the sphere
ax.plot_wireframe(x, y, z, color="r")

# Plot the animated rotating arrow
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, n), interval=0.0005)
plt.show()
