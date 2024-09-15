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
    
    def craft(self, ingredients):
        """
        Send in some ingredients and get back the product if you have the right stuff
        
        ingredients: list of strings with duplicated
        self.ingredients: dicitionary of string with minimum required amount
        """
        build = True
        ingredients_set = set(self.ingredients)
        for ing in ingredients_set:
            if ingredients.count(ing) < self.ingredients.count(ing):
                print(f"Missing {ing}")
                build = False
        if build:
            print (globals())
            return globals()[self.product]()
        else:
            return None
"""
Put all models in here to avoid circular imports
"""

class HandAxe(Resource):
    def __init__(self, **kwargs):
        super().__init__(name='handaxe', 
            #model = load_model('assets/fbx/Hand_Axe.glb'),
            model = 'cube',
            **kwargs)

HandAxeRecipe = Recipe('handaxe', ['wood', 'wood', 'stone'], 'HandAxe')

        