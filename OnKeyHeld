from ursina import *
from random import randint

def update():
    if held_keys['a']:
        cube.rotation_y+=time.dt*100
    if held_keys['d']:
        cube.rotation_y-=time.dt*100
    if held_keys['w']:
        cube.rotation_x+=time.dt*100
    if held_keys['s']:
        cube.rotation_x-=time.dt*100

app=Ursina()

cube=Entity(model="cube",color=color.blue,texture="white_cube")
app.run()
