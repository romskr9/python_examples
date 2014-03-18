from engine.figures.figures import *
from engine.common import Common

class Board:
    """This class encapsulates the game board."""
    
    #figures of the 1st and the 8th line (left to right)
    initial_figures = [
                       Rook, Knight, Bishop,
                       Queen, King,
                       Bishop, Knight, Rook
                       ]

    def __init__(self, game, board = None):
        self.board = board or self._create_initial_board(game)
    
    @staticmethod
    def create_empty_board(game, size = Common.board_size ** 2):
        """Empty game board is used also for testing purposes."""
        board = [None for _ in range(size)]
        return Board(game, board) 
        
    def _create_initial_board(self, game):
        """Create an initial board according the chess game rules."""
        white_figures = [figure(Common.white, game) for figure in self.initial_figures]
        black_figures = [figure(Common.black, game) for figure in self.initial_figures]
        white_pawns = [Pawn(Common.white, game) for _ in range(Common.board_size)]
        black_pawns = [Pawn(Common.black, game) for _ in range(Common.board_size)]
        empty = self.create_empty_board(game, Common.board_size ** 2 // 2).board
        return white_figures + white_pawns + empty + black_pawns + black_figures
