import pyautogui
import time
import random
import threading

def autoclicker(x,y):
    print(f'Autoclicker starting. Clicks will occur randomly between {x} and {y} seconds. Press Ctrl+C in the terminal to stop.')
    time.sleep(10)
    while True:
        pyautogui.click()
        if random.choice([True, False, False]):

            dx = random.randint(-3,3)
            dy = random.randint(-3,3)
            dura = random.uniform(0.01,0.1)
            pyautogui.moveRel(dx,dy,duration=dura)
        interval = random.uniform(x,y)
        time.sleep(interval)
x = float(input('Enter number1:   '))
y = float(input('Enter number2:   '))
autoclicker(x,y)