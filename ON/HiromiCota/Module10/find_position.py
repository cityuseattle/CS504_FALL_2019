import pyautogui


print('Press control + C to terminate')
#Oh, god. What are we about to do that we need to remind people of how to kill command line processes?
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x) + ' Y: ' + str(y)
        print(positionStr, end='\r')
except KeyboardInterrupt:
    print('\nDone')