# Terrain() class

class Terrain:

    def __init__(self, name:str, move_cost:int, effects:list=None):
        """
        Terrain() class representing movement cost of ground and its effects.

        Parameters
        ----------
        move_cost : int
            Movement cost of a unit to enter this area.
        effects : list, optional
            Special effects of this terrain.
        """
        self.name = name
        self.move_cost = move_cost
        self.effects = effects if effects else []

    def __str__(self):
        """String representatin of this Terrain()"""
        return self.name

    def get_cost(self):
        return self.move_cost

    def get_effects(self):
        return self.effects