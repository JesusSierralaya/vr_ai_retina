#!/usr/bin/env python3

from model import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # # simple cubes
        add(Cube(app, tex_id=3))
        # add(Cube(app, tex_id=1, pos=(-2.5, 0, 0), rot=(45, 0, 0), scale=(1, 2, 1)))
        # add(Cube(app, tex_id=2, pos=(2.5, 0, 0), rot=(0, 0, 45), scale=(1, 1, 2)))

        # n, s = 30, 3
        # for x in range(-n, n, s):
        #     for z in range(-n, n, s):
        #         add(Cube(app, pos=(x, -s, z)))

        # add(Cat(app, pos=(0, -2, -10)))
        # add(Surface1(app, pos=(0, 2, -5)))
        # add(Surface2(app, pos=(0, 4, -5)))
        # add(Surface3(app, pos=(0, 6, -5)))
        # add(Surface4(app, pos=(0, 8, -5)))
        # add(Surface5(app, pos=(0, 10, -5)))
        # add(Surface6(app, pos=(0, 12, -5)))

        # Assuming 'app' is your application context and 'add' is a function to add surfaces
        from config import surface_from, surface_to
        for i in range(surface_from, surface_to + 1):
            # Calculate the y-coordinate for 'pos', starting at 2 and increasing by 2 each iteration
            # y_pos = i
            # Dynamically generate the class name for the Surface
            surface_class = globals()[f'Surface{i}']
            # Create an instance of the Surface with the specified 'pos'
            surface_instance = surface_class(app)
            # Add the surface instance to the application
            add(surface_instance)


    def render(self):
        for obj in self.objects:
            obj.render()
