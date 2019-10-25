import os

def make_directory(ans):

    if ans.lower() == 'y' or ans.lower() == 'yes':
        prev = os.chdir('..')

        for i in range(4, 11):
            try:
                os.mkdir('Module{}'.format(i))
            except FileExistsError:
                continue

        print("Directories created: ")
        lst = os.listdir(prev)
        lst.sort()
        print(', '.join(lst))

    else:
        print('maybe next time')


answer = input("Do you want to create Modules 4-10 directories? (y/n): ")
make_directory(answer)