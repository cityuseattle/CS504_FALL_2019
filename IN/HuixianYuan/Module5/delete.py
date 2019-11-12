import shutil
import os

extension=input("what extension of file do you want ot delete?")
for filename in os.listdir('./'):
    if filename.endswith(extension):
        print(filename)

ans=input("are you sure to delete? (y/n)")
if ans.lower=='y':
    for filename in os.listdir('./'):
        if filename.endswith(extension):
            os.unlink(filename)