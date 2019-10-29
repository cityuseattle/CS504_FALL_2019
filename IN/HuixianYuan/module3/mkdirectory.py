import os

def makedirectory(ans):
    if ans.lower()=='y' or ans.lower()=='yes':
        prev = os.chdir('..')
        print(os.getcwd())
        for i in range(4,11):
            # if directory already exists, slip to make the next one
            if not ('Mocule{}'.format(i)):
                # if directory have no contents
                if len(os.listdir('Module{}'.format(i))) ==0:
                    try:
                        os.mkdir('Module{}'.format(i))
                    except FileExistsError:
                        continue
                #if directory have contents
                else:
                    print('Module{} not empty, cannot be deleted'.format(i))
        print('there you go.')
        lst=os.listdir(prev)
        lst.sort()
        print(', '.join(lst))
    else:
        print('maybe next time :)')

if __name__ == '__main__':
    answer = input('do you want to create module 4-10 directories? (y/n): ')
    makedirectory(answer)