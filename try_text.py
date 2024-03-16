from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()


class Page(Entity):
    def __init__(self, name):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.7, 0.9),
            origin=window.center,
            color=color.white
        )
        self.name = name
        self.tooltip = Tooltip(self.name)
        self.tooltip.background.color = color.color(0,0,0,.8)
        self.output_parent = Entity(parent=self, scale=(1/5,1/8)) 

class BotPage(Page):
    def __init__(self, name='bot'):
        super().__init__(
            name=name
        )
        self.color = color.green
        self.position = (0.5, 0, .1)

class UserPage(Page):
    def __init__(self, name):
        super().__init__(
            name=name
        )
        self.color = color.azure
        self.position = (-0.5, 0, -.1)
        self.input_parent = Entity(parent=self, scale=(1.8,2))
        # https://www.ursinaengine.org/api_reference.html#InputField
        self.itxt = InputField(
            max_lines = 3,
            character_limit=100,
            parent = self.input_parent,    
            origin = window.center,
            position=(0, -.24, -0.2),
            #scale=(3,1),
            color=color.black,
            background=True, text='Type here'
        )


"""
class Banana(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture='banana',
            scale=.1,
            origin=(-.5,.5),
            position=(-.5,.5),
            color=color.white
        )
        self.tooltip = Tooltip('Banana')
        self.tooltip.background.color = color.color(0,0,0,.8)

def process_user_input(txt):
    if 'banana' in txt:
        b = Banana()
        bananas.append(b)
        print('Banana!')

def display_user_input():
    print(itxt.text)
    process_user_input(itxt.text)
    txt.text += "\n" + itxt.text
    itxt.text = ''

itxt = InputField(position=(0.5,0,0), scale=(.5,.1), background=True, text='Type here')
btn = Button(text='Click me', color=color.azure, scale=.25, x=-.5)
btn.on_click = display_user_input 
"""

# Works with either, but if no controller, it's flat and upside down... ?
#model = Entity(model='autumn_house.glb', scale=1, position=(0,0,0), collider='mesh')
#model = Entity(model='autumn_house/scene.gltf', scale=1, position=(0,0,0), collider='mesh')
#txt = Text(text='Hello World', postion=(0,1,0), background=True)
#player = FirstPersonController(position=(0,0,-3))
sky = Sky()


user_page = UserPage('user')
bot_page = BotPage()
app.run()
