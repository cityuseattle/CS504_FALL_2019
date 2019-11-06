import shutil
import os

# I could not get this program to run with the relative path, so I used the absolute

#shutil.copy('C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\test0.txt', 'C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\Module5_Backup')
shutil.copy('C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\test0.py', 'C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\Module5_Backup')
# copy test0.py to destination with new name
shutil.copy('C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\test0.py', 'C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\Module5_Backup\\test0_newName.txt')

shutil.move('C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\test1.txt', 'C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\Module5_Backup')
shutil.move('C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\test1.py', 'C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\Module5_Backup')
# move test2.py and change to the new name
shutil.move('C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\test2.py', 'C:\\users\\david\\CS504_FALL_2019\\ON\\DavidJohnson\\Module5\\Module5_Backup\\test2_newName.py')
