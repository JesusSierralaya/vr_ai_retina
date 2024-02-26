# coder_space
A good practice of the video https://www.youtube.com/watch?v=eJDIsFJN4OQ. At the moment, I'm just repeting the code to follow each step and apply it at my job.

## How to add a new model
1. (vbo.py) add the class to the dictionary: 
   - lines aprox 15-20
   - "self.vbos['object'] = ObjectVBO(ctx)" 

2. (vbo.py) create the class: 
   - Example in lines aprox 85 to 100
   - Copy the cat example at the end of the file: From # cat VBO --... to # cat VBO END ---
   - Change the name of the class "class ObjectVBO(BaseModel)..."
   - Change the .obj file "objs = pywavefront..."

3. (vao.py) add the model to the vao dictionary: 
   - lines aprox 35+
   - "self.vaos['object']..."
   - "vbo = self.vbo.vbos['object']"

4. (texture.py) add the texture model to the dictionary:
   - lines aprox 20+
   - "self.textures['object'] = self.get_texture(path='objects/object/object.jpg')"

5. (model.py) add the new model as a class: "class New_object(BaseModel)"
   - Copy the model. Lines aprox 62 to 88
   - paste at the end of the document
   - Change the class name, the vao_name and the tex_id
   "class Object(BaseModel): 
    def __init__(self, app, vao_name='object', tex_id='object',..."

6. (scene.py) add the model to the scene: 
   - "add(New_object(app, ...)))"

### sites to download a model
1. https://free3d.com
