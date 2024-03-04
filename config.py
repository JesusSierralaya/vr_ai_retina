#!/usr/bin/env python3

# config.py

# Define surface range # render nothing 0 0
surface_from = 0
surface_to = 0
# parameters
invert_y = -1 # Invert vertical axis
position = (0, 25, -10)
rotation = (0, 0, 0) # y = 90 change the light
scale = (2, 12, 2)

# origin
origin_cross = False
long_axis = 100

# floor
floor = False

# objects
cube_sample = True
objects_sample = False

# stereo
stereo_view = True
cam_separation = -1

# Camera position fix (no calibrated for movement)
fix_camera = False# Only for stereo_view = True
camera_position = (0, 5, 5)
draw_lines_position = True
draw_line_forward = True
forward = (0, 5, -15)

# cam change at x seconds
cam_toggle = False
toggle_interval= 1 # seconds
cam_separation_1 = 0.5
cam_separation_2 = 1.5
