# cam_toggle.py

"""
This module contains functionality to toggle the camera's separation distance based on timing.
"""

from config import cam_separation_1, cam_separation_2

# Initialize the last toggle time as a global variable to maintain state across calls
last_toggle_time = 0

def toggle_camera(camera, current_time, toggle_interval):
    """
    Toggles the camera separation based on the current time and the last toggle time.

    Parameters:
        camera: The Camera object whose separation we're toggling.
        current_time: The current time in seconds.
        toggle_interval: The interval between toggles in seconds.

    Returns:
        Updates the global last_toggle_time if the camera was toggled.
    """
    global last_toggle_time

    if current_time - last_toggle_time > toggle_interval:
        new_cam_separation = cam_separation_2 if camera.cam_separation == cam_separation_1 else cam_separation_1
        camera.cam_separation = new_cam_separation
        last_toggle_time = current_time

    return last_toggle_time
