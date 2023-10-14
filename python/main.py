import cv2
import mediapipe as mp
import HandTrackingModule as htm

# ---------------------------------------------- #
# model stuff
from vedo import *
from time import time


# function that loops over and over, like a while true loop
def loop_func(event):
  # print(event)
  # global prev
  # if event.keyPressed != prev and event.keyPressed != None:

  #   prev = event.keyPressed
  #   print(prev)
  #   if event.keyPressed == "Up":
  #     # cur = msh.pos()
  #     # msh.pos(cur[0], cur[1] + 0.1, cur[2])
  #     cur = msh.scale()
  #     msh.scale(cur*1.02)
  #   if event.keyPressed == "Down":
  #     cur = msh.pos()
  #     msh.pos(cur[0], cur[1] - 0.1, cur[2])
  #   if event.keyPressed == "Right":
  #     msh.rotate_z(0.1)
  #   if event.keyPressed == "Left":
  #     msh.rotate_z(-0.1)
  #   plt.render()



  # opencv hand tracking setup
  success, img = cap.read()
  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = hands.process(imgRGB)
  if results.multi_hand_landmarks:
    for handLMS in results.multi_hand_landmarks:
      #display hands
      mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS)
      #get fist close
      print(htm.fistClosed(handLMS))
      if htm.fistClosed(handLMS):
        msh.rotate_z(0.5)
        plt.render()
      else:
        msh.rotate_z(-0.5)
        plt.render()

  cv2.imshow("Image", img)
  cv2.waitKey(1)
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# 3d model display setup
msh = Mesh("Ironman2.obj")
msh.texture("25.5_defaultMat_BaseColor.png", scale=0.1)
txt = Text2D(bg='yellow')

plt = Plotter(axes=1)
plt += [msh, txt]

plt.add_callback("timer", loop_func)
plt.timer_callback("start")
plt.show()
plt.close()


