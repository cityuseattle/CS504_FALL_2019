import os

def deleteDirectory(ans):
    if ans.lower() == 'y' or ans.lower() == 'yes':
        prev = os.chdir('..')
        print(os.getcwd())
        for i in range(4, 11):
            # if directory already exists
            if not ('Module{}'.format(i)):
                # if directory has no contents
                if len(os.listdir('Module{}'.format(i))) == 0:
                    try:
                        os.rmdir('Module{}'.format(i))
                    except FileExistsError:
                        continue 
                # if directory has contents       
                else:
                    print('Module{} not empty, cannot be deleted'.format(i))    
        print('There you go!')
        lst = os.listdir(prev)
        lst.sort()
        print(', '.join(lst))
    else:
        print('Maybe next time :)')


if __name__ == '__main__':
    answer = input('Do you want to delete Module 4-10 directories? (y/n): ')
    deleteDirectory(answer) 