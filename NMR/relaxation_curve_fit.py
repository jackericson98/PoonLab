import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import random as rd
from print2data import *
import numpy as np
from matplotlib.animation import FuncAnimation

"""This file takes in consecutive frames of full spectra of 2D NMR data and returns relaxation constants for each 
residue. The Test_data class can be used to produce test data for fitting and animation"""


class Test_data:

    """Creates an exponential decay data set with random noise"""

    def __init__(self, x_max=1, num_frames=32, decay_constant=[-10], noise=0.05, y0=1, vol_data=np.linspace(1, 1, 100)):
        self.decay_constant = decay_constant
        self.x_test = np.linspace(.01, x_max, num_frames)
        self.y_test = []
        self.noise = noise
        self.y0 = y0
        self.df = []
        self.vol_data = vol_data

    def make_y_data(self, y0):

        """Make decay data from given an x range and and a decay constant"""

        decay_constant = self.decay_constant
        x_test = self.x_test
        self.y_test = y0 * np.exp(x_test * decay_constant)
        return self.y_test

    def make_noise_data(self, y0):

        """For each value in our test data array add a random amount of noise given by noise var"""

        input_data = self.make_y_data(y0)
        noise = self.noise
        noise_array = np.abs(np.random.normal(0, noise, len(input_data)))
        self.y_test = np.add(input_data, noise_array)
        return self.y_test

    def make_data_frame(self):  # Bug where this only returns the last array of the data frame

        """returns a data frame of test values each with unique relaxation constants"""
        for peak in self.vol_data:
            self.decay_constant = -10 * rd.random()
            decay_storage.append(self.decay_constant)
            ds = self.make_noise_data(peak)
            self.df.append(ds)

        jint = self.df
        return print(jint)

    def __str__(self):
        return str(self.y_test)

# ----------------------------- Curve Fitting ---------------------------


# Create an exponential function
def exp_func(x, a, b, c):
    func = a * np.exp(b * x) + c
    return func


# Create a curve fitting function
def exp_fit(x_vals, y_vals):
    a_guess = np.mean(y_vals)
    best_fit, _ = curve_fit(exp_func, x_vals, y_vals, p0=(a_guess, 0, 0), maxfev=500000)
    a, b, c = best_fit[0], best_fit[1], best_fit[2]
    y_fit = a * np.exp(x_vals * b) + c
    return y_fit, a, b, c


def multi_exp_fit(vol_data, x_max):
    """Takes a set of sets of data (ex: data = [dataset 1, ... , dataset n], dataset1 = [(1 x num steps) volume data]
    and returns an array of relaxation rates for each peak"""
    x_array = np.linspace(0, x_max, len(vol_data[0]))  # Array of time stamps for relaxation fitting
    relaxation_data = []
    for point in vol_data:  # For each data point record relaxation constant
        cum = exp_fit(x_array, point)[2]
        relaxation_data.append(cum)
    return relaxation_data


# # create datasets
df = []
decay_storage = []
y0_array = vol
x_end = 2

for i in y0_array:
    decay = -10 * rd.random()
    decay_storage.append(decay)
    ds = Test_data(x_max=x_end, decay_constant=decay, y0=i)
    ds1 = ds.make_noise_data(i)
    df.append(ds1)
print(df[1])
relax_vals = multi_exp_fit(df, x_end)

# ------------------- Plotting ---------------------
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))


vol_data = ax.scatter(w1, w2, vol)


def update(frame):

    global vol_data, df
    vol_data.remove()
    print(frame)
    ax.scatter(w1, w2, df[:][frame:frame+1])


ani = FuncAnimation(fig, update, frames=32)


plt.show()







# Create single test data sets

# y = Test_data()
# y_data = y.make_noise_data()
# x_data = y.x_test
# y_fitted = exp_fit(x_data, y_data)

# Plot single data set against it's best fit line

# ax = plt.gca()
# plt.title("Best fit for exponential decay data")
# plt.xlabel("Time")
# plt.ylabel("Data")
# ax.text(0.5, 0.75, "Relaxation Constant = %.2f" % y_fitted[2],
#         horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
# plt.scatter(x_data, y_data, color='blue')  # Noisy data
# plt.plot(x_data, y_fitted[0], color='red')  # Fitted data
# plt.show()



