import glfw
class INPUT:
    def __init__(self):
        self.l_r= 0.0
        self.u_d= 0.0
        self.zoom= 10.0
        self.toggle= 0.0 
        self.mouseX = 0.0
        self.mouseY = 0.0
in_pk = None
def initalizeINP():
    global in_pk
    in_pk = INPUT()
    return in_pk

def keyboard(window, key, scancode, action, mods):
    moveAmt = 0.01
    if key == glfw.KEY_W:
        in_pk.u_d += moveAmt
    if key == glfw.KEY_S:
        in_pk.u_d -= moveAmt
    if key == glfw.KEY_D:
        in_pk.l_r += moveAmt
    if key == glfw.KEY_Q:
        in_pk.zoom += moveAmt
    if key == glfw.KEY_E:
        in_pk.zoom -= moveAmt
    if key == glfw.KEY_ENTER:
        in_pk.toggle += 1.0
    if key == glfw.KEY_SPACE:
        in_pk.toggle -= 1.0
    elif key == glfw.KEY_A:
        in_pk.l_r -= moveAmt