#A bot for this game https://www.agame.com/game/magic-piano-tiles
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
x=0
locationY=200
while keyboard.is_pressed('q') == False:
    
    if (pyautogui.pixel(540, locationY)[0] == 0) and (x!=1):
        click(540, locationY)
        x=1
        locationY+=2
    if (pyautogui.pixel(635, locationY)[0] == 0) and (x!=2):
        click(635, locationY)
        x=2
        locationY+=2
    if (pyautogui.pixel(725, locationY)[0] == 0) and (x!=3):
        click(725, locationY)
        x=3
        locationY+=2
    if (pyautogui.pixel(820, locationY)[0] == 0) and (x!=4):
        click(820, locationY)
        x=4
        locationY+=2
