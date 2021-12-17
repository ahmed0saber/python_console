from ursina import *
from random import randint

def input(key):
    if key =='a':
        y=randint(-5,5)
        x=randint(-5,5)
        z=randint(-5,5)
        a=randint(1,3)
        b=randint(1,3)
        c=randint(1,3)
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)
        newcube = Entity(model='cube',color=color.rgb(red, green, blue),texture="white_cube", position=(x,y,z), scale=(a,b,c))

app=Ursina()
app.run()
