from ursina import *
import time

def update():
    if held_keys['a']:
        cube.x-=time.dt*2
    if held_keys['d']:
        cube.x+=time.dt*2
    if held_keys['w']:
        cube.z+=time.dt*2
    if held_keys['s']:
        cube.z-=time.dt*2
    camera.position=(cube.x,4,-30)
    
app=Ursina()

cube=Entity(model="cube",color=color.blue,texture="white_cube",position=(0,1,0))

ground=Entity(model="cube",color=color.red,texture="white_cube",position=(0,0,0),scale=(10,1,10))

app.run()
