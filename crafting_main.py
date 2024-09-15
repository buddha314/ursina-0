from ursina import *
from crafting import models, recipes
from ursina.prefabs.first_person_controller import FirstPersonController

if __name__ == "__main__":
    s1 = models.Stone()
    w1 = models.Wood()
    w2 = models.Wood()
    app = Ursina()

    handaxe_recipe = models.Recipe('handaxe', ['wood', 'wood', 'stone'], 'HandAxe')
    recipes.HandAxeRecipe.craft(ingredients=['wood', 'wood', 'stone'])
    camera = EditorCamera()
    app.run()