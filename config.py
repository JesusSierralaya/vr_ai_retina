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
origin_cross = True
long_axis = 1

# floor
floor = False

# objects
cube_sample = False
objects_sample = True
object_ref = True

# stereo
stereo_view = True
cam_separation = -.1 # not accurated
# cam_separation = -5

# invert direction to mirror mode
mirror_mode = False

# Camera position fix (no calibrated for movement)
# # Only for stereo_view = True
fix_camera = True
camera_position = (0, 5, 5)
forward = (0, 5, 0)
draw_lines_position = False # camera position
draw_line_forward = True

# cam change at x seconds
cam_toggle = True
toggle_interval= 1 # seconds
# cam_separation_1 = .05
# cam_separation_2 = .1
cam_separation_1 = 1
cam_separation_2 = 2

# draw lines cam separation
draw_lines_cams = False
test_cameras = False # fix_camera = True and cam_toggle = True

# Test cameras transformation # test_cameras = True
# just works for camera_position = (0, 5, 5); forward = (0, 5, 0)
from math import atan, tan
increase_z = 1 # increase distance to explore the cameras
separation = cam_separation_1 # cam_separation_1 o _2
screen = -1 # left -1; right 1
tan_angle = tan(atan(camera_position[2]/(separation/2)))
new_x_position = ((camera_position[2] + increase_z)/tan_angle)-(separation/2)
back = (new_x_position*screen, 0, increase_z)
