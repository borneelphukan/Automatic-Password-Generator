from PyQt5.QtWidgets import *
from PyQtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
from create_password import create_password_btn, create_button_btn
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec_())
    
if __main__ == "__main__":
    main()