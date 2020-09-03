import random
ALPHABETS = [chr(i) for i in range(ord('a'), ord('z')+1)]
SYMBOLS = ['!','@','#','$','%','^','&','*']
NUM = [str(i) for i in range(1, 10)]   
UPPER_CASE = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

def create_password(choice,text):
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

    elif choice == 5:
        length = ALPHABETS + SYMBOLS + NUM + UPPER_CASE
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 6:
        length = ALPHABETS + NUM + UPPER_CASE
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 7:
        length = ALPHABETS + NUM + SYMBOLS
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 8:
        length = ALPHABETS + NUM
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 9:
        length = ALPHABETS + SYMBOLS + UPPER_CASE
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 10:
        length = ALPHABETS + UPPER_CASE
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 11:
        length = ALPHABETS + SYMBOLS
        for i in range(text):
            character = random.choice(length)
            password.append(character)

    elif choice == 4 or choice == 12:
        length = ALPHABETS

    password = str(''.join(password))
    return password