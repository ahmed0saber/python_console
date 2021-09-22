from ursina import *
from random import randint
import time

def update():
    y=randint(-5,5)
    x=randint(-5,5)
    z=randint(-5,5)
    newcube = Entity(model='cube', color=color.yellow,texture="white_cube", position=(x,y,z), scale=(1,1,1))
    time.sleep(0.5)

app=Ursina()
app.run()
