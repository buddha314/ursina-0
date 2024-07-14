from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def update():
    for key, value in held_keys.items():
        if key == 'z':
            print("press z key")

# run the app
if __name__ == '__main__':
    app = Ursina() 
    sky = Sky()
    ground = Entity(model='plane', scale=32, texture='white_cube', texture_scale=(32,32), collider='box')
    
    n_floors = 4
    cylinder_resolution = 6
    Entity(model='cube', scale=(2,0.1,2), position=(0, 0, 0), texture='brick')
    for i in range(n_floors):
        #Entity(model=Plane(subdivisions=(3,6)), position=(0, i, 0), texture='brick', rotation=-45)
        Entity(model='cube', scale=(2,0.1,2), position=(0, i+1, 0), texture='brick')
        # Pillars?
        Entity(model=Cylinder(resolution=cylinder_resolution, radius=0.2), position=(1, i, 1), texture='brick')
        Entity(model=Cylinder(resolution=cylinder_resolution, radius=0.2), position=(1, i, -1), texture='brick')
        Entity(model=Cylinder(resolution=cylinder_resolution, radius=0.2), position=(-1, i, 1), texture='brick')
        Entity(model=Cylinder(resolution=cylinder_resolution, radius=0.2), position=(-1, i, -1), texture='brick')
    player = FirstPersonController(gravity=0, position=Vec3(-3,0,0))
    player.look_at(Vec3(0,0,0))
    #camera = EditorCamera()
    app.run()
