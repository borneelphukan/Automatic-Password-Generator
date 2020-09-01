# Import Libraries and Classes
import random
from app_window import app_window

# List of Characters to be Used
ALPHABETS = [chr(x) for x in range(ord('a'), ord('z') + 1)]    # List of Aplhabets from a -> z
NUM = [str(i) for i in range(1, 10)]                           # List of Numbers from 1 -> 9
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*']             # List of Symbols

# Create Password Method
def create_password(choice, text):

    password = []
    if choice == 1:
        length = ALPHABETS + NUM + SYMBOLS
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 2:
        length = ALPHABETS + NUM
        for i in range(text):
            character = random.choice(length)
            password.append(character)
    
    elif choice == 3:
        length = ALPHABETS + SYMBOLS
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 4:
        length = ALPHABETS

    password = str(''.join(password))
    return password

# Create Password Button
def create_password_btn():

    if app_window.length.text() == "Select Length of Password":
            app_window.display.setText("Select Password Length !!")
    else:
        if app_window.numbers.isChecked() and app_window.special_characters.isChecked():
            choice = 1
        elif app_window.numbers.isChecked() and app_window.special_characters.isChecked()==False:
            choice = 2
        elif app_window.numbers.isChecked() == False and app_window.special_characters.isChecked():
            choice = 3
        elif app_window.numbers.isChecked() == False and app_window.special_characters.isChecked() == False:
            choice = 4
        
    text = int(app_window.length.selectedItem())
    create = create_password(choice, text)
    app_window.display.setText(create)
