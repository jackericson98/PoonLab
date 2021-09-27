"""This file is used to create a best fit function for exponential decay functions and returns the decay constant"""
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from statsmodels.regression.quantile_regression import QuantReg


def rand_error(datapoint):
    err_max = datapoint
    data_error = 2 * (random.random() - 0.5) * err_max
    return data_error


def error_data(old_data, percent):
    new_data = []
    for data_point in old_data:
        new_data_point = data_point + rand_error(data_point) * percent
        new_data.append(new_data_point)
    return new_data


def lin_func(x, m, b):
    y = m * x + b
    return y


def exp_func(x, a, b):
    y = a * np.exp(b * x)
    return y


num_points = 100

x_data = np.linspace(0, 100, num_points)
y_data = lin_func(x_data, 2, 4)
lin_data, p_cov = optimize.curve_fit(lin_func, x_data, y_data)


slope = lin_data[0]
intercept = lin_data[1]
new_y_data = x_data * slope + intercept

plt.scatter(x_data, y_data, )
plt.plot(x_data, new_y_data, color='red')

plt.show()
