'''
*********description*********
the main opengl application using shader ( programmable pipeline) with shader source string hard-coded inside.
'''
import opengl-window-class
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np


vertex_src = """
# version 330 core
in vec3 a_position;

void main()
{
	gl_Position = vec4(a_posotion, 1.0);
}
"""

fragment_src = """
# version 330 core
out vec4 out_color;

void main()
{
	out_color = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

my_PyGL_window = opengl-window-class.Window(1280, 720, "My PyOpenGL window")

vertices = [-0.5, -0.5, 0.0,
	     0.5, -0.5, 0.0,
	     0.0,  0.5, 0.0]

colors = [1.0, 0.0, 0.0,
	  0.0, 1.0, 0.0,
	  0.0, 0.0, 1.0]

np_vertices = np.array(vertices, dtype=np.float32)
np_colors   = np.array(colors  , dtype=np.float32)

# this internally use glCompileShader() and all the other necessary works to link a 
# shader program, decrease the coding complexity for programmers. 
shader_program_handle = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), \
				       compileShader(fragment_src, GL_FRAGMENT_SHADER))

glClearColor(0, 0.1, 0.1, 1)


# after an opengl context are created and all related drawing configuration complete, 
# we enter a loop probe for any user mouse click and key strike.
my_PyGL_window.main_loop()
