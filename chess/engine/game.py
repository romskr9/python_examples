from engine.game_move import GameMove
from engine.board import Board
from engine.common import Common
from engine.game_manager import GameManager

class GameMetaClass(type):
    """Metaclass is used for using the Game class in the GameManager as a singleton."""

    def __new__(cls, name, bases, attrs):
        game_class = type.__new__(cls, name, bases, attrs)
        GameManager.set_managed_class(game_class)
        return game_class
    
class Game(metaclass = GameMetaClass):
    """ This class represents a game as the history of moves
        and the engine for generation of moves.
    """

    def __init__(self):
        self._history = []
        self._initial_board = Board(self)
        self._board = self._initial_board
        
    def add_to_history(self, new_board):
        self._history.append(self._board)
        self._board = new_board
        
    def revert_from_history(self):
        if self._history:
            self._board = self._history[-1]
            self._history = self._history[:-1]

    def board(self):
        return self._board.board
    
    def players_move(self, move):
        if self._check_move(move) == 'OK':
            self._apply_move(move)
        
    def computers_move(self, color):
#         status, move = self._find_best_move(color, Common.initial_deep)
#         if status == 'OK':
#             self._apply_move(move)
        pass
    
    def _apply_move(self, move):
        source, _, _ = move
        figure = self.board()[source]
        if figure:
            figure.apply_move(move)
    
    def _check_move(self, move):
        return 'OK'     #TODO
    
    def _find_best_move(self, color, deep):
#         possible_moves = []
#         for figure in self.board():
#             if figure and figure.color == color:
#                 possible_moves += figure.find_possible_moves()
#         best_move = None
#         for move in possible_moves:
#             status, score = self._try_move(move)
#             if not best_move or self._better_score(old_score, new_score, color):
#                 best_move = (move, status, score)
        pass    #TODO

    def _try_move(self, source, destination, changed_figure):
#         self._apply_move(source, destination, changed_figure)
        pass    #TODO