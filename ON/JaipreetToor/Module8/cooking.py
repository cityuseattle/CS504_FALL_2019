import threading
import time

print('Begining...')

def meat():
    time.sleep(2)
    print('Meat is ready')

def veggie():
    time.sleep(2)
    print('Veggie is ready')

def soup():
    time.sleep(2)
    print('Soup is ready')

if __name__ == "__main__":
    mom = threading.Thread(target=meat)
    mom.start()
    dad = threading.Thread(target=veggie)
    dad.start()
    sister = threading.Thread(target=soup)
    sister.start()