import numpy as np
import scipy as sp
import random


# Rotation Matrices
def rotation_x(angle):
    Rx = [[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]]
    return Rx


def rotation_y(angle):
    Ry = [[np.cos(angle), 0, np.sin(angle)], [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]]
    return Ry


def rotation_z(angle):
    Rz = [[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]]
    return Rz


def lin_func(x, m, b):
    y = m * x + b
    return y


def exp_func(x, a, b):
    y = a * np.exp(b * x)
    return y


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