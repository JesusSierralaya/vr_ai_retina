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
        # add other textures dictionary
        # self.textures['object'] = self.get_texture(path='objects/object/object.jpg')
        self.textures['cat'] = self.get_texture(path='objects/cat/20430_cat_diff_v1.jpg')
        self.textures['skull'] = self.get_texture(path='objects/skull/Skull.jpg')
        self.textures['duck'] = self.get_texture(path='objects/duck/12248_Bird_v1_diff.jpg')
        self.textures['grass'] = self.get_texture(path='objects/grass/10450_Rectangular_Grass_Patch_v1_Diffuse.jpg')
        self.textures['slr_camera'] = self.get_texture(path='objects/slr_camera/10124_SLR_Camera_V1_Diffuse.jpg')
        self.textures['heart'] = self.get_texture(path='objects/heart/12190_Heart_v1_L3.jpg')
        self.textures['venus'] = self.get_texture(path='objects/venus/statue.jpg')
        self.textures['david'] = self.get_texture(path='objects/david/DavidFixedDiff.jpg')
        self.textures['turtle'] = self.get_texture(path='objects/turtle/10042_Sea_Turtle_V1_Diffuse.jpg')
        self.textures['dolphin'] = self.get_texture(path='objects/dolphin/10014_dolphin_v1_Diffuse.jpg')
        self.textures['frog'] = self.get_texture(path='objects/frog/12268_banjofrog_diffuse.jpg')
        self.textures['monkey'] = self.get_texture(path='objects/monkey/12958_Spider_Monkey_diff.jpg')
        self.textures['snake'] = self.get_texture(path='objects/snake/10050_RattleSnake_v04.jpg')
        self.textures['fish'] = self.get_texture(path='objects/fish/13001_Ryukin_Goldfish_diff.jpg')
        # end dictionary

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
