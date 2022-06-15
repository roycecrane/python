from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
class Shaders:
    def __init__(self):
        self._shaderPrograms = {}
        # if TF_V:
        #     print("Dictionary is not empty!")
        # else:
        #     print("Dictionary is empty!")
    def setProgram(self,vert,frag,name):
        vert_compiled = compileShader(vert, GL_VERTEX_SHADER)
        frag_compiled = compileShader(frag, GL_FRAGMENT_SHADER)
        self._shaderPrograms[name] = compileProgram(vert_compiled,frag_compiled)
    def getProgram(self,name):
        return self._shaderPrograms[name]