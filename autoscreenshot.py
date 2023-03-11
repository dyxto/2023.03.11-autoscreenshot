"""
WHO: DYxTO | github.com/dyxto
WHAT: autoscreenshot
WHEN: March 11, 2023
WHERE: VS CODE | Python
WHY: i wanted to monitor my pc temps and usage while gaming
HOW: i decided to automate screenshotting a second screen
~~~ i'll still have to manually read and record
~~~ the numbers for graphs but oh well for now
"""

import pyautogui
import time

count=10 #total number of captures

while count > 0:
    time.sleep(60) #number of seconds before each capture
    pyautogui.keyDown("win")
    pyautogui.press("printscreen")
    pyautogui.keyUp("win")
    print(count)
    count-=1

pyautogui.keyUp("win")
