import cv2
import numpy as np
import pyautogui
from sys import argv
from datetime import datetime
from time import sleep

template = cv2.imread('./icon.png', cv2.IMREAD_GRAYSCALE)

SCALES = np.linspace(0.5, 2.0, 10)
THRESHOLD = 0.8
SLEEP_TIME = 10

def found_match():
    scrnsht = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)
    for scale in SCALES:
        resized_template = cv2.resize(template, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
        result = cv2.matchTemplate(scrnsht, resized_template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        if max_val > THRESHOLD:
            return True
    return False

while True:
    if found_match():
        print(f'Icon found at {datetime.now()}')
    else:
        print(f"Icon not found at {datetime.now()}")
    sleep(SLEEP_TIME)
    