from vedo import *
from time import time

prev = "None"

def loop_func(event):
  print(event)
  global prev
  if event.keyPressed != prev and event.keyPressed != None:

    prev = event.keyPressed
    print(prev)
    if event.keyPressed == "Up":
      # cur = msh.pos()
      # msh.pos(cur[0], cur[1] + 0.1, cur[2])
      cur = msh.scale()
      msh.scale(cur*1.02)
    if event.keyPressed == "Down":
      cur = msh.pos()
      msh.pos(cur[0], cur[1] - 0.1, cur[2])
    if event.keyPressed == "Right":
      msh.rotate_z(0.1)
    if event.keyPressed == "Left":
      msh.rotate_z(-0.1)
    plt.render()

msh = Mesh("Ironman2.obj")
msh.texture("25.5_defaultMat_BaseColor.png", scale=0.1)
txt = Text2D(bg='yellow')

plt = Plotter(axes=1)
plt += [msh, txt]
plt.add_callback("timer", loop_func)
plt.timer_callback("start")
plt.show()
plt.close()
