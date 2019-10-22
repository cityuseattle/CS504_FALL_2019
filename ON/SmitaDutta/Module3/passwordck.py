import hashlib
while True:
    passwd=input("Please enter a password (letters and numbers only ):" )
    if passwd.isalnum() :
        print("Yoy have just created your password .")

        if(len(passwd) < 8):
         print("Your password is too short. \n")

        else:
           hpassword=hashlib.sha256(passwd.encode())
           print("This is your hash password: " +hpassword.hexdigest())
           break
    else:
        print(" Sorry , Password can contain only letters and numbers. ")

             

