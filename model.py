import moderngl as mgl
import numpy as np
import glm

class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self, left):
        self.update(left)
        self.vao.render()


class Cube(BaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self, left):
        self.texture.use()
        # self.program['camPos'].write(self.camera.position)
        # self.program['m_view'].write(self.camera.m_view)
        # self.program['m_model'].write(self.m_model)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.get_view_matrix(left))
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


# Surfaces Model -------------------------------------------------------------
class BaseSurface(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self, left):
        self.texture.use()
        # self.program['camPos'].write(self.camera.position)
        # self.program['m_view'].write(self.camera.m_view)
        # self.program['m_model'].write(self.m_model)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.get_view_matrix(left))
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

def create_surface_class(surface_id):
    class Surface(BaseSurface):
        from config import position, rotation, scale
        def __init__(self, app, tex_id=1, pos=position, rot=rotation, scale=scale):
            vao_name = f'surface_{surface_id}'
            super().__init__(app, vao_name, tex_id, pos, rot, scale)
    return Surface

# Dynamically create and assign Surface classes
from config import surface_from, surface_to
if surface_from > 0 and surface_to > 0:
    for i in range(surface_from, surface_to +1):
        class_name = f"Surface{i}"
        globals()[class_name] = create_surface_class(i)
# Surfaces Model END ------------------------------------------------------

# Object models -----------------------------------------------------------

class BaseObjectModel(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos, rot, scale):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self, left):
        self.texture.use()
        # self.program['camPos'].write(self.camera.position)
        # self.program['m_view'].write(self.camera.m_view)
        # self.program['m_model'].write(self.m_model)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.get_view_matrix(left))
        self.program['m_model'].write(self.m_model)

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use()
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

class Cat(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.5, .5, .5)):
        super().__init__(app, vao_name='cat', tex_id='cat', pos=pos, rot=rot, scale=scale)

class David(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.02, .02, .02)):
        super().__init__(app, vao_name='david', tex_id='david', pos=pos, rot=rot, scale=scale)

class Dolphin(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.3, .3, .3)):
        super().__init__(app, vao_name='dolphin', tex_id='dolphin', pos=pos, rot=rot, scale=scale)

class Duck(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.15, .15, .15)):
        super().__init__(app, vao_name='duck', tex_id='duck', pos=pos, rot=rot, scale=scale)

class Fish(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(1.5, 1.5, 1.5)):
        super().__init__(app, vao_name='fish', tex_id='fish', pos=pos, rot=rot, scale=scale)

class Frog(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(1.4, 1.4, 1.4)):
        super().__init__(app, vao_name='frog', tex_id='frog', pos=pos, rot=rot, scale=scale)

class Monkey(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.15, .15, .15)):
        super().__init__(app, vao_name='monkey', tex_id='monkey', pos=pos, rot=rot, scale=scale)

class Slrcamera(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.05, .05, .05)):
        super().__init__(app, vao_name='slrcamera', tex_id='slrcamera', pos=pos, rot=rot, scale=scale)

class Snake(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.4, .4, .4)):
        super().__init__(app, vao_name='snake', tex_id='snake', pos=pos, rot=rot, scale=scale)

class Turtle(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.4, .4, .4)):
        super().__init__(app, vao_name='turtle', tex_id='turtle', pos=pos, rot=rot, scale=scale)

class Venus(BaseObjectModel):
    def __init__(self, app, pos, rot=(-90, 0, 0), scale=(.05, .05, .05)):
        super().__init__(app, vao_name='venus', tex_id='venus', pos=pos, rot=rot, scale=scale)

# Object models END ------------------------------------------------------
