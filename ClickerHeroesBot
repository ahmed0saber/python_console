#A bot for this game https://www.kongregate.com/games/Playsaurus/clicker-heroes
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api ,win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(2)
while keyboard.is_pressed('q') == False:
    click(830, 400)
