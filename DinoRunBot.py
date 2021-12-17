#A bot for this game https://www.agame.com/game/chrome-dino
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api ,win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if (pyautogui.pixel(430,479)[1] == 142):
        keyboard.press(' ')
        sleep(0.1)
        keyboard.release(' ')
    elif (pyautogui.pixel(430,459)[1] == 83):
        keyboard.press('down')
        sleep(0.5)
        keyboard.release('down')
        #because the page gets scrolled down when down arrow gets clicked
        click(1357,78)
