import os 

def deletedirectory(ans):
    if ans.lower() == 'y' or ans.lower( )=='yes':
        prev=os.chdir('..')
        for i in range(4, 11):
            #if directory already exists 
            if ('Module {}' .format(i)):
              #if directory has no contents
                if len(os.listdir('Module {}' .format(i))) == 0: 

                    try:
                        print("Deleting Module {}".format(i))
                        os.rmdir('Module {}'.format(i))
                    except FileExistsError :
                        continue

                else:
                    print("Module {} not empty, cannot be deleted" .format(i))
        print("There you go!")
        lst=os.listdir(prev)
        lst.sort()
        print(',' .join(lst))
    else:
        print("May be next time :) ")


if __name__  == "__main__":
    answer=input("Do you want to delete modeule 4-10 directories ? (y/n): ") 
    deletedirectory(answer)       