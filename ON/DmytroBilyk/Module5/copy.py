import shutil
import os

shutil.copy('test0.txt', './Module5_Backup')
shutil.copy('test0.py', './Module5_Backup')

shutil.copy('test0.py', './Module5_Backup/test0_newName.txt')


shutil.copy('test1.txt', './Module5_Backup')
shutil.copy('test1.py', './Module5_Backup')

shutil.copy('test2.py', './Module5_Backup/test0_newName.txt')
