# Game class - handles logic of entire game

from numpy import ndarray, empty

class Game:
    def __init__(
        self, board_size: tuple = None, players: int = None, bases: list = None
    ):
        """
        Game class handling logic and class interactions.

        Parameters
        ----------
        board_size : tuple, optional; default=(12, 12)
            Size of board x, y
        players : int, optional; default=2
            # of players
        bases : list, optional; default=[[0,0], [board_size[0], board_size[1]]]
            Position of starting bases for bases[n] nth player
        """
        self.board_size = board_size if board_size else (12, 12)
        self.players = players if players else 2
        self.bases = bases if bases else [[0, 0], [board_size[0], board_size[1]]]
        
