import hashlib

while True:
    passwd = input("Please enter a password (letters and numbers only): ")

    if passwd.isalnum():
        print("You've just created your password.")

        if len(passwd) < 8:
            print("Your password is too short")
        else:
            hpasswd = hashlib.sha256(passwd.encode())
            print("Your password: " + hpasswd.hexdigest())
            break

    else:
        print("Sorry, password must be alphanumberic")
