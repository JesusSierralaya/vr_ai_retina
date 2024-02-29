#!/usr/bin/env python3

from vbo import VBO
from shader_program import ShaderProgram

class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube']
        )

        # Surfaces vao --------------------------------
        from config import surface_from, surface_to
        if surface_from > 0 and surface_to > 0:
            for i in range(surface_from, surface_to+1):
                surface_key = f'surface_{i}'
                self.vaos[surface_key] = self.get_vao(
                    program=self.program.programs['default'],
                    vbo=self.vbo.vbos[surface_key]
                )
        # Surfaces vao END --------------------------------

        # objects vao --------------------------------
        self.vaos['cat'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cat']
        )
        self.vaos['venus'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['venus']
        )
        # objects vao END --------------------------------

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
