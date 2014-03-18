from PyQt4.QtGui import *
from PyQt4.QtCore import *

from ui_commons import UICommons

from engine.figures.figure import FigureRegister 

class Images:
    
    def __init__(self):
        self._init_images()
    
    def _init_images(self):
        self.figures = {}
        for figure in FigureRegister.registered():
            self._init_figure(figure)
            
        #initialize empty arrays
        white_array = QPixmap(UICommons.image_size)
        white_array.fill(QColor(UICommons.WHITE_ARRAY))
        black_array = QPixmap(UICommons.image_size)
        black_array.fill(QColor(UICommons.BLACK_ARRAY))
        
        self.empty = [black_array, white_array]

    def _init_figure(self, figure):
        image = QImage("images/{}.png".format(figure.get_name()))
        
        # black on black
        image.setColor(image.colorTable().index(UICommons.WHITE), UICommons.BLACK_ARRAY)
        bb = QPixmap.fromImage(image)

        # white on black
        image.setColor(image.colorTable().index(UICommons.BLACK), UICommons.WHITE)
        wb = QPixmap.fromImage(image)
        
        # white on white
        image.setColor(image.colorTable().index(UICommons.BLACK_ARRAY), UICommons.WHITE_ARRAY)
        ww = QPixmap.fromImage(image)
        
        # black on white
        image.setColor(image.colorTable().index(UICommons.WHITE), UICommons.BLACK)
        bw = QPixmap.fromImage(image)

        self.figures[figure] = [bb, wb, bw, ww]
        
