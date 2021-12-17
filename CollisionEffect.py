from ursina import *

def update():
    global dx
    ball.x+=dx
    hit_info=ball.intersects()
    if hit_info.hit:
        dx=-dx
        if hit_info.entity in destroyables:
            destroy(hit_info.entity)

app=Ursina();
destroyables=[]
ball=Entity(model="sphere",collider="box",texture="brick")
box1=Entity(model="cube",texture="white_cube",scale=(1,3,2),position=(3,0,0),collider="box")
box2=Entity(model="cube",texture="white_cube",scale=(1,3,2),position=(-3,0,0),collider="box")
destroyables.append(box1)
destroyables.append(box2)
dx=0.07
box1=Entity(model="cube",texture="white_cube",scale=(1,3,2),position=(5,0,0),collider="box")
box2=Entity(model="cube",texture="white_cube",scale=(1,3,2),position=(-5,0,0),collider="box")
app.run()
