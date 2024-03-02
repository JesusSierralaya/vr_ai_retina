#!/usr/bin/env python3

import pygame as pg
import moderngl as mgl

class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/img.png')
        self.textures[1] = self.get_texture(path='textures/img_1.png')
        self.textures[2] = self.get_texture(path='textures/img_2.png')
        self.textures['test'] = self.get_texture(path='textures/test.png')
        self.textures['tile'] = self.get_texture(path='textures/tile.jpg')

        # colors
        self.textures['red'] = self.get_texture(path='textures/red.png')
        self.textures['red_2'] = self.get_texture(path='textures/red_2.jpg')
        self.textures['green'] = self.get_texture(path='textures/green.png')
        self.textures['blue'] = self.get_texture(path='textures/blue.png')
        self.textures['white'] = self.get_texture(path='textures/white.png')

        # surface textures
        self.textures['cm'] = self.get_texture(path='textures/surface_cm.jpeg')

        # object textures ------------------------------------------
        self.textures['cat'] = self.get_texture(path='objects/cat/20430_cat_diff_v1.jpg')
        self.textures['david'] = self.get_texture(path='objects/david/DavidFixedDiff.jpg')
        self.textures['dolphin'] = self.get_texture(path='objects/dolphin/10014_dolphin_v1_Diffuse.jpg')
        self.textures['duck'] = self.get_texture(path='objects/duck/12248_Bird_v1_diff.jpg')
        self.textures['fish'] = self.get_texture(path='objects/fish/13001_Ryukin_Goldfish_diff.jpg')
        self.textures['frog'] = self.get_texture(path='objects/frog/12268_banjofrog_diffuse.jpg')
        self.textures['monkey'] = self.get_texture(path='objects/monkey/12958_Spider_Monkey_diff.jpg')
        self.textures['slrcamera'] = self.get_texture(path='objects/slrcamera/10124_SLR_Camera_V1_Diffuse.jpg')
        self.textures['snake'] = self.get_texture(path='objects/snake/10050_RattleSnake_v04.jpg')
        self.textures['turtle'] = self.get_texture(path='objects/turtle/10042_Sea_Turtle_V1_Diffuse.jpg')
        self.textures['venus'] = self.get_texture(path='objects/venus/statue.jpg')
        # object textures END ------------------------------------------

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # improve the quality of the textures
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]
