from PyQt4.QtCore import *

from engine.common import Common

class UICommons:

    #colors of the board and figures
    BLACK = 0xff000000
    WHITE = 0xffffffff
    WHITE_ARRAY = 0xff00ff00
    BLACK_ARRAY = 0xff800000
    
    image_width = 64
    image_height = 64
    
    image_size = QSize(image_width, image_height)
    
    WHITE_STR = "White"
    BLACK_STR = "Black"
    
    @staticmethod
    def game_position(position, color):
        """Evaluate position on the game from position on the board by regarding player's color"""
        direction = color * 2 - 1
        x, y = position % Common.board_size, position // Common.board_size
        return Common.reverse(x, direction) + Common.reverse(y, direction) * Common.board_size
