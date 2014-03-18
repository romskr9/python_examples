
class GameManager:
    """This serves for accessing of the singleton instance of the Game class."""

    _instance = None
    _managed_class = None
        
    @classmethod
    def instance(cls):
        if not cls._instance:
            cls._instance = cls._managed_class()
        return cls._instance
    
    @classmethod
    def new_game(cls):
        cls._instance = None

    @classmethod
    def set_managed_class(cls, managed_class):
        cls._managed_class = managed_class
