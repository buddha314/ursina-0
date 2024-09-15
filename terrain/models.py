from ursina import Entity, load_model, color, Cylinder

class HexPad(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            model=Cylinder(resolution=6),
            **kwargs
        ) 

"""
Grid Layout https://www.ursinaengine.org/api_reference.html#grid_layout
Signature 
 grid_layout(l, max_x=8, max_y=8, spacing=(0,0,0), origin=(-.5,.5,0), offset=(0,0,0))
Source
 https://github.com/pokepetter/ursina/blob/master/ursina/scripts/grid_layout.py
"""
def hexgrid_layout(l, max_x=8, max_y=8, spacing=(0,0,0), origin=(-.5,.5,0), offset=(0,0,0)):
    if len(origin) == 2:
        origin += (0,)
    if len(offset) == 2:
        offset += (0,)
    if not isinstance(l, list):
        print('error: hex_layout input must be a list or tuple, not', l.__class__.__name__)
        return
    x, y, z = 0, 0, 0

    row = list()
    dimensions = l[0].bounds.size
    direction = [-e*2 for e in origin]
    direction = [1 if e == 0 else e for e in direction]
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
    
        x += 1
        if x >= max_x:
            y += 1
            x = 0
            # center row
            if origin[0] == 0:
                for e in row:
                    e.x -= e.bounds.size.x * len(row) / 2 - e.bounds.size.x / 2
            row.clear()

        if y >= max_y:
            z += 1
            y = 0

        e.x *= 1 + spacing[0]
        e.y *= 1 + spacing[1]

    # center last row
    if origin[0] == 0:
        for e in row:
            e.x -= e.bounds.size.x * len(row) / 2 - (e.bounds.size.x / 2)
