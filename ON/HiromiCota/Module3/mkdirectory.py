import os


def makedirectory(ans):
    if ans.lower() == 'y' or ans.lower() == 'yes':
        prev = os.chdir('..')
        for i in range(4, 11):
            # if dir exists, skip
            try:
                os.mkdir('Module{}'.format(i))
            except IOError:
                continue
        print("There you go!")
        lst = os.listdir(prev)
        lst.sort()
        print(', '.join(lst))
    else:
        print("Maybe next time")


if __name__ == "__main__":
    answer = raw_input("Do you want to create Module 4-10 directories? (y/n): ")
    makedirectory(answer)

    
