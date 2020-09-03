from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from util import create_password
from PyQt5 import *
from PyQt5.QtCore import *

class app_window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.create_gui()

    def create_gui(self):
        self.setWindowTitle("Password Generator")
        self.setGeometry(540, 150, 400, 300)
        self.setFixedSize(400, 500)
        self.title = QtWidgets.QLabel(self)
        self.title.setText("Automatic Password Generator")
        self.title.move(110, 30)
        
        self.display = QtWidgets.QLineEdit(self)
        self.display.setText("Generated Password...")
        self.display.setGeometry(0,0,350,50)
        self.display.move(30,70)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignCenter)
        
        self.generate = QtWidgets.QPushButton(self)
        self.generate.setText("Generate Password")
        self.generate.setGeometry(QRect(0, 0, 140, 40))
        self.generate.move(130, 170)
        
        self.length = QComboBox(self)
        self.length.move(110, 239)
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

        self.upper_case = QtWidgets.QCheckBox("Uppercase", self)
        self.upper_case.move(110,339)

        self.generate.clicked.connect(self.create_password_btn)
        
        self.show()

    def create_password_btn(self):
        if self.length.itemData("Generated Password..."):
            self.display.setText("Select Password Length !!")
        else:
            if self.numbers.isChecked() and self.special_characters.isChecked():
                choice = 1
            elif self.numbers.isChecked() and self.special_characters.isChecked()==False:
                choice = 2
            elif self.numbers.isChecked() == False and self.special_characters.isChecked():
                choice = 3
            elif self.numbers.isChecked() == False and self.special_characters.isChecked() == False:
                choice = 4
            elif self.numbers.isChecked() and self.special_characters.isChecked() and self.upper_case.isChecked():
                choice = 5
            elif self.numbers.isChecked() and self.special_characters.isChecked() == False and self.upper_case.isChecked():
                choice = 6
            elif self.numbers.isChecked() and self.special_characters.isChecked() and self.upper_case.isChecked() == False:
                choice = 7
            elif self.numbers.isChecked() and self.special_characters.isChecked() == False and self.upper_case.isChecked() == False:
                choice = 8
            elif self.numbers.isChecked() == False and self.special_characters.isChecked() and self.upper_case.isChecked():
                choice = 9
            elif self.numbers.isChecked() == False and self.special_characters.isChecked() == False and self.upper_case.isChecked():
                choice = 10
            elif self.numbers.isChecked() == False and self.special_characters.isChecked() and self.upper_case.isChecked() == False:
                choice = 11
            elif self.numbers.isChecked() == False and self.special_characters.isChecked() == False and self.upper_case.isChecked() == False:
                choice = 12
            text = self.length.currentIndex()
            create = create_password(choice,text)
            self.display.setText(create)