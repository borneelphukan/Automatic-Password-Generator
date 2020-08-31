# Importing Libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from create_password import create_password_btn, create_button_btn
import sys

# Window Class
class Window(QMainWindow): 
    
    # Default Constructor
    def __init__(self): 

        # Super Method
        super().__init__()
        self.setWindowTitle("Password Generator")    # Title 
        self.setGeometry(0, 0, 1000, 1000)           # Size of the Window
        self.show() 

# Main Method
def main():
    app = QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec_())

# Execution Point
if __name__ == "__main__":
    main()
