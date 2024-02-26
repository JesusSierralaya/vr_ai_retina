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

        # cat vao --------------------------------------------
        self.vaos['cat'] = self.get_vao( # 'cat' --> 'new_object'
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cat'] # 'cat' --> 'new_object'
        )
        # cat vao END --------------------------------------------

        # skull vao --------------------------------------------
        self.vaos['skull'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['skull']
        )
        # skull vao END --------------------------------------------

        # duck vao --------------------------------------------
        self.vaos['duck'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['duck']
        )
        # duck vao END --------------------------------------------

        # grass vao --------------------------------------------
        self.vaos['grass'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['grass']
        )
        # grass vao END --------------------------------------------

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
