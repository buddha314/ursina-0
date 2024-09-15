from ursina import *
from crafting import models
from ursina.prefabs.first_person_controller import FirstPersonController

if __name__ == "__main__":
    s1 = models.Stone()
    w1 = models.Wood()
    app = Ursina()
    camera = EditorCamera()
    app.run()