# Board class for game. Objects in this Board() object represent units and terrain.
# Unnecessary TODO? vectorize getting a range for access to x-wise and y-wise strips.
# Won't need it unless we go into continuous float-Terrain() coordinates, really.

from terrain import Terrain

class Board():
    
    def __init__(self, size:tuple, default_terrain: object, terrain_objects: object=None):
        """
        Board class for units and terrain to be represented.

        Parameters
        ----------
        size : tuple
            x, y size of Board().
        default_terrain : object
            Terrain() object to fill unspecified terrain objects.
        terrain_objects : list[list]
            Specified list of lists of Terrain()/None where jth list's ith object represents x, yth position on the Board(). 
        """        
        self.size = size
        self.default_terrain = default_terrain
        self.terrain_objects = terrain_objects if terrain_objects else None

        self.board = [[self.default_terrain for x in range(size[0])] for y in range(size[1])]

    def __str__(self):
        """String representation of this Terrain() class."""
        build_me = "\n".join(" ".join(str(terra) for terra in row) for row in self.board)
        return build_me


# Testing
if __name__ == "__main__":
    bod = Board((12, 12), Terrain("X", 2))
    print(bod)