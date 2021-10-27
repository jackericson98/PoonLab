
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import random as rd
from translate_Poky import Translate_Poky
import numpy as np
from matplotlib.animation import FuncAnimation
from POKY_string_data import *

"""This file takes in consecutive frames of full spectra of 2D NMR data and returns relaxation constants for each 
residue. The Test_data class can be used to produce test data for fitting and animation"""

data = Translate_Poky(data2)
vol = data.vol()
w1, w2 = data.chem_shift()
lw1, lw2 = data.line_width()
rms = data.rms()


# ------------------------------- Test Data ---------------------------------------
class Test_data:
    """Creates an exponential decay data set with random noise"""

    def __init__(self, decay_time=1, num_frames=64, decay_constant=-10, noise=0.05, y0=1):
        self.decay_constant = decay_constant
        self.x_test = np.linspace(.01, decay_time, num_frames)
        self.y_test = []
        self.noise = noise
        self.y0 = y0
        self.df = []

    def make_y_data(self, y0, decay_constant):
        """Make decay data from given an x range and and a decay constant"""

        x_test = self.x_test
        self.y_test = y0 * np.exp(x_test * decay_constant)
        return self.y_test

    def make_noise_data(self, y0, decay_constant):
        """For each value in our test data array add a random amount of noise given by noise var"""

        input_data = self.make_y_data(y0, decay_constant)
        noise = self.noise
        noise_array = np.abs(np.random.normal(0, noise, len(input_data)))
        self.y_test = np.add(input_data, noise_array)
        return self.y_test

    def make_data_frame(self, vol_data=np.linspace(1, 1, 100)):
        """Creates a data frame of test values each with unique relaxation constants"""

        decay_storage = []

        for peak in vol_data:
            decay_constant = -10 * rd.random()
            decay_storage.append(decay_constant)
            ds = self.make_noise_data(peak, decay_constant)
            self.df.append(ds)
        return self.df

    def __str__(self):
        return str(self.y_test)


# ----------------------------- Curve Fitting ---------------------------

# Create an exponential function
def exp_func(x, a, b, c):
    func = a * np.exp(b * x) + c
    return func


# Create a curve fitting function
def exp_fit(x_values, y_values):
    """Single exponential fit function"""

    best_fit, _ = curve_fit(exp_func, x_values, y_values, p0=(1e+9, -5, 0), maxfev=50000)
    a, b, c = best_fit[0], best_fit[1], best_fit[2]
    y_fit = a * np.exp(x_values * b) + c
    return y_fit, a, b, c


def multi_exp_fit(vol_data, x_max):
    """Takes a full spectrum of relaxation data and returns an array of relaxation rates for each peak"""

    x_array = np.linspace(0, x_max, len(vol_data[0]))  # Array of time stamps for relaxation fitting
    a_array = []
    b_array = []
    c_array = []

    for point in vol_data:  # For each data point record relaxation constant

        decay_fit = exp_fit(x_array, point)
        a_array.append(decay_fit[1])
        b_array.append(decay_fit[2])
        c_array.append(decay_fit[3])

    return b_array


# ------------------------------ Make our test data -------------------------

df = Test_data(decay_time=50).make_data_frame(vol)  # This would be the data we import

fits = multi_exp_fit(df, 5)  # Get an array of fits


# ------------------------------ Plotting ------------------------------------
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))


vol_plot = ax.scatter(w1, w2, vol, color='blue')


def update(frame):
    global vol_plot, df
    vol_plot.remove()
    new_df = []
    for element in df:
        new_df.append(element[frame])
    vol_plot = ax.scatter(w1, w2, new_df, color='blue')


ani = FuncAnimation(fig, update, frames=32)

ax.set_xlabel('Hydrogen Chemical Shift (ppm)')
ax.set_ylabel('Nitrogen Chemical Shift (ppm)')
ax.set_zlabel('Intensity')
ax.set_title('HSQC Relaxation')
z_max = np.max(vol)
ax.set_zlim(0, z_max)
plt.show()


# Create single test data sets
#
# y = Test_data(decay_constant=-1.55)
# y_data = y.make_noise_data(vol[0])
# x_data = y.x_test
# y_fitted = exp_fit(x_data, y_data)
#
# # Plot single data set against it's best fit line
#
# ax = plt.gca()
# plt.title("Best fit for exponential decay data")
# plt.xlabel("Time")
# plt.ylabel("Data")
# ax.text(0.5, 0.75, "Relaxation Constant = %.2f" % y_fitted[2],
#         horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
# plt.scatter(x_data, y_data, color='blue')  # Noisy data
# plt.plot(x_data, y_fitted[0], color='red')  # Fitted data
# plt.show()
