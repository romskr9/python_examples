from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_commons import UICommons

from engine.common import Common

class PictureButton(QAbstractButton):
    """This class encapsulates graphical manipulation of one chess array field"""
    
    def __init__(self, parent, position):
        super(PictureButton, self).__init__(parent)
        self._parent = parent
        self._border = False
        self.position = position

    def paintEvent(self, event):
        
        """Redraw the field array regarding the figure and color."""
        painter = QPainter(self)
        
        #Coordinates of [0, 0] are on the left bottom corner here
        game_position = UICommons.game_position(self.position, self._parent._players_color())
        board_color = (self.position + (self.position // Common.board_size) % 2) % 2
        
        figure = self._parent.game.board()[game_position]
        if figure:
            figure_type = figure.get_type()
            index = figure.color + 2 * board_color
            painter.drawPixmap(event.rect(), self._parent.images.figures[figure_type][index])
        else:
            painter.drawPixmap(event.rect(), self._parent.images.empty[board_color])
        if self._parent.selected == game_position:
            self._draw_border()
            
    def _draw_border(self):
        
        """Draw a border around a field actually selected."""
        painter = QPainter(self)
        width = self.size().width() - 1
        painter.setPen(Qt.cyan)
        painter.drawLine(0, 0, 0, width)
        painter.drawLine(0, width, width, width)
        painter.drawLine(width, width, width, 0)
        painter.drawLine(width, 0, 0, 0)
        
    def sizeHint(self):
        return UICommons.image_size

