from functions import *
import matplotlib.pyplot as plt
import numpy as np
from print2data import *
from scipy.optimize import curve_fit


def make_y_data(decay_constant, num_points):
    y = []
    for i in range(num_points):
        y.append((decay_at_time([vol[0]], i, decay_constant))[0])
    return y


num_its = 100
x_data = np.linspace(0.1, 1.1, num_its)
y_data = add_noise(make_y_data(.08, len(x_data)))
# y_data = add_noise(3.4 * np.exp(-2 * x_data) + 4)
best_fit, _ = curve_fit(exp_func, x_data, y_data, maxfev=5000)
a, b, c = best_fit[0], best_fit[1], best_fit[2]
y_fit = a * np.exp(x_data * b) + c
ax = plt.gca()
ax.text(0.5, 0.75, "Relaxation Constant = %.2f" % b, horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
plt.scatter(x_data, y_data)
plt.plot(x_data, y_fit)
plt.show()
