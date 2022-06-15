from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader


class Uniforms:
    def __init__(self):
        self._unis = {}
    def setUni(self,program,name):
       self._unis[name] = glGetUniformLocation(program, name)
    def updateUni1f(self,name,val):
         glUniform1f( self._unis[name],val) 
    def updateUni3f(self,name,v1,v2,v3):
        glUniform3f(self._unis[name] ,v1,v2,v3) 

class Buffers:
    def __init__(self):
        self._buffs = {}
    def setBuff(self,name,type,data):
        self._buffs[name] = glGenBuffers(1)
        print(data.nbytes/data[0].nbytes)


        glBindBuffer(type, self._buffs[name])
        glBufferData(type, data.nbytes, data, GL_STATIC_DRAW)
        print('ERROR',glGetError())
    def getBuff(self,name):
        return self._buffs[name]
        
class VTXAttribs:
    def __init__(self):
        self._attribLoc = {}
    def addAttrib(self,shader,name,size,v):
        self._attribLoc[name] = glGetAttribLocation(shader, name)
        glEnableVertexAttribArray(self._attribLoc[name])
        glVertexAttribPointer(len(self._attribLoc)-1, size, GL_FLOAT, GL_FALSE, 0, v)
        print('ERROR',glGetError())

    def enableAttrib(self, name):
        glEnableVertexAttribArray(self._attribLoc[name])
        print('ERROR',glGetError())
