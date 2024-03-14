# cam_toggle.py

"""
Toggles the camera separation based on the current time and the last toggle time.
    Parameters:
   - camera: The Camera object whose separation we're toggling.
   - current_time: The current time in seconds.
   - last_toggle_time: The last time the camera was toggled.
   - toggle_interval: The interval between toggles in seconds.
    Returns:
   - last_toggle_time: Updated last toggle time if the camera was toggled, otherwise the same as input.
"""

from config import cam_separation_1, cam_separation_2
def toggle_camera(camera, current_time, last_toggle_time, toggle_interval):

    if current_time - last_toggle_time > toggle_interval:
        new_cam_separation = cam_separation_2 if camera.cam_separation == cam_separation_1 else cam_separation_1
        camera.cam_separation = new_cam_separation
        last_toggle_time = current_time
    return last_toggle_time
