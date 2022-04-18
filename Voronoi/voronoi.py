import numpy as np


# Atom class to define atom elements
class Atom:
    # Initiate atoms with radius, location, neighbors and shape variables
    def __init__(self, radius, location):

        self.rad = radius
        self.loc = location
        self.neighbors = []
        self.edges = []


# Mesh class to house math methods
class Mesh:
    # Initiate the mesh with a base sphere and list of atoms
    def __init__(self):
        self.base_sphere = Atom(1, (0, 0, 0))
        self.atom_list = []

    # Method for retrieving the magnitude and direction of a ray from one atom to another
    def get_ray(self, a1, a2):
        # Calculate the magnitude
        mag = np.sqrt((a1.loc[0] - a2.loc[0]) ** 2 +
                      (a1.loc[1] - a2.loc[1]) ** 2 +
                      (a1.loc[2] - a2.loc[2]) ** 2)
        # Calculate the direction
        direction = [(a1.loc[0] - a2.loc[0]) / mag,
                     (a1.loc[0] - a2.loc[0]) / mag,
                     (a1.loc[0] - a2.loc[0]) / mag]
        return mag, direction

    def build_grid(self):
        self.find_neighbors()

    # Method to build neighbor list for each atom
    def find_neighbors(self):
        # Go through each atom in our atom list
        for i in range(len(self.atom_list)):
            # Set atom variable
            atom = self.atom_list[i]
            # Go through all other atoms
            for j in range(len(self.atom_list)):
                # set neighbor variable
                neighbor = self.atom_list[j]
                # Get the distance between atom and the neighbor
                mag, direction = self.get_ray(atom, neighbor)
                # If atom and neighbor are different and their radii overlap, add neighbor to neighbors and add the
                # plane to the edge list of each atom
                if i != j and mag < atom.rad + neighbor.rad:
                    # Place the plane halfway between the atoms and set it's normal direction to the direction of the
                    # ray between the atoms
                    my_plane = [[atom.loc + direction*mag/2], [direction]]
                    atom.edges.append(my_plane)
                    atom.neighbors.append(j)

            #
            for neighbor in atom.neighbors:

                atom.shape = []


atom0 = Atom(2, (1, 1, 1))
atom1 = Atom(2, (1, 2, 3))


myMesh = Mesh()
myMesh.atom_list.append(atom0)
myMesh.atom_list.append(atom1)
myMesh.build_grid()
print(atom0.neighbors, atom1.neighbors)