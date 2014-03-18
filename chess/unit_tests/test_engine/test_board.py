import unittest
import os, sys

sys.path.append('../..')
    
from engine.board import Board
from engine.figures.figures import *
from engine.common import Common

class TestBoard(unittest.TestCase):
    
    def test_init(self):
        board = Board(None)
        self.assertEqual(len(board.board), Common.board_size ** 2)
        self.assertIsInstance(board.board[0], Rook)
        self.assertIsInstance(board.board[7 * Common.board_size + 6], Knight)
        self.assertIsInstance(board.board[6 * Common.board_size + 7], Pawn)
        self.assertEqual(board.board[6 * Common.board_size + 7].color, Common.black)

    def test_empty_board(self):
        board = Board.create_empty_board(None)
        self.assertEqual(len(board.board), Common.board_size ** 2)
        for field in board.board:
            self.assertIsNone(field)

if __name__ == '__main__':
    unittest.main()
