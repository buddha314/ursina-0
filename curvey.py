from ursina import *
import bezier

# run the app
if __name__ == '__main__':
    app = Ursina() 
    sky = Sky()
    #box1 = Entity(model='cube', color=color.red, position=(0, 0, 0))
    # Add origin point at right end of box1 I think
    # c = curve.CubicBezier(x1, y1, x2, y2)
    dot1 = Entity(model=Circle(8, mode='line', thickness=10), color=color.hsv(60,1,1,.3),
                  position = (0, 0, 0)
                  )
    c = curve.CubicBezier(0, 0.5, 1, 0.5)
    c2 = curve.CubicBezier(1, 0, 0, 1)
    print(c)

    curve_resolution = 64

    curve_renderer_1 = Entity(
            model=Mesh(vertices=[Vec3(i / curve_resolution, c.solve_curve_x(i / curve_resolution), 0) for i in range(curve_resolution+1)], mode='line', thickness=2),
            position=Vec3(0, 0, 0),
            color=color.red)
    curve_renderer_2 = Entity(
            model=Mesh(vertices=[Vec3(i / curve_resolution, c2.solve_curve_x(i / curve_resolution), 0) for i in range(curve_resolution+1)], mode='line', thickness=2),
            scale=2,
            position=Vec3(-1, 0, 0),
            color=color.blue)

    box2 = Entity(model='cube', color=color.blue, position=(2, 1, 0))
    box3 = Entity(model='cube', color=color.blue, position=(3, -1, 0))
    camera = EditorCamera()
    app.run()