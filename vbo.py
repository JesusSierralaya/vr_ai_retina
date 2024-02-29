#!/usr/bin/env python3

import numpy as np
import moderngl as mgl
import pywavefront
import pandas as pd

class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['cat'] = CatVBO(ctx)
        # Dictionary
        self.vbos['surface_over_1'] = SurfaceOver1VBO(ctx)
        # Dictionary End
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

# SURFACES -------------------------------------------
# constants
scale = 2
layer = 1

class SurfaceOver1VBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        layer = 1
        X = pd.read_csv(f'surfaces_data/x_{layer}.txt',header=None)
        X = np.array(X*-scale)
        Y = pd.read_csv(f'surfaces_data/y_{layer}.txt',header=None)
        Y = np.array(Y*-scale)
        Z = pd.read_csv(f'surfaces_data/z_{layer}.txt',header=None)
        Z = np.array(Z*-scale)

        # swap axis
        Y, Z = Z, Y

        # Flatten and stack the X, Y, Z matrices to create the vertices
        vertices = np.column_stack([X.flatten(), Y.flatten(), Z.flatten()])

        def generate_indices_and_tex_coords(size):
            indices = []
            tex_coord_vertices = []

            # Generate indices and texture coordinates
            for y in range(size - 1):
                for x in range(size - 1):
                    # Add indices for two triangles (square) - note the reversed order
                    indices.append((y * size + x, (y + 1) * size + x, y * size + x + 1))
                    indices.append((y * size + x + 1, (y + 1) * size + x, (y + 1) * size + x + 1))

            for y in range(size):
                for x in range(size):
                    # Add texture coordinate for vertex
                    tex_coord_vertices.append((x / (size - 1), y / (size - 1)))

            return indices, tex_coord_vertices

        size = np.size(X[0])
        #print(size)
        indices, tex_coord_vertices = generate_indices_and_tex_coords(size)

        vertex_data = self.get_data(vertices, indices)

        # Create texture coordinates
        tex_coord_indices = indices  # Reuse the same indices for texture coordinates
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        # Create normals (assuming all normals point upwards in the Z direction)
        normals = [(0, 0, 1) for _ in range(size*size)]  # 16 vertices
        normals = [normals[i] for triangle in indices for i in triangle]  # repeat normals for each vertex
        normals = np.array(normals, dtype='f4')

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])

        return vertex_data
