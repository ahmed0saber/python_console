from ursina import *

def update():
    global speed
    cube.x+=time.dt*speed
    camera.position=(cube.x,0,-25)
    if abs(cube.x)>3:
        speed*=-1

app=Ursina()
speed=1

cube=Entity(model="cube",color=color.rgb(0,0,100),scale=(2,2,2))
cube2=Entity(model="cube",color=color.rgb(100,50,100),scale=(1,1.5,5))
cube2.y=2
app.run()
