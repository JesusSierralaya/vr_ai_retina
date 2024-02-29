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

        # cat vao
        self.vaos['cat'] = self.get_vao( # 'cat' --> 'new_object'
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cat']
        )

        # Surfaces vao --------------------------------
        for i in range(1, 7):
            surface_key = f'surface_{i}'
            self.vaos[surface_key] = self.get_vao(
                program=self.program.programs['default'],
                vbo=self.vbo.vbos[surface_key]
            )
        # Surfaces vao END --------------------------------

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
