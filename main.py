import pyautogui
import random
import time

# get the resolution (width & height) of display
width, height = pyautogui.size()

while True:
    # move the cursor every 4 mins as MS Teams & Skype changes the status after 5 mins
    time.sleep(240)
    
    # get new random co-ordinates
    newWidth, newHeight = random.randint(0, width), random.randint(0,height)

    # move the cursor to new co-ordinates
    pyautogui.moveTo(newWidth, newHeight)

'''
MS Teams in my organization was smart enough and was
not turning green with the above code snippet :P
I used the below code snippet to fool MS Teams

while True:
    time.sleep(240)

    # Simulate the scroll action by not literally scrolling :P
    pyautogui.scroll(0)

'''