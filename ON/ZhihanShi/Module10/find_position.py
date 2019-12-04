import pyautogui

print('Press control + c to terminate')
try:
    while True:
        x,y = pyautogui.position()
        positionStr = 'x:' + str(x) + ' Y: ' + str(y)
        print(positionStr, end='\r')
except KeyboardInterrupt:
    print('\nDone')