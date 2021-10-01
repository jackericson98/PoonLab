from functions import *
import matplotlib.pyplot as plt
import numpy as np
from print2data import *


def make_y_data(decay_constant, num_points):
    y = [0]
    for i in range(num_points-1):
        y.append((decay_at_time([vol[0]], i, decay_constant))[0])
    return y


num_its = 10
x_data = np.linspace(0, 1, num_its)
y_data = add_noise(make_y_data(.2, len(x_data)))
print(x_data), print(y_data)
plt.scatter(x_data, y_data)
plt.show()

