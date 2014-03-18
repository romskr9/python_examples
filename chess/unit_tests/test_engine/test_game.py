import unittest
import os, sys

sys.path.append('../..')
    
from engine.game import *

class TestGame(unittest.TestCase):
    
    def test_init(self):
        game = Game()
        self.assertSequenceEqual(game._history, [])

if __name__ == '__main__':
    unittest.main()
