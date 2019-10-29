import hashlib

while True:
    passwd=input('please enter a password (letters, and numbers only): ')
    if passwd.isalnum():
        print('you have just created your pasword.')
        if len(passwd) < 8:
            print('your password is too short.\n')
        else:
            hpasswd = hashlib.sha256(passwd.encode())
            print('This is your hashed  password: '+hpasswd.hexdigest())
            break
    else:
        print('sorry, your password contain only letters and numbers.')