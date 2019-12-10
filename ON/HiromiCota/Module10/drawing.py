import pyautogui
import webbrowser
import time
import os



webbrowser.open('https://www.youidraw.com/apps/painter/')
time.sleep(5)
x, y = pyautogui.size()
pyautogui.click(x//2, y//2)
distance = 200
while distance > 0:
    # dragRel() drags mouse relative to its current position
    # excuse me? What?
    pyautogui.dragRel(distance, 0, duration=0.25)
    distance = distance - 20
    # why not distance -= 20?
    pyautogui.dragRel(0, distance, duration=0.25)
    pyautogui.dragRel(-distance, 0, duration=0.25)
    distance -= 20
    pyautogui.dragRel(0, -distance, duration=0.25)
#close drawing tab after 5 seconds
time.sleep(5)

#use command for MacOS instead of ctrl
if os.sys.platform == 'darwin':
    pyautogui.hotkey('command', 'w')
    pyautogui.press('return')
else:
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.press('enter')