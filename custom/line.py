# line.py

'''
Adds a line from one point to other
'''
import numpy as np
from model import Cube

def Line(app, start_point, end_point, tex_id='white', thickness=0.02):
    start_point = np.array(start_point)
    end_point = np.array(end_point)

    direction = end_point - start_point
    length = np.linalg.norm(direction)

    adjustment_factor = 0.5
    adjusted_length = length * adjustment_factor

    scale = (adjusted_length, thickness, thickness)  # Use thickness for the y and z dimensions
    position = (start_point + end_point) / 2

    angle_y = np.arctan2(-direction[2], direction[0])
    angle_z = np.arcsin(direction[1] / length)
    rotation = (0, np.degrees(angle_y), np.degrees(angle_z))  # Convert radians to degrees

    # Assuming you have a method to add objects that looks something like this
    return Cube(app, pos=position.tolist(), scale=scale, rot=rotation, tex_id=tex_id)
