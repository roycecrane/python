import glfw

class Window:
    """INPUT: (X , Y) RESOLUTION. THIS INIT MUST BE CALLED BEFORE USING OPENGL"""
    def __init__(self,xRes, yRes):
        self._xRes = xRes
        self._yRes = yRes
        if not glfw.init():
            raise Exception("GLFW FAILURE")
        self._window = glfw.create_window(int(xRes), int(yRes), "MANDELBROT ZOOM", None, None)
        if not self._window:
            glfw.terminate()
            raise Exception("WINDOW FAILURE")
        glfw.make_context_current(self._window)
    @property
    def window(self):
        return self._window
    @property
    def xyRes(self):
        return self._xRes, self._yRes
    @window.deleter
    def window(self):
        glfw.terminate()
        del self._window