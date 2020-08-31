import random
from app_window import app_window

ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NUM = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*']

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

def create_password_btn():
    if app_window.length.text() == "Select length of Password":
            app_window.display.setText("Select password length !!")
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
