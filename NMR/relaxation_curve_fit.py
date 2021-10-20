import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

"""This file creates an exponential decay function, adds random noise and then fits a line of best fit to the noise. 
Will eventually be repurposed to be applied to NMR relaxation data to return values for T1 and T2, which can then be 
plotted and shown as an animation in full_spectrum_relaxation_animation.py"""


class Test_data:

    """Creates an exponential decay data set with random noise"""

    def __init__(self, x_test=np.linspace(0.1, 1.1, 100), decay_constant=-10, noise=0.05):
        self.decay_constant = decay_constant
        self.x_test = x_test
        self.y_test = []
        self.noise = noise

    def make_y_data(self):

        """Make decay data from given an x range and and a decay constant"""

        decay_constant = self.decay_constant
        x_test = self.x_test
        self.y_test = np.exp(x_test * decay_constant)
        return self.y_test

    def make_noise_data(self):

        """For each value in our test data array add a random amount of noise given by noise var"""

        input_data = self.make_y_data()
        noise = self.noise
        noise_array = np.abs(np.random.normal(0, noise, len(input_data)))
        self.y_test = np.add(input_data, noise_array)
        return self.y_test

    def __str__(self):
        return str(self.y_test)

# ----------------------------- Curve Fitting ---------------------------


# Create an exponential function
def exp_func(x, a, b, c):
    y = a * np.exp(b * x) + c
    return y


# Create a curve fitting function
def exp_fit(x_vals, y_vals):
    best_fit, _ = curve_fit(exp_func, x_vals, y_vals, p0=(0, 0, 0), maxfev=500000)
    a, b, c = best_fit[0], best_fit[1], best_fit[2]
    y_fit = a * np.exp(x_vals * b) + c
    return y_fit, a, b, c


def multi_exp_fit(data, time_step):
    """Takes a set of sets of data (ex: data = [dataset1, ... , datasetn], dataset1 = [xdata, ydata, volumedata] at time
    t) and returns an array of relaxation times for each peak"""
    time_step_array = np.arrange(0, time_step*len(data), time_step)  # Array of time stamps for relaxation fitting
    relaxation_data = []
    for i in range(data[0, :]):  # For each data point record relaxation constant
        relaxation_data.append(exp_fit(time_step_array, (data[:, 2, i]))[2])
    return relaxation_data


# Create our test data sets
x_data = np.linspace(0.1, 1.1, 100)
y_data = Test_data(x_data).make_noise_data()
y_fitted = exp_fit(x_data, y_data)

# ------------------- Plotting ---------------------

ax = plt.gca()
plt.title("Best fit for exponential decay data")
plt.xlabel("Time")
plt.ylabel("Data")
ax.text(0.5, 0.75, "Relaxation Constant = %.2f" % y_fitted[2],
        horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
plt.scatter(x_data, y_data, color='blue')  # Noisy data
plt.plot(x_data, y_fitted[0], color='red')  # Fitted data
plt.show()
