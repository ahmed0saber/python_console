from ursina import *
from random import randint

def input(key):
    if key=="a":
        cube.rotation_y+=time.dt*200
    if key=="d":
        cube.rotation_y-=time.dt*200
    if key=="w":
        cube.rotation_x+=time.dt*200
    if key=="s":
        cube.rotation_x-=time.dt*200

app=Ursina()

cube=Entity(model="cube",color=color.blue,texture="white_cube")
app.run()
