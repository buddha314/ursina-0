from ursina import Entity, load_model

class Resource(Entity):
    def __init__(self, name,**kwargs):
        super().__init__(
            size=(75, 75),
            **kwargs)
        self.name = name 

class Wood(Resource):
    def __init__(self, **kwargs):
        super().__init__(name='wood', 
            model = load_model('assets/fbx/Solid_Wooden_Wheel.gltf'),
            rotation_x = 90,
            **kwargs
        )


class Stone(Resource):
    def __init__(self, **kwargs):
        super().__init__(name='stone', 
            model = load_model('assets/fbx/Simple_Rock.glb'),
            **kwargs)

class Recipe:
    def __init__(self, name, ingredients, product):
        self.name = name
        self.ingredients = ingredients
        self.product = product