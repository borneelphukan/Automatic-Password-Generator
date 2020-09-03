import sys
from util import *
from app_window import app_window
from PyQt5.QtWidgets import QApplication
import PyQt5.QtCore
import PyQt5.QtGui

app = QApplication(sys.argv)
window = app_window()
sys.exit(app.exec_())