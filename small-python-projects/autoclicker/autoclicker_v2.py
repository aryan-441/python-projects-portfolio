from pynput import keyboard
import time
import random
import threading
import pyautogui
CLICK_MIN = 3.0
CLICK_MAX = 7.0

MOVE_X_MIN = 10
MOVE_Y_MIN = 10
MOVE_X_MAX = -10
MOVE_Y_MAX = -10
MOVE_CHANCE = random.choice([1/2,1/3,1/4])

E_MIN = 60
E_MAX = 220

E_HOLD_MIN = 2
E_HOLD_MAX = 6
XPB_MIN = 160
XPB_MAX = 225
TAB_MIN = 60
TAB_MAX = 220

WASD_MIN = 60
WASD_MAX = 180

WASD_HOLD_MIN = 0.05
WASD_HOLD_MAX = 0.1

WASD_KEYS = ['w','a','s','d']
clicking = True
running = True
def stop_program():
    global running
    running = False
    print('Stopping')
def keyboard_listener():
    with keyboard.Listener(
        on_press=lambda key:
        stop_program() if key == keyboard.Key.esc else None
    ) as listener:
        listener.join()

def press_e():
    global clicking
    clicking = False
    pyautogui.press('e')
    time.sleep(random.uniform(2,6))
    pyautogui.press('e')
    clicking = True
def run_xpb():
    global clicking
    clicking = False
    pyautogui.write('/XPB 250', interval=random.uniform(0.2,0.4))
    pyautogui.press('enter')
    time.sleep(random.uniform(3,5))
    clicking = True
def press_tab():
    global clicking
    clicking = False

    pyautogui.keyDown('tab')
    time.sleep(random.uniform(2, 6))
    pyautogui.keyUp('tab')

    clicking = True

def do_wasd():
    global clicking
    clicking = False
    key = random.choice(WASD_KEYS)
    pyautogui.keyDown(key)
    time.sleep(random.uniform(WASD_HOLD_MIN,WASD_HOLD_MAX))
    pyautogui.keyUp(key)
    clicking = True

'''
START
'''

print('Starting in 10 seconds...')
print('Press esc or Ctrl+C to stop')
time.sleep(10)
threading.Thread(
    target=keyboard_listener,
    daemon=True
).start()
next_e = time.time() + random.uniform(E_MIN, E_MAX)
next_xpb = time.time() + random.uniform(XPB_MIN,XPB_MAX)
next_wasd = time.time() + random.uniform(WASD_MIN, WASD_MAX)
next_tab = time.time() + random.uniform(TAB_MIN, TAB_MAX)
'''
MAIN
'''
while running:
    current_time = time.time()
    '''
    E EVENT
    '''
    if current_time >= next_e:
        press_e()
        next_e = time.time() + random.uniform(E_MIN,E_MAX)
        continue
    '''
    XPB EVENT
    '''
    if current_time >= next_xpb:
        run_xpb()
        next_xpb = time.time() + random.uniform(XPB_MIN, XPB_MAX)
        continue

    '''
    WASD EVENT
    '''

    if current_time >= next_wasd:
        do_wasd()
        next_wasd = time.time() + random.uniform(WASD_MIN,WASD_MAX)
        continue
    '''
    TAB EVENT
    '''
    if current_time >= next_tab:
        press_tab()
        next_tab = time.time() + random.uniform(TAB_MIN, TAB_MAX)
        continue
    if clicking: 
        pyautogui.click()
        if random.random() < MOVE_CHANCE:
            dx = random.randint(
                MOVE_X_MAX, MOVE_X_MIN
            )
            dy = random.randint(
                MOVE_Y_MAX, MOVE_Y_MIN
            )
            dura = random.uniform(0.01,0.1)
            pyautogui.moveRel(dx,dy,duration=dura)
        time.sleep(random.uniform(CLICK_MIN, CLICK_MAX))

pyautogui.keyUp('e')
print('Stopped.')
