import numpy as np
"""I want this to simulate what happens to an atomic nucleus in an NMR machine with an input pulse sequence.
We are currently assuming that all atoms precess around the +z axis and the pulse comes from the +x direction"""

time = 0 # Running time
pulse_sequence = [[1, 1, 500], [1, 0, 0], [1, 0.5, 600], [5, 0, 0]]  # Pulse sequence [[Time, Intensity, Frequency]].
T = np.sum(pulse_sequence, axis=0)[0]  # Total time for the experiment
omega = w0 - wrf
w1 = -gamma * B1
theta = np.arctan((w1/omega))
alpha = -gamma*B1*tau_p/np.sin(theta)  # page 11

class atom:

    def __init__(self, atom, pulse_sequence):
        self.bmom = []  # Holds the magnetic moment of the atom while it goes through the pulse sequence
        self.atom = atom
        self.pulse_sequence = pulse_sequence

    def relaxation(self, time, alpha):
        """Given an alpha and a current time this returns a magnetization vector for the atom"""
        M0 = np.linalg.norm(self.atom[3])  # Magnitude of the magnetization vector of the atom
        Mx = M0 * np.sin(alpha) * np.cos(omega * time) * np.exp(-R2 * time)
        My = M0 * np.sin(alpha) * np.sin(omega * time) * np.exp(-R2 * time)
        self.bmom = [Mx, My]
        return self.bmom

    def get_alpha(self, pulse):
        gamma = self.atom[1]
        B1 = B0 * np.cos(theta)
        w0 = gamma * B0
        tao_p = pulse[0]
        alpha = -gamma*B1*tao_p/np.sin(theta)

    def run_nmr(self):
        for pulse in self.pulse_sequence:
            alpha = self.get_alpha(pulse)
            self.relaxation()
