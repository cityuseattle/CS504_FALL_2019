import os

def deletedirectory(ans):
    if ans.lower()=='y' or ans.lower() == 'yes':
        prev = os.chdir('..')
        print(os.getcwd())
        for i in range(4,11):
            if not ('Module{}'.format(i)):
                if len(os.listdir('Module{}'.format(i))) ==0:
                    try:
                        os.rmkdir('Module{}'.format(i))
                    except FileExistsError:
                        continue
            else:
                print("Module{} not empty. coannot be deleted".format(i))
        print("THERE YOU GO!")
        lst = os.listdir(prev)
        lst.sort()
        print(', '.join(lst))
        
   
if __name__ == "__main__":
    answer= input("Do you want to delete Module 4-10 directories(y/n):")
    deletedirectory(answer)