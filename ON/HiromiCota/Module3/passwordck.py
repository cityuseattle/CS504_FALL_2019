import hashlib

while True:
    passwd = raw_input('Please enter a password (letters and numbers only): ')
    if passwd.isalnum():
        print("You've just created your password")
        if len(passwd) < 8:
            print('Your password is too short.\n')
        else:
            hpasswd = hashlib.sha256(passwd.encode())
            print('This is your hashed password: ' + hpasswd.hexdigest())
        break
    else:
        print('Sorry. Passwords can contain only letters and numbers.')
        