import shutil
import os

extension = input("what file extension do you want to delete?")

for filename in os.listdir("./"):
    if filename.endswith(extension):
        print(filename)



answ = input("Are you sure? y/n ")

if answ.lower() == "y":
    for filename in os.listdir("./"):
        if filename.endswith(extension):
            os.unlink(filename)
