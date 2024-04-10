"""
Tests for model.py.

Note that the unittest module predates PEP-8 guidelines, which
is why we have a bunch of names that don't comply with the
standard.
"""
import model
from model import Vec
import unittest
import sys

class TestScaffolding(unittest.TestCase):

    def test_to_from_list(self):
        """to_list and from_list should be inverse"""
        board = model.Board()
        as_list = [[0, 2, 2, 4], [2, 0, 2, 8], [8, 2, 2, 4], [4, 2, 2, 0]]
        board.from_list(as_list)
        self.assertEqual(board.to_list(), as_list)

    def test_from_to(self):
        """to_list and from_list should be inverse"""
        board = model.Board()
        board.place_tile()
        board.place_tile(value=32)
        board.place_tile()
        as_list = board.to_list()
        board.from_list(as_list)
        again = board.to_list()
        self.assertEqual(as_list, again)

if __name__ == "__main__":
    unittest.main()
