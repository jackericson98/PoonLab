import MDAnalysis as mda
import pandas as pd


class Analyze:
    def __init__(self):
        pass
    def load_traj(self, path2gro, path2xtc):
        self.universe = mda.Universe(path2gro, path2xtc)

    def analyze(self, listofparts, datapoints):
        self.data = pd.DataFrame()
        for part in listofparts:
            part(datapoints)

    def plot(self):


