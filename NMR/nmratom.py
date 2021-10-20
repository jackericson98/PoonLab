import numpy as np


class NMRAtom:
    """Class for processing the response of an atom (1H, 13C, 15N) in different possible states of an NMR environment.
    The larmor function works as the initial state for other functions, since it represents the state of an unperturbed
    atomic nuclei in the presence of a static magnetic field."""

    def __init__(self, initM, atom='h', T1=120, T2=80, B_0=14):  #T1, T2 measured in , B_0 measured in Tesla

        self.mag_vec = initM
        self.phi = np.arctan(np.sqrt(initM[0] ** 2 + initM[1] ** 2) / initM[2])
        self.T1 = T1
        self.T2 = T2
        self.B_0 = B_0

        if atom == 'Hydrogen' or 'hydrogen' or 'H' or 'h':
            self.atom = [1, 4257.7, 1 / 2, 2.79]  # amu, Hz/G, nuclear magnetons
        elif atom == 'Carbon' or 'carbon' or 'c' or 'C':
            self.atom = [13, 1070.5, 1 / 2, 0.70]  # amu, Hz/G, nuclear magnetons
        elif atom == 'Nitrogen' or 'nitrogen' or 'N' or 'n':
            self.atom = [15, -431.6, 1 / 2, -0.28]  # amu, Hz/G, nuclear magnetons

    def larmor(self, t):

        """Larmor precession of an atom in a magnetic field. Takes in a time returns a vector"""

        M = self.mag_vec
        phi = self.phi
        gyro = self.atom[1]
        mag_mom = self.atom[3]
        w_0 = -self.B_0 * gyro  # Hz

        M[0] = mag_mom * np.sin(phi) * np.cos(w_0 * t)
        M[1] = mag_mom * np.sin(phi) * np.sin(w_0 * t)
        M[2] = mag_mom * np.cos(phi)

        return M

    def relaxation(self, t):

        """Motion of an atom starting from a perturbed state (initM) to its relaxed state"""

        M = self.mag_vec
        M0 = self.larmor(t)

        M[0] = M0[0] * np.exp(-t / self.T2)
        M[1] = M0[1] * np.exp(-t / self.T2)
        M[2] = M0[2] * (1 - np.exp(-t / self.T1))

        return M

    def bloch_eq(self, dt=1e-6):

        """Time step of motion of an atom in a perturbed state toward relaxed state"""

        M = self.mag_vec
        B = [0, 0, self.B_0]
        gamma = 1

        dMxdt = (-1 / self.T2) * M[0] + (gamma * B[2]) * M[1] + (-gamma * B[1]) * M[2]
        dMydt = (-gamma * B[2]) * M[0] + (-1 / self.T2) * M[1] + (gamma * B[0]) * M[2]
        dMzdt = (gamma * B[1]) * M[0] + (-gamma * B[0]) * M[1] + (-1 / self.T1) * M[2]

        return dMxdt * dt, dMydt * dt, dMzdt * dt

    def perturbation(self, t, phase=0):
        B_0 = self.B_0
        B1 = 1
        wrf = 1
        B_rf = [B1 * np.cos(wrf * t + phase), B1 * np.sin(wrf * t + phase), 0]
        return B_rf
