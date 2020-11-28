from render import Render
from texture import Texture
import os
dirname = os.path.dirname(__file__)
filename_texture = os.path.join(dirname, 'mars.bmp')
filename_obj = os.path.join(dirname, 'h.obj')
print(filename_texture)
gl = Render(800, 600)	
t = Texture(filename_texture)									
gl.load(filename_obj, (2.5, 2, 0), (150,150,150),  texture=t)
#gl.load('C:/Users/dsgsp/Documents/progra/graficas por computadora/tarea1/h.obj', (2.5, 2, 0), (150,150,150))
gl.display('./out.bmp')
