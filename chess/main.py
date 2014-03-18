#!/usr/bin/python3

import sys
from PyQt4.QtGui import *
# from PyQt4.QtCore import *

from main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

main()
