'''
*********description*********
the main opengl application using shader ( programmable pipeline) with shader source string hard-coded inside.
'''
import opengl-window-class
from OpenGL.GL import *
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


my_PyGL_window.main_loop()
