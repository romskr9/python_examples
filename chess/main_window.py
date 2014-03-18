from PyQt4.QtGui import *
from PyQt4.QtCore import *

from picture_button import PictureButton
from ui_commons import UICommons
from images import Images

from engine.common import Common
from engine.game import Game
from engine.game_manager import GameManager

class MainWindow(QMainWindow):
    """This class encapsulates main window of the chess application"""
    
    #signals used in the application
    close_app = pyqtSignal()
    redraw = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.images = Images() 
        self._init_ui()
        self._init_game()
        
    def _init_game(self):
        self.selected = None
        self.players_color = Common.white
        self._create_new_game()
        
    def _init_ui(self):
        """Initialization of the user interface"""
        
        #connect signals to slots
        self.close_app.connect(self.close)
        self.redraw.connect(self.update)
        
        #design of the main window
        self.statusBar().showMessage("")
        layout = QHBoxLayout()
        layout.insertLayout(1, self._init_buttons())
        layout.insertLayout(0, self._init_board())
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()
        
    def _init_board(self):
        """Initialization of the chess board"""
        
        self._buttons = []
        layout = QGridLayout()
        layout.setSpacing(0)
        
        #create labels of rows and columns
        for i in range(1, Common.board_size + 1):
            self._add_chessboard_label(layout, i, 0)
            self._add_chessboard_label(layout, i, Common.board_size + 1)
            self._add_chessboard_label(layout, 0, i)
            self._add_chessboard_label(layout, Common.board_size + 1, i)
            
        #create fields of the board
        for x in range(Common.board_size):
            for y in range(Common.board_size):
                button = PictureButton(self, Common.reverse(y, -1) * Common.board_size + x)
                button.setCheckable(True)
                button.clicked.connect(self.button_clicked)
                self._buttons.append(button)
                layout.addWidget(button, y + 1, x + 1)
        self.board_layout = layout
        self._board_labels()
        return layout
    
    @staticmethod
    def _add_chessboard_label(layout, y, x):
        """This auxiliary function adds a empty label into layout and centers it."""
        label = QLabel(' ')
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout.addWidget(label, y, x)
    
    def _board_labels(self):
        """Write labels of rows and columns of the chess board."""
        
        for x in range(1, Common.board_size + 1):
            letter = chr(ord('A') + x - 1)
            self.board_layout.itemAtPosition(0, x).widget().setText(letter)
            self.board_layout.itemAtPosition(Common.board_size + 1, x).widget().setText(letter)
        direction = -1 if self.players_select[UICommons.WHITE_STR].isChecked() else 1
        for y in range(1, Common.board_size + 1):
            letter = chr(ord('A') + Common.reverse(y - 1, direction))
            self.board_layout.itemAtPosition(y, 0).widget().setText(letter)
            self.board_layout.itemAtPosition(y, Common.board_size + 1).widget().setText(letter)

    def _init_buttons(self):
        """Initialization of the control buttons and radio checks"""
        
        layout = QVBoxLayout()
        
        #New game button
        new_button = QPushButton("New game")
        layout.addWidget(new_button)
        new_button.clicked.connect(self.new_game_clicked)
        layout.addStretch(1)
        
        #Player's color selection
        player_select = self._init_player_select()
        layout.addWidget(player_select)
        layout.addStretch(1)
        
        #Exit button
        exit_button = QPushButton("Exit")
        layout.addWidget(exit_button)
        exit_button.clicked.connect(self.close_app)
        layout.addStretch(1)
        
        return layout
    
    def _init_player_select(self):
        """Initialization of the player's select radio group"""
        player_select = QGroupBox("Player's color")
        layout = QHBoxLayout()
        self.players_select = {}
        for color, selected in [(UICommons.WHITE_STR, True), (UICommons.BLACK_STR, False)]:
            button = QRadioButton(color)
            button.setChecked(selected)
            button.clicked.connect(self.players_color_selected)
            layout.addWidget(button)
            self.players_select[color] = button
        player_select.setLayout(layout)
        return player_select
    
    def _players_color(self):
        """Give numeric value based on player's color"""
        return 0 if self.players_select[UICommons.BLACK_STR].isChecked() else 1
    
    def button_clicked(self):
        """This method is called when an array of the board (button) is clicked."""
        position = UICommons.game_position(self.sender().position, self._players_color())
        if self.selected:
            result = self.game.players_move((self.selected, position, None))
            self.selected = None
            self.redraw.emit()
            self._computers_move()
        else:
            self.selected = position
        self.redraw.emit()
        
    def new_game_clicked(self):
        """This method is called when the New game button is clicked."""
        self._create_new_game()

    def _create_new_game(self):
        """Create a new game, on demand or on start"""
        GameManager.new_game()
        self.game = GameManager.instance()
        self.selected = None
        self.redraw.emit()
        if self.players_select[UICommons.BLACK_STR].isChecked():
            self._computers_move()
        
    def _computers_move(self):
        self.game.computers_move(self._players_color())
        self.redraw.emit()
        
    def players_color_selected(self):
        """Player selects his color""" 
        self._board_labels()
        self.redraw.emit()

