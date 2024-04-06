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

    def __init__(self, pos: Vec, value: int = 2):
        super().__init__()
        self.row = pos.y
        self.col = pos.x
        self.value = value


class Board(GameElement):
    """The game grid.  Inherits 'add_listener' and 'notify_all'
    methods from game_element.GameElement so that the game
    can be displayed graphically.
    """

    def __init__(self, rows=4, cols=4):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.tiles = [ ]
        for row in range(rows):
            row_tiles = [ ]
            for col in range(cols):
                row_tiles.append(None)
            self.tiles.append(row_tiles) # FIXed: a grid holds a matrix of tiles

    def __getitem__(self, pos: Vec) -> Tile:
        return self.tiles[pos.x][pos.y]

    def __setitem__(self, pos: Vec, tile: Tile):
        self.tiles[pos.y][pos.x] = tile

    def has_empty(self) -> bool:
        """Is there at least one grid element without a tile?"""
        for row in self.tiles:
            for tile in row:
                if not tile:
                    return True

        return False
        # FIXed: Should return True if there is some element with value None

    def _empty_positions(self) -> List[Vec]:
        empty = []
        for row in range(len(self.tiles)):
                for col in range(self.cols):

                    if not self.tiles[row][col]:
                        empty.append(Vec(col, row))
        return empty

    def place_tile(self, value: None | int = None):
        """Place a tile on a randomly chosen empty square."""
        empty = self._empty_positions()
        assert len(empty) > 0
        pos = random.choice(empty)
        if not value:
            if random.random() < 0.1:
                self[pos] = Tile(pos, 4)
                return
        self[pos] = Tile(pos)
        #FIXed

    def score(self) -> int:
        """Calculate a score from the board.
        (Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        return 0
        #FIXME

    def from_list(self, values: List[List[int]]) -> 'Board':
        result = Board(len(values), len(values[0]))
        for row in range(result.rows):
            for col in range(result.cols):
                if not values[row][col]:
                    result[Vec(row, col)] = Tile(values[row][col])
        
        return result
    
    def in_bounds(self, pos: Vec) -> bool:
        return (self.rows >= pos.x and self.y >= pos.y)

