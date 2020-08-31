from PyQt5.QtWidgets import *
from PyQtGui import *
from PyQt5 import *
from PyQt5.QtCore import *
from create_password import create_password_btn, create_button_btn

class app_window():
    def __init__(self):
        super().__init__()
        self.create_gui()

    def create_gui(QtWidgets.QWidget):
        self.setWindowTitle("Password Generator")
        self.setGeometry(540, 150, 400, 300)
        self.setFixedSize(400, 500)
        self.title = QtWidgets.QLabel(self)
        self.title.setText("Automatic Password Generator")
        self.title.move(110, 30)
        self.setFont(Qtgui.QFont("Times", 12, QtGui.QFont.DemiBold))
        
        self.display = QtWidgets.QLineEdit(self)
        self.display.setText("Generated Password...")
        self.display.setGeometry(0,0,350,50)
        self.display.move(30,70)
        self.display.setFont(QtGui.QFont("Times", 10))
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.clicked.connect(create_button_btn)
        
        self.generate = QtWidgets.QPushButton(self)
        self.generate.setText("Generate Password")
        self.generate.setGeometry(QRect(0, 0, 140, 40))
        self.generate.move(130, 170)
        
        self.length = QtGui.QComboBox(self)
        self.length.addItem("Select length of Password")
        self.length.addItem("5")
        self.length.addItem("6")
        self.length.addItem("7")
        self.length.addItem("8")
        self.length.addItem("9")
        self.length.addItem("10")
        self.length.addItem("11")
        self.length.addItem("12")
        self.length.addItem("13")
        self.length.addItem("14")
        self.length.addItem("15")
        
        self.numbers = QtWidgets.QCheckBox("Numbers", self)
        self.numbers.move(110,279)
        
        self.special_characters = QtWidgets.QCheckBox("Special Characters", self)
        self.special_characters.move(110,309)
        
        self.show()