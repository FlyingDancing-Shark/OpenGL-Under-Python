'''
*********description*********
the main opengl application using shader ( programmable pipeline) with shader source string hard-coded inside.
'''
import opengl-window-class
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# "vertex_in_color" 
vertex_src = """
# version 330 core
in  vec3  a_position;

in  vec3  vertex_in_color;
out vec3  vertex_out_color;

void main()
{
	gl_Position = vec4(a_posotion, 1.0);
	vertex_out_color = vertex_in_color;
}
"""

fragment_src = """
# version 330 core
in   vec3  vertex_out_color; 
out  vec4  fragment_out_color;

void main()
{
	fragment_out_color = vec4(vertex_out_color, 1.0);
}
"""

my_PyGL_window = opengl-window-class.Window(1280, 720, "My PyOpenGL window")


vertices = [-0.5, -0.5, 0.0,	# vertex coordinates
	     0.5, -0.5, 0.0,
	     0.0,  0.5, 0.0,
	     1.0,  0.0, 0.0,	# color values (offest = 36 bytes)
	     0.0,  1.0, 0.0,
	     0.0,  0.0, 1.0]

""" 
# this rearrange with require re-compute the "stride" and "offset" argument of 
# "glVertexAttribPointer()", as I gave the # comment in corresponding statement 

vertices = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,	# each strides 24 bytes	
	     0.5, -0.5, 0.0, 0.0, 1.0, 0.0,	
	     0.0,  0.5, 0.0, 0.0, 0.0, 1.0]
	     		     # color begins at offset = 12 bytes
"""

np_vertices = np.array(vertices, dtype=np.float32)

# this internally use glCompileShader() and all the other necessary works(calling chain)
# to link a shader program, decrease the coding complexity for programmers. 
shader_program_handle = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), \
				       compileShader(fragment_src, GL_FRAGMENT_SHADER))

# vertex buffer object creation logic
# notice that in C/C++ programs, this function need a 2nd argument to store the buffer 
# name, but Python give us unprecedented flexibility and convenience for variable 
# declaration so that's enough to pass only one parameter in PyOpenGL environment
VBO = glGenBuffers(1)
glBindBuffers(GL_ARRAY_BUFFER, VBO)

# "np_vertices.nbytes" store the same information as expression "len(np_vertices) * 4"
# which is 72 bytes
glBufferData(GL_ARRAY_BUFFER, len(np_vertices) * 4, np_vertices, GL_STATIC_DRAW)

position = glGetAttribLocation(shader_program_handle, "a_position")
glEnableVertexAttribArray(position)
glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(0))
# glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

color = glGetAttribLocation(shader_program_handle, "vertex_in_color")
glEnableVertexAttribArray(color)
glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(36))
# glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))

glUseProgram(shader_program_handle)
glClearColor(0, 0.1, 0.1, 1)


# after an opengl context are created and all related drawing configuration complete, 
# we enter a loop probe for any user mouse click and key strike.
my_PyGL_window.main_loop()
