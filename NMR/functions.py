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


# Add noise function
def add_noise(input_data):
    noise = np.random.normal(12, 100, len(input_data))
    noise_data = np.add(input_data, noise)
    return noise_data


# Exponential decay function. Input an array of different data points, a decay constant and the iteration and it will
# return the specific decay value
def decay_at_time(vol_array, time, decay_constant):
    old_data = vol_array
    new_data = []
    for i in range(len(vol_array)):
        decay_value = np.exp(-time * decay_constant)
        new_point = old_data[i] * decay_value
        new_data.append(new_point)
    return new_data
