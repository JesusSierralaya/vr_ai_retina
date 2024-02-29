#!/usr/bin/env python3

import numpy as np
import moderngl as mgl
import pywavefront
import pandas as pd

class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        # Dictionary surfaces ------------------------
        from config import surface_from, surface_to
        if surface_from > 0 and surface_to > 0:
            for i in range(surface_from, surface_to+1):
                surface_key = f'surface_{i}'
                self.vbos[surface_key] = SurfaceVBO(ctx, i)
        # Dictionary surfaces END ------------------------
        # Dictionary objects ------------------------
        self.vbos['cat'] = CatVBO(ctx)
        self.vbos['venus'] = VenusVBO(ctx)
        # Dictionary objects END ------------------------
    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.format: list = None

    def get_vertex_data(self): ...

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()

class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype = 'f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1), # 0, 1, 2, 3
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)] # 4, 5, 6, 7
        # triangles to make the cube
        indices = [(0, 2, 3), (0, 1, 2), # front face
                   (1, 7, 2), (1, 6, 7), # right face
                   (6, 5, 4), (4, 7, 6), # back face # (4, 7, 5) order important?
                   (3, 4, 5), (3, 5, 0), # left face
                   (3, 7, 4), (3, 2, 7), # up face
                   (0, 6, 1), (0, 5, 6)] # down face

        vertex_data = self.get_data(vertices, indices)

        tex_coord = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]

        tex_coord_data = self.get_data(tex_coord, tex_coord_indices)

        normals = [
            (0, 0, 1) * 6,
            (1, 0, 0) * 6,
            (0, 0, -1) * 6,
            (-1, 0, 0) * 6,
            (0, 1, 0) * 6,
            (0, -1, 0) * 6,
        ]
        normals = np.array(normals, dtype ='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])

        return vertex_data

# SURFACES VBO -------------------------------------------
class SurfaceVBO(BaseVBO):
    def __init__(self, ctx, surface_number):
        self.surface_number = surface_number
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        X = pd.read_csv(f'surfaces_data/x_{self.surface_number}.txt', header=None)
        Y = pd.read_csv(f'surfaces_data/y_{self.surface_number}.txt', header=None)
        Z = pd.read_csv(f'surfaces_data/z_{self.surface_number}.txt', header=None)
        from config import invert_y
        X = np.array(X * invert_y)
        Y = np.array(Y * invert_y)
        Z = np.array(Z * invert_y)

        # Swap axis
        Y, Z = Z, Y

        # Flatten and stack the X, Y, Z matrices to create the vertices
        vertices = np.column_stack([X.flatten(), Y.flatten(), Z.flatten()])

        def generate_indices_and_tex_coords(size):
            indices = []
            tex_coord_vertices = []

            for y in range(size - 1):
                for x in range(size - 1):
                    indices.append((y * size + x, (y + 1) * size + x, y * size + x + 1))
                    indices.append((y * size + x + 1, (y + 1) * size + x, (y + 1) * size + x + 1))

            for y in range(size):
                for x in range(size):
                    tex_coord_vertices.append((x / (size - 1), y / (size - 1)))

            return indices, tex_coord_vertices

        size = np.size(X[0])
        indices, tex_coord_vertices = generate_indices_and_tex_coords(size)

        # Duplicate vertices for the second surface
        vertices_double = np.vstack([vertices, vertices])

        # Reverse indices for the second set of triangles
        indices_double = indices + [(i[2] + len(vertices), i[1] + len(vertices), i[0] + len(vertices)) for i in indices]

        # Generate normals for both sides, flipping them for the second set
        normals = [(0, 0, 1) for _ in range(len(vertices))] + [(0, 0, -1) for _ in range(len(vertices))]
        normals = [normals[i] for triangle in indices_double for i in triangle]
        normals = np.array(normals, dtype='f4')

        vertex_data = self.get_data(vertices_double, indices_double)
        tex_coord_data = self.get_data(tex_coord_vertices * 2, indices_double)  # Duplicate texture coords for the second surface

        # Combine the vertex attributes
        vertex_data = np.hstack([tex_coord_data, normals, vertex_data])

        return vertex_data

# SURFACES VBO END -------------------------------------------

# OBJECTS VBO-------------------------------------------
class CatVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/cat/20430_Cat_v1_NEW.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class VenusVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/venus/12328_Statue_v1_L2.obj', cache=True, parse=True) # Location of the .obj
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data
# OBJECTS VBO END -------------------------------------------
