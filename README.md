# coder_space
A good practice of the video https://www.youtube.com/watch?v=eJDIsFJN4OQ. At the moment, I'm just repeting the code to follow each step and apply it at my job.

## How to add a new model
1. (vbo.py) create the class: "class Object..."
2. (vbo.py) add the class to the dictionary: "self.vbo['new_object']..."
3. (vao.py) add the model to the vao dictionary: "self.vaos['new_object']..."
4. (texture.py) add the texture model to the dictionary: "self.textures['new_object']..."
5. (model.py) add the new model as a class: "class New_object(BaseModel)"
6. (scene.py) add the model to the scene: "add(New_object(app, ...)))"

### sites to download a model
1. https://free3d.com
