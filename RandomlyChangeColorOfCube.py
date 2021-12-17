from ursina import *
from random import randint
import time

def update():
    red=randint(0,255)
    green=randint(0,255)
    blue=randint(0,255)
    cube.color=color.rgb(red,green,blue)
    time.sleep(0.2)

app=Ursina()
cube=Entity(model="cube",color=color.rgb(0,0,100))
app.run()
