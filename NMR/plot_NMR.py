"""The point of this file is to be able to input your data and receive a plot"""


from print2data import *
import matplotlib.pyplot as plt


plt.title('Volume vs. Chemical Shift')
plt.ylabel('Volume of the Peak')
plt.xlabel('Hydrogen Chemical Shift')
plt.scatter(w1, vol, marker='x')
plt.show()