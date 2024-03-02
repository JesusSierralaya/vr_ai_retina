#!/usr/bin/env python3

# config.py

# Define surface range # render nothing 0 0
surface_from = 0
surface_to = 0
# parameters
invert_y = -1 # Invert vertical axis
position = (0, 15, -5)
rotation = (0, 90, 0) # y = 90 change the light
scale = (2, 10, 2)

# origin
origin_cross = True
long_axis = 100

# objects
objects_sample = True

# floor
floor = True

# stereo
stereo_view = False
cam_separation = .5

# cam change at x seconds
cam_toggle = True
toggle_interval= 1 # seconds
cam_separation_1 = 0.5
cam_separation_2 = 5

# Camera position fix (no calibrated for movement)
fix_camera = True # Only for stereo_view = True
camera_position = (0, 5, 5)
draw_lines = True
forward = (0, 5, -15)
