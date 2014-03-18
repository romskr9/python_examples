class Common:
    """Common definition of the chess game"""
    
    board_size = 8
    
    black = 0
    white = 1
    
    initial_deep = 2
    
    @classmethod
    def reverse(cls, i, direction):
        """If direction = -1, reverse numbers 0..7 to 7..0"""
        return ((i + 1) * direction) % (cls.board_size + 1) - 1
