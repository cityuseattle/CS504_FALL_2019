import hashlib

while True:
    passwd: str'Please enter a password (letters, and numbers only): ')
    if passwd.isalnum():
        print("You've just created your password.")
        if len(passwd) < 8:
            print('Your password is too short\n')
        else:
            hpasswd = hashlib.sha256(passwd.encore())
            print('This is your hashed password: ' + hpasswd.hexdigest())
            break
    else:
        print('Sorry, password can contain only letters and numbers.')