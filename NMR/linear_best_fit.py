
"""This function creates random error exponential decay functions"""
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def rand_error(datapoint, percent):
    err_max = datapoint
    data_error = 2*(random.random()-0.5)*err_max
    return data_error


def error_data(old_data, percent):
    new_data = []
    for data_point in old_data:
        new_data_point = rand_error(data_point, percent)
        new_data.append(new_data_point)
    return new_data


def func(x, m, b):
    y = m*x + b
    return y

num_points = 100

xdata = np.linspace(0, 100, num_points)
ydata = error_data(xdata, 0.15)
popt, pcov = optimize.curve_fit(func, xdata, ydata)

print(popt)

slope = popt[0]
intercept = popt[1]
new_ydata = xdata*slope

plt.scatter(xdata, ydata)
plt.plot(xdata, new_ydata)

plt.show()

