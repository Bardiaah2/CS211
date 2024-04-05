"""
The game state and logic (model component) of 512,
a game based on 2048 with a few changes.
This is the 'model' part of the model-view-controller
construction plan.  It must NOT depend on any
particular view component, but it produces event
notifications to trigger view updates.
"""

from game_element import GameElement, GameEvent, EventKind
from typing import List, Tuple, Optional
import random

# Configuration constants
GRID_SIZE = 4

class Vec():
    """A Vec is an (x,y) or (row, column) pair that
    represents distance along two orthogonal axes.
    Interpreted as a position, a Vec represents
    distance from (0,0).  Interpreted as movement,
    it represents distance from another position.
    Thus we can add two Vecs to get a Vec.
    """
    #Fixed:  We need a constructor, and __add__ method, and __eq__.
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, __value: 'Vec') -> 'Vec':
        return Vec(self.x + __value.x, self.y + __value.y)

    def __eq__(self, __value: 'Vec') -> bool:
        return (self.x == __value.x and self.y == __value.y)


class Tile(GameElement):
    """A slidy numbered thing."""

    def __init__(self):
        super().__init__()


class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self):
        super().__init__()
        self.tiles = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]  # FIXed: a grid holds a matrix of tiles

    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        for row in self.tiles:
            for tile in row:
                if not tile:
                    return True

        return False
        # FIXed: Should return True if there is some element with value None

    def place_tile(self):
        """Place a tile on a randomly chosen empty square."""
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        self.tiles[y][x] = Tile()
        #FIXed

    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        return 0
        #FIXME
