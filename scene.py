#!/usr/bin/env python3

from model import *
from config import *

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

        # Object reference to test the fenomemon
        if object_ref:
            # add(Cube(app, tex_id='red', scale=(long_axis, .1, .1), pos=(0, 4, 2), rot=(20,40,0)))
            # add(Cube(app, tex_id='green', scale=(.1, long_axis, .1),pos=(0,4,2), rot=(20,40,0)))
            # add(Cube(app, tex_id='red', scale=(.1, .1, long_axis),pos=(0,4,2), rot=(0,0,0)))
            # add(Duck(app, pos=(0, 3,0), scale=(.06,.06,.06), rot=(-90, 0,30)))
            add(Fish(app, pos=forward, scale=(.1, .1, .1), rot=(-90, 0, -60)))


        # Reference cube
        if origin_cross:
            add(Cube(app, tex_id='red', scale=(long_axis, .1, .1)))
            add(Cube(app, tex_id='green', scale=(.1, long_axis, .1)))
            add(Cube(app, tex_id='blue', scale=(.1, .1, long_axis)))

        # floor
        if floor:
            n, s = 40, 2
            for x in range(-n, n, s):
                for z in range(-n, n, s):
                    add(Cube(app, pos=(x, -s +1, z), tex_id='tile'))

        # add(Cube(app, pos=(0, 5, -15), rot=(0, 0, 0), tex_id='red')) # red_2, test
        # add cube
        if cube_sample:
            add(Cube(app, pos=(0, 5, -5), rot=(45, 45, 0), tex_id='red')) # red_2, test
            # add(Venus(app, pos=(0, -2, -15))) # red_2, test
            # add(Duck(app, pos=(0, 0, -15))) # red_2, test
        # add line reference
        # if fix_camera and draw_lines_position:
        if draw_lines_position:
            add(Cube(app, tex_id='white', pos=camera_position, scale=(0.01, 0.01, 100)))
            add(Cube(app, tex_id='white', pos=camera_position, scale=(0.01, 100, 0.01)))
            add(Cube(app, tex_id='white', pos=camera_position, scale=(100, 0.01, 0.01)))
        # add line forward
        if draw_line_forward:
            add(Cube(app, tex_id='white', pos=forward, scale=(0.01, 100, 0.01)))
            add(Cube(app, tex_id='white', pos=forward, scale=(100, 0.01, 0.01)))

        # add lines
        from custom.line import Line
        # add(Line(app, (0.5, 5, 5), forward, 'blue'))  # Uses default tex_id and thickness
        # add(Line(app, (-0.5, 5, 5), forward, 'blue'))  # Uses default tex_id and thickness

        # add(Line(app, (1.5, 5, 5), forward, 'red'))  # Uses default tex_id and thickness
        # add(Line(app, (-1.5, 5, 5), forward, 'red'))  # Uses default tex_id and thickness

        #
        # Draw lines that indicate the camera position
        if draw_lines_cams:
            camera_position_left = list(camera_position)
            camera_position_left[0] = cam_separation_1/2
            camera_position_left = tuple(camera_position_left)

            camera_position_right = list(camera_position)
            camera_position_right[0] = -cam_separation_1/2
            camera_position_right = tuple(camera_position_right)

            add(Line(app,camera_position_left , forward, 'blue'))
            add(Line(app,camera_position_right , forward, 'blue'))
            add(Cube(app, tex_id='blue', pos=camera_position_left, scale=(0.001, 100, 0.001)))
            add(Cube(app, tex_id='blue', pos=camera_position_right, scale=(0.001, 100, 0.001)))

            camera_position_left = list(camera_position)
            camera_position_left[0] = cam_separation_2/2
            camera_position_left = tuple(camera_position_left)

            camera_position_right = list(camera_position)
            camera_position_right[0] = -cam_separation_2/2
            camera_position_right = tuple(camera_position_right)

            add(Line(app,camera_position_left , forward, 'red'))  # Uses default tex_id and thickness
            add(Line(app,camera_position_right , forward, 'red'))  # Uses default tex_id and thickness
            add(Cube(app, tex_id='red', pos=camera_position_left, scale=(0.001, 100, 0.001)))
            add(Cube(app, tex_id='red', pos=camera_position_right, scale=(0.001, 100, 0.001)))

        # add objects
        if objects_sample:
            dist = 20
            add(Venus(app, pos=(-dist, 0, -dist)))
            add(David(app, pos=(dist, 0, -dist), rot=(-90, 0, -50)))

            add(Duck(app, pos=(dist, 0, 0), rot=(-90, 0, -90)))

            add(Snake(app, pos=(dist, 0, dist), rot=(-90, 0, 90)))
            add(Frog(app, pos=(0, 0, dist), rot=(-90, 0, 180)))
            add(Monkey(app, pos=(-dist, 0, dist), rot=(-90, 0, 135)))

            add(Slrcamera(app, pos=(-dist, 0, 0), rot=(-90, 0, 90)))

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

    def render(self, left=False):
        for obj in self.objects:
            if stereo_view:
                obj.render(left)
            else:
                obj.render()
