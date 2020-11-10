import string

users = ['Sam', 'Frank', 'Jane']
caps = string.ascii_uppercase
numbers = []
for i in range(10):
    numbers.append(str(i))
special_chars = ['!', '@', '#', '$']
name_check = False


def name_available(name):
    if name.title() in users:
        return False
    else:
        return True


def number_found(name):
    found = False
    for number in numbers:
        if name.find(number) > -1:
            found = True
    return found


def caps_found(pw):
    found = False
    for letter in caps:
        if pw.find(letter) > -1:
            found = True
    return found


def special_found(pw):
    found = False
    for char in special_chars:
        if pw.find(char) > -1:
            found = True
    return found


while True:
    if not name_check:
        username = input("Enter your username: ")
        if name_available(username):
            if not number_found(username):
                if 2 < len(username) < 15:
                    name_check = True
                    users.append(username)
                    print("Username created")
            else:
                print("Username cannot contain numbers")
        else:
            print("Please choose another username")
    else:
        password = input("Enter your password: ")
        if caps_found(password):
            if special_found(password):
                if number_found(password):
                    if len(password) > 7:
                        print(f'Your username is {username} and your password is {password}')
                        break
                    else:
                        print("Password must be at least 8 characters long")
                else:
                    print("Password must contain a number")
            else:
                print("Password must contain a special character ('!', '@', '#', '$')")
        else:
            print("Password must contain a capital letter")
