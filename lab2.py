from render import Render
from texture import Texture

gl = Render(800, 600)	
t = Texture('C:/Users/dsgsp/Documents/progra/graficas por computadora/tarea1/mars.bmp')									
gl.load('C:/Users/dsgsp/Documents/progra/graficas por computadora/tarea1/h.obj', (2.5, 2, 0), (150,150,150),  texture=t)
#gl.load('C:/Users/dsgsp/Documents/progra/graficas por computadora/tarea1/h.obj', (2.5, 2, 0), (150,150,150))
gl.display('out.bmp')
