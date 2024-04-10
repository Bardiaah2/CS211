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
        self.row = pos.x
        self.col = pos.y
        self.value = value

    def __eq__(self, __value: 'Tile') -> bool:
        if not isinstance(__value, Tile):
            return False
        return self.value == __value.value
    
    def move_to(self, new_pos: Vec):
        self.row = new_pos.x
        self.col = new_pos.y
        self.notify_all(GameEvent(EventKind.tile_updated, self))

    def merge(self, other: "Tile"):
        # This tile incorporates the value of the other tile
        self.value = self.value + other.value
        self.notify_all(GameEvent(EventKind.tile_updated, self))
        # The other tile has been absorbed.  Resistance was futile.
        other.notify_all(GameEvent(EventKind.tile_removed, other))


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
        if self.in_bounds(pos):
            return self.tiles[pos.x][pos.y]
        else:
            return None

    def __setitem__(self, pos: Vec, tile: Tile):
        self.tiles[pos.x][pos.y] = tile

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
                        empty.append(Vec(row, col))
        return empty

    def place_tile(self, value: None | int = None):
        """Place a tile on a randomly chosen empty square."""
        empty = self._empty_positions()
        assert len(empty) > 0
        pos = random.choice(empty)
        if not value:
            if random.random() < 0.1:
                new_tile = Tile(pos, 4)
                self[pos] = new_tile
                self.notify_all(GameEvent(EventKind.tile_created, new_tile))
                return
        new_tile = Tile(pos)
        self[pos] = new_tile
        self.notify_all(GameEvent(EventKind.tile_created, new_tile))
        #FIXed

    def score(self) -> int:
        """Calculate a score from the board.
        Differs from classic 1024, which calculates score
        based on sequence of moves rather than state of
        board.
        """
        tiles_val = [sum(i) for i in self.to_list()]
        return sum(tiles_val)
        #FIXed

    def to_list(self) -> List[List[int]]:
        """Test scaffolding: represent each Tile by its
        integer value and empty positions as 0
        """
        result = [ ]
        for row in self.tiles:
            row_values = []
            for col in row:
                if col is None:
                    row_values.append(0)
                else:
                    row_values.append(col.value)
            result.append(row_values)
        return result

    def from_list(self, values: List[List[int]]):
        self.__init__(len(values), len(values[0]))
        for row in range(self.rows):
            for col in range(self.cols):
                if values[row][col]:
                    self[Vec(row, col)] = Tile(Vec(row, col), values[row][col])

        return self
        
    
    def in_bounds(self, pos: Vec) -> bool:
        return (self.rows > pos.x >= 0 and self.cols > pos.y >= 0)
    
    def slide(self, pos: Vec,  dir: Vec):
        """Slide tile at row,col (if any)
        in direction (dx,dy) until it bumps into
        another tile or the edge of the board.
        """
        if self[pos] is None:
            return
        while True:
            new_pos = pos + dir
            if not self.in_bounds(new_pos):
                break
            if self[new_pos] is None:
                self._move_tile(pos, new_pos)
            elif self[pos] == self[new_pos]:
                self[pos].merge(self[new_pos])
                self._move_tile(pos, new_pos)
                break  # Stop moving when we merge with another tile
            else:
                # Stuck against another tile
                break
            pos = new_pos

    def _move_tile(self, old_pos: Vec, new_pos: Vec):
        if self[old_pos] is None:
            return
        self[old_pos].move_to(new_pos)
        self[new_pos] = self[old_pos]
        self[old_pos] = None

    def left(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                self.slide(Vec(row, col), Vec(0, -1))
    
    def right(self):
        for row in range(0, self.rows):
            for col in range(self.cols - 1, -1, -1):
                self.slide(Vec(row, col), Vec(0, 1))
    
    def down(self):
        for row in range(self.rows - 1, -1, -1):
            for col in range(0, self.cols):
                self.slide(Vec(row, col), Vec(1, 0))
    
    def up(self):
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                self.slide(Vec(row, col), Vec(-1, 0))
    
    