from ursina import *

app = Ursina()


def hexgrid_layout(l, max_x=10, max_y=10, origin=(0,0,0), offset=(0,0,0)):
    if not isinstance(l, list):
        print('error: hex_layout input must be a list or tuple, not', l.__class__.__name__)
        return
    x, y, z = 0, 0, 0

    row = list()
    dimensions = l[0].bounds.size
    direction = [-e*2 for e in origin]
    for i, e in enumerate(l):
        e.position=(
            x * dimensions[0] * direction[0],
            y * dimensions[1] * direction[1],
            z * dimensions[2] * direction[2]
        )
        e.position += offset
        e.origin = origin
        row.append(e)
        print(i, e)

          
h = Entity()
for i in range(5):
    hex = Entity(
        model=Cylinder(resolution=6),
        scale=0.1,
        color=color.orange,
        parent=h
    )

#hexgrid_layout(h.children)
grid_layout(h.children)

player = EditorCamera()
player.position = (0, 2, -10)
player.look_at(h.position)
app.run()