BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
PasswordSet = False
while not PasswordSet:
    password = input("Please enter a password:")
    check = input("Please enter your password again:")
    length = len(password)
    if password != check:
        print("Sorry, your passwords don't match! Please try again.")
    elif password in BAD_PASSWORDS:
        print("Sorry, that is too common of a password! Please try again.")
    elif length < 8 or length > 12:
        print("Sorry, your password must be between 8 and 12 characters long. Please try again.")
    else:
        PasswordSet = True
        print("Password set!")
