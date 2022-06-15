import glfw
from OpenGL.GL import *
import numpy as np
import Win as WIN
import Input as IN_P
import Shaders as SHDR
import Constants as CONS
import glConfigure as GLC



def start(glDat,priceDat):
    EST = np.array([40.748333, -73.98527, 0.0])
    new_dat = 4.0 * np.array(glDat.astype(np) - EST,dtype=np.float32)
    num_points = new_dat.shape[0]

    for i in range(num_points):
        new_dat[0] = new_dat[0] * -1.0
        voidPtr = ctypes.c_void_p(0)

    win = WIN.Window(900.0,900.0)
    shdr = SHDR.Shaders()
    uni =  GLC.Uniforms()
    buff = GLC.Buffers()
    vtx =  GLC.VTXAttribs()

    shdr.setProgram(CONS.vertex_src,CONS.fragment_src,"1")
    uni.setUni(shdr.getProgram("1"),"time")
    uni.setUni(shdr.getProgram("1"),"Input")
    uni.setUni(shdr.getProgram("1"),"xyRes")

    buff.setBuff("pos",GL_ARRAY_BUFFER, new_dat)
    vtx.addAttrib(shdr.getProgram("1"),'pos',3,voidPtr)
    glUseProgram(shdr.getProgram("1"))
    vtx.enableAttrib('pos')
    # vtx.enableAttrib('col')


    in_p = IN_P.initalizeINP()
    glfw.set_key_callback(win.window, IN_P.keyboard)
    onRun(win,shdr,uni,num_points,in_p)
    print(new_dat[0])
    onWindowClosed(win)
    
def onRun(win,shdr,uni,size,INP):
    glPointSize(1.0)
    glClearColor(0, 0.0, 0.0, 0)
    glUseProgram(shdr.getProgram("1"))
    glfw.swap_interval(1)
    print(glGetError())

    # uni.updateUni3f("xyRes",res[0] , res[1] ,0.0)
    while not glfw.window_should_close(win.window):

        uni.updateUni3f("Input",INP.l_r, INP.u_d,INP.zoom)
        uni.updateUni1f("time",INP.toggle)

        glfw.poll_events()
        glDrawArrays(GL_POINTS, 0, size)
        glfw.swap_buffers(win.window)
        glClear(GL_COLOR_BUFFER_BIT)
def onWindowClosed(win):
    print(glGetError())
    del win.window
    print("\nDONE")



