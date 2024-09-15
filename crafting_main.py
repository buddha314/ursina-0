from ursina import *
from crafting import models as crafting_models
from terrain import models as terrain_models
from ursina.prefabs.first_person_controller import FirstPersonController

if __name__ == "__main__":
    #s1 = models.Stone()
    #w1 = models.Wood()
    #w2 = models.Wood()
    app = Ursina()

    """
    Craft a handaxe, which is a white cube
    """
    handaxe_recipe = crafting_models.Recipe('handaxe', ['wood', 'wood', 'stone'], 'HandAxe')
    # Will show up if you actually craft it, neat!
    #crafting_models.HandAxeRecipe.craft(ingredients=['wood', 'wood', 'stone'])
    
    """
    Set up the terrain, I think.
    """
    center = Entity(model='quad', scale=.1, color=color.red)
    p = Entity()
    for i in range(4*5):
        #b = Button(parent=p, model='quad', scale=Vec2(.2,.1), text=str(i), color=color.tint(color.random_color(),-.6))
        b = terrain_models.HexPad(parent=p, scale=Vec2(.2,.1), text=str(i), color=color.tint(color.random_color(),-.6))
        #b.text_entity.scale=1
    t = time.time()
    terrain_models.hexgrid_layout(p.children, max_x=7, max_y=10, origin=(0, .5), spacing=(.15, 0))
    center = Entity(parent=camera.ui, model=Circle(), scale=.005, color=color.lime)



    camera = EditorCamera()
    app.run()