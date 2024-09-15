from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from direct.actor.Actor import Actor
#player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=2)


if __name__ == "__main__":
    app = Ursina()
    entity = Entity(position=Vec3(0,0,0))
    entity.rotation_x = -90
    entity.rotation_y = 193
    actor = Actor('assets/Cute_Demon.glb')
    actor.reparent_to(entity)
    #entity.look_at(camera.position)
    #entity.look_at(Vec3(-1,0,1))
    camera.position=(0,0,-100)
    print("animations: ")
    anims = actor.get_anim_names()
    print(actor.get_anim_names())
    actor.loop(anims[0])
    app.run()