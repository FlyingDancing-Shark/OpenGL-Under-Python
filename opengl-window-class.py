'''
*********description*********

'''


import glfw     # thid-party python library handle opengl context initialization, mandatory for this class

# one possibly usage of this class in other ".py" file : 
# my_pyopengl_window = Window(1280, 720, "new pyopengl window")
class Window:
	
	# init() is running each time an instance of Window class is created.
	# according to Python Class convention, "self" is always the first argument of "__init__()" 
	def __init__(self, width:int, height:int, title:str):
    	if not glfw.init():
			raise Exception("GLFW can not be initialized !")
		
		
		# for the purpose of last two parameters, see the documentations of GLFW open source project.
		# and "self" refers to the new instance created of this class,
		# for example, "my_pyopengl_window._win"
		self._win = glfw.create_window(width, height, title, None, None) 
		
		if not self._win:		# this variable stored object similar to window handle or pointer in the traditional opengl window creation process.
			glfw.terminate()
			raise Exception("GLFW window can not be created !")
			
		glfw.set_window_pos(self._win, 400, 200)
		glfw.make_context_current(self._win)
	
	
	# invoke by caller at proper time
	def main_loop(self):
		
		# if user click on the cross button on the right top of a pyopengl window, this loop will exit and terminate the process.
		while not glfw.window_should_close(self._win):
			
			# detecting user mouse click on and key striking events, then react accordingly
			glfw.poll_events()
			
		    # one of the two buffers is used for back-end rendering, another is used for front-end display.
			glfw.swap_buffers(self._win)
		
		glfw.terminate()
		
# if this file (module) isn't import by other file, but running as an independently python program, 
# it should do the initialization automatically by itself.		
if __name__ == "__main__":
	win = Window(1280, 720, "My OpenGL window")
	win.main_loop()
	
