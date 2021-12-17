from ursina import *

def update():
    if held_keys['a']:
        cube.x-=time.dt*2
    if held_keys['d']:
        cube.x+=time.dt*2
    if held_keys['w']:
        cube.y+=time.dt*2
    if held_keys['s']:
        cube.y-=time.dt*2
    camera.position=(cube.x,0,-25)

app=Ursina()

cube=Entity(model="cube",color=color.blue,texture="white_cube",position=(0,0,-1))

cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(1,0,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(0,1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(0,0,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(1,1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-1,1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-1,0,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(0,-1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(1,-1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-1,-1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(2,2,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(2,-2,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-2,2,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-2,-2,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-2,1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(2,1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(2,-1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-2,-1,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(1,2,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(1,-2,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-1,2,0))
cube2=Entity(model="cube",color=color.red,texture="white_cube",position=(-1,-2,0))

app.run()
