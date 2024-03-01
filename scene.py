#!/usr/bin/env python3

from model import *
from config import stereo_view, floor, objects_sample

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

        # Reference cube
        add(Cube(app, tex_id=3, scale=(.1, 2, .1)))
        add(Cube(app, tex_id=3, scale=(2, .1, .1)))
        add(Cube(app, tex_id=3, scale=(.1, .1, 2)))

        # floor
        if floor:
            n, s = 40, 2
            for x in range(-n, n, s):
                for z in range(-n, n, s):
                    add(Cube(app, pos=(x, -s +1, z)))

        # add objects
        if objects_sample:
            dist = 20
            add(Slrcamera(app, pos=(-dist, 0, -dist), rot=(-90, 0, 45)))
            add(Venus(app, pos=(0, 0, -dist)))
            add(David(app, pos=(dist, 0, -dist), rot=(-90, 0, -50)))

            add(Duck(app, pos=(dist, 0, 0), rot=(-90, 0, -90)))

            add(Snake(app, pos=(dist, 0, dist), rot=(-90, 0, 90)))
            add(Frog(app, pos=(0, 0, dist), rot=(-90, 0, 180)))
            add(Monkey(app, pos=(-dist, 0, dist), rot=(-90, 0, 135)))

            add(Cat(app, pos=(-dist, 0, 0), rot=(-90, 0, 90)))

            add(Fish(app, pos=(0, dist*2, dist*2), rot=(-90, 0, 90)))
            add(Dolphin(app, pos=(dist*2, dist*2, 0), rot=(-90, 0, 0)))
            add(Turtle(app, pos=(-dist*2, dist*2, 0)))

        # Surfaces -------------------------------------------
        from config import surface_from, surface_to
        if surface_from > 0 and surface_to > 0:
            for i in range(surface_from, surface_to + 1):
                # Dynamically generate the class name for the Surface
                surface_class = globals()[f'Surface{i}']
                # Create an instance of the Surface with the specified 'pos'
                surface_instance = surface_class(app)
                # Add the surface instance to the application
                add(surface_instance)
        # Surfaces END -------------------------------------------


    # def render(self):
    #     for obj in self.objects:
    #         obj.render()

    def render(self, left=False):
        for obj in self.objects:
            if stereo_view:
                obj.render(left)
            else:
                obj.render()
