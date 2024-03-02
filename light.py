#!/usr/bin/env python3

import glm

class Light:
    def __init__(self, position=(3, 3, -3), color=(1, 1, 1)):
    # def __init__(self, position=(0, 35, -10), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        # intensities
        # self.Ia = 0.1 * self.color # ambient
        # self.Id = 0.8 * self.color # difuse
        # self.Is = 1.0 * self.color # specular

        self.Ia = 0.4 * self.color # ambient
        self.Id = 0.8 * self.color # difuse
        self.Is = 1.0 * self.color # specular
