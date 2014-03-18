import unittest
import os, sys

sys.path.append('../..')
    
from engine.figures.figures import *
from engine.figures.figure import *
from engine.board import *
from engine.game import *
from engine.common import Common
from engine.game_manager import GameManager

class TestFigure(unittest.TestCase):
    
    def test_figure_name(self):
        pawn = Pawn(Common.black, None)
        self.assertEqual(pawn.get_name(), 'pawn')
        
    def test_figure_register(self):
        
        #There are 6 different figures in the game.
        self.assertEqual(len(FigureRegister.registered()), 6)
        self.assertEqual(Pawn.get_name(), "pawn")
        self.assertEqual(Pawn.get_type(), Pawn)

    def test_apply_move(self):
        
        #an empty game
        game = GameManager.instance()
        game._board = Board.create_empty_board(game)
        game.board()[0] = Bishop(Common.white, game)
        self.assertEqual(game.board()[0].get_type(), Bishop)
        self.assertIsNone(game.board()[Common.board_size * 2 - 1])
        game.board()[0].apply_move((0, Common.board_size * 2 - 1, None))
        self.assertEqual(game.board()[Common.board_size * 2 - 1].get_type(), Bishop)
        self.assertIsNone(game.board()[0])
        
    
if __name__ == '__main__':
    unittest.main()
