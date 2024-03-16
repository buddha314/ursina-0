from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


# Create a cylinder in ursina with a given radius and height and offset
def create_cylinder(radius, height, offset):
    # Create a cylinder
    cylinder = Entity(model='cylinder', scale=(radius, height, radius), color=color.white, position=offset)
    return cylinder

# Take an array of five integers and normalized the values to be between 0 and 1
def normalize_array(array):
    s = sum(array)
    normalized_array = [i/s for i in array]
    return normalized_array

# Create the cylinders from the normalized array
def create_cylinders(normalized_array):
    cylinders = []
    for i in range(5):
        cylinder = create_cylinder(0.1, normalized_array[i], Vec3(i, 0, 0))
        cylinders.append(cylinder)
    return cylinders

def update():
    t = time.time()
    camera_rotation_speed = 25
    camera.position = (camera_radius * math.sin(t/camera_rotation_speed)
                       , 4
                       , camera_radius * math.cos(t/camera_rotation_speed))
    camera.look_at(Vec3(0,0,0))
    print(t)


# run the app
if __name__ == '__main__':
    camera_radius = 10
    app = Ursina() 
    sky = Sky() 
    # Create a normalized array
    #normalized_array = normalize_array([1, 2, 3, 4, 5])
    # Create the cylinders
    #cylinders = create_cylinders(normalized_array)

    data = [1, 2, 3, 4, 5]
    total = sum(data)
    """
    for i in range(5):
        cylinder = Entity(model=Cylinder(6, start=-.5), color=color.hsv(60,1,1,.3), scale=(1, data[i]/total, 1), position=(i, 0, 0))

    """
    Entity(model=Cylinder(6, start=-.5), color=color.hsv(60,1,1,.3)
           , position = (1,0,0)
           )
    Entity(model=Cylinder(6, start=-.5, height=4), color=color.hsv(60,1,1,.3))
    origin = Entity(model='quad', color=color.orange, scale=(5, .05))
    """
    ed = EditorCamera(rotation_speed = 200, panning_speed=200
                      , pan_speed = (0.5, 0.5)
                      , look_at=(0,0,0)
                      , position = (0, 4, -10))
    """
    # create a camera to look at the origin
    #camera.position = (0, 4, 0)
    #camera.look_at(Vec3(0,0,0))

    app.run()
