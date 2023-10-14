from vedo import *
from time import time

def loop_func(event):
    print(event.keyPressed == "Right")
    if event.keyPressed == "Right":
      msh.rotate_z(0.1)
    if event.keyPressed == "Left":
      msh.rotate_z(-0.1)
    plt.render()
msh = Mesh("Ironman2.obj")
msh.texture("25.5_defaultMat_BaseColor.png", scale=0.1)
txt = Text2D(bg='yellow')
t0 = time()

plt = Plotter(axes=1)
plt += [msh, txt]
plt.add_callback("timer", loop_func)
plt.timer_callback("start")
plt.show()
plt.close()
