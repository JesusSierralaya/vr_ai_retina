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

        # slr camera vao --------------------------------------------
        self.vaos['slr_camera'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['slr_camera']
        )
        # slr camera vao END --------------------------------------------

        # heart vao --------------------------------------------
        self.vaos['heart'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['heart']
        )
        # heart vao END --------------------------------------------

        # venus vao --------------------------------------------
        self.vaos['venus'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['venus']
        )
        # venus vao END --------------------------------------------

        # david vao --------------------------------------------
        self.vaos['david'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['david']
        )
        # david vao END --------------------------------------------

        # turtle vao --------------------------------------------
        self.vaos['turtle'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['turtle']
        )
        # turtle vao END --------------------------------------------

        # dolphin vao --------------------------------------------
        self.vaos['dolphin'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['dolphin']
        )
        # dolphin vao END --------------------------------------------

        # frog vao --------------------------------------------
        self.vaos['frog'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['frog']
        )
        # frog vao END --------------------------------------------

        # monkey vao --------------------------------------------
        self.vaos['monkey'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['monkey']
        )
        # monkey vao END --------------------------------------------

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()
