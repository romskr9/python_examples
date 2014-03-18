from engine.game_manager import GameManager

class FigureRegister:
    """All descendant classes of the Figure are registered here."""
    
    _register = []
    
    @classmethod
    def register(cls, item):
        if item not in cls.registered():
            cls._register.append(item)
            
    @classmethod
    def registered(cls):
        return cls._register

class FigureMetaClass(type):
    """This meta-class registers all descendants of the Figure base."""
    
    def __new__(cls, name, bases, attrs):
        result = type.__new__(cls, name, bases, attrs)
        if bases:
            FigureRegister.register(result)
        return result

class Figure(metaclass = FigureMetaClass):
    """"A common base for all figures"""
    
    def __init__(self, color, game):
        self.color = color
        
    @classmethod
    def get_name(cls):
        return cls.__name__.lower()
    
    @classmethod
    def get_type(cls):
        return cls
    
    @staticmethod
    def apply_move(move):
        """Common move of all figures, but rooks and pawns, which may have special behavior."""
        game = GameManager.instance()
        source, destination, _ = move
        game.board()[destination] = game.board()[source]
        game.board()[source] = None
