from ursina import *

def update():
    global speed
    cube.x+=time.dt*speed
    if abs(cube.x)>3:
        speed*=-1

app=Ursina()
speed=1
cube=Entity(model="cube",color=color.rgb(0,0,100),scale=(1,2,10))
app.run()
