#!/usr/bin/env python3

"""
This module is the main entry point of the stereoscopic 3D graphics engine.
It handles initialization of the graphics engine and starts the main event loop.
"""

import glm
import pygame as pg
from config import stereo_view, fix_camera, mirror_mode, test_cameras, back

FOV = 50 # deg
NEAR = 0.1
FAR = 100
# SPEED = 0.01
# SENSITIVITY = 0.05
SPEED = 0.005
SENSITIVITY = 0.005

class Camera:
    # yaw = 90 to turn around becuase the yaw will change
    if mirror_mode:
        yaw = 90
    else:
        yaw = -90
    def __init__(self, app, position= (0, 5, 5), yaw=yaw, pitch=0, cam_separation = 0):
        self.app = app
        # Change the aspect ratio to take in account the size of the viewport instead of the window
        from main import VIEWPORT_SIZE
        self.aspect_ratio = VIEWPORT_SIZE[0] / VIEWPORT_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        # Negative yaw becuase change due to the mirror view on the stereoscope
        if mirror_mode:
            self.yaw = -yaw
        else:
            self.yaw = yaw
        self.pitch = pitch
        # Stereo ---------------
        self.cam_separation = cam_separation
        # view matrix
        # True for stereo view
        # False for simple view
        self.m_view = self.get_view_matrix(True if stereo_view else False)
        # projection matrix
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY
        self.pitch = max(-89, min(89, self.pitch))

    def update_camera_vectors(self):
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix(True if stereo_view else False)

    def move(self):
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        # if keys[pg.K_a]:
        if keys[pg.K_d]:
            if mirror_mode:
                self.position -= self.right * velocity
            else:
                self.position += self.right * velocity
        # if keys[pg.K_d]:
        if keys[pg.K_a]:
            if mirror_mode:
                self.position += self.right * velocity
            else:
                self.position -= self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity

    def get_view_matrix(self, left=True):
        if not stereo_view:
            return glm.lookAt(self.position, self.position + self.forward, self.up)
        else:
            if fix_camera:
                from config import forward, camera_position
                cam_offset = (self.cam_separation / 2) * (-1 if left else 1)
                cam_position = camera_position + self.right * cam_offset
                if test_cameras:
                    return glm.lookAt(cam_position + back, forward, self.up)
                else:
                    print(cam_position)
                    return glm.lookAt(cam_position, forward, self.up)
            else:
                cam_offset = (self.cam_separation / 2) * (-1 if left else 1)
                cam_position = self.position + self.right * cam_offset
                return glm.lookAt(cam_position, cam_position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
