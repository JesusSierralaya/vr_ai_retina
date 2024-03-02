#!/usr/bin/env python3

"""
This module is the main entry point of the stereoscopic 3D graphics engine.
It handles initialization of the graphics engine and starts the main event loop.
"""

import glm
import pygame as pg
from config import stereo_view

FOV = 50 # deg
NEAR = 0.1
FAR = 100
SPEED = 0.01
SENSITIVITY = 0.05

class Camera:
    def __init__(self, app, position=(0, 0, 0), yaw=-90, pitch=0, cam_separation = 0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
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
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity

    def get_view_matrix(self, left=True):
        if not stereo_view:
            forward= self.position + self.forward
            print(forward)
            return glm.lookAt(self.position, forward, self.up)
        else:
            cam_offset = (self.cam_separation / 2) * (-1 if left else 1)
            cam_position = self.position + self.right * cam_offset
            return glm.lookAt(cam_position, cam_position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

    def print_view_matrix(self):
        if stereo_view:  # Check if stereo view is enabled
            print("Left Camera View Matrix:")
            left_view_matrix = self.get_view_matrix(left=True)
            for i in range(4):  # View matrix is 4x4
                for j in range(4):
                    print(f"{left_view_matrix[i][j]:6.2f}", end=" ")
                print()

            print("Right Camera View Matrix:")
            right_view_matrix = self.get_view_matrix(left=False)
            for i in range(4):  # View matrix is 4x4
                for j in range(4):
                    print(f"{right_view_matrix[i][j]:6.2f}", end=" ")
                print()
            print("\n")
        else:  # If not in stereo view, print the current view matrix
            print("View Matrix:")
            for i in range(4):  # View matrix is 4x4
                for j in range(4):
                    print(f"{self.m_view[i][j]:6.2f}", end=" ")
                print()
