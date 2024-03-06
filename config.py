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


# stereo
stereo_view = True
cam_separation = -.1 # not accurated
# cam_separation = -5

# invert direction to mirror mode
mirror_mode = False

# Camera position fix (no calibrated for movement)
fix_camera = False# Only for stereo_view = True
camera_position = (0, 5, 5)
forward = (0, 5, 2)
draw_lines_position = False
draw_line_forward = False

# cam change at x seconds
cam_toggle = False
toggle_interval= 3 # seconds
cam_separation_1 = .05
cam_separation_2 = .1

# draw lines cam separation
draw_lines_cams = False
test_cameras = False# fix_camera = True and cam_toggle = True

back = 0
# back = (-.025, 0, 1) # cam sep 1 / izq / (0, 5, 5) + (-.025, 0, 1) = (-.525, 5, 6)
# back = (-.050, 0, 2) # cam sep 1 / izq / (0, 5, 5) + (-.055, 0, 2)
# back = (-.05, 0, 1) # cam sep 2 / izq / (0, 5, 5) +
# back = (-.1, 0, 2) # cam sep 2 / izq / (0, 5, 5) +
#
# back = (.025, 0, 1) # cam sep 1 / der/
# back = (.055, 0, 2) # cam sep 1 / der/
# back = (.05, 0, 1) # cam sep 2 / der/
# back = (.1, 0, 2) # cam sep 2 / der/
