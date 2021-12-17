from ursina import *

def update():
    cube.rotation_z+=time.dt*50
    
app=Ursina()
cube=Entity(model="cube",color=color.rgb(0,0,100))
app.run()
