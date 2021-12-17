from ursina import *

app=Ursina()

cube=Entity(model="cube",color=color.yellow,rotation=(45,45,0),texture="white_cube")
cube2=Entity(model="cube",color=color.yellow,rotation=(45,45,0),texture="brick",position=(2,2,2))
app.run()
