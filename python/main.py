import cv2
import mediapipe as mp
import HandTrackingModule as htm
import serial
# model stuff
from vedo import *
from time import time

# ---------------------------------------------- #
wCam, hCam = 640, 480
# ---------------------------------------------- #
startingHandPos = [[None, None, None],[None, None, None]]
startingModelPos = [[None, None, None],[None, None, None]]
prevAngle = None

arduino = serial.Serial(port='/dev/cu.usbmodem142401', baudrate=9600, timeout=0.1)

it = 0
# function that loops over and over, like a while true loop
def loop_func(event):

  try:
    sensorVal = arduino.read(arduino.in_waiting).decode()
    #idk why i have to do this, but it works
    num = int(sensorVal.partition('\n')[2].partition('\n')[0])
    global prevAngle
    if prevAngle == None:
      prevAngle = num
    elif prevAngle != num:
      if abs(prevAngle - num) < 150 and abs(prevAngle - num) > 1 and num > 0 and num < 649:
        plt.azimuth((prevAngle - num)/2)
        prevAngle = num
    else:
      plt.azimuth(0)
  except:
    pass

  # opencv hand tracking setup
  success, img = cap.read()
  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = hands.process(imgRGB)
  if results.multi_hand_landmarks:
    for handLMS in results.multi_hand_landmarks:
      isRightHand = htm.isRightHand(handLMS)
      msh = gauntlet
      if isRightHand:
        msh = ironman
      #display hands
      mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS)

      fingersUp = htm.fingersUp(handLMS)
      global startingHandPos
      global startingModelPos
      if fingersUp == [0, 0, 0, 0, 0]:
        if startingHandPos[isRightHand] == [None, None, None]:
          startingHandPos[isRightHand] = [handLMS.landmark[0].x, handLMS.landmark[0].y, handLMS.landmark[0].z]
          startingModelPos[isRightHand] = msh.pos()
        else:
          meshPosition = startingModelPos[isRightHand]
          movePos = [handLMS.landmark[0].x - startingHandPos[isRightHand][0], handLMS.landmark[0].y - startingHandPos[isRightHand][1], handLMS.landmark[0].z - startingHandPos[isRightHand][2]]
          msh.pos(meshPosition[0] - movePos[0]*5, meshPosition[1] - movePos[1]*5, meshPosition[2])
        # # move around

        #   print(msh.pos())
        #   print([handLMS.landmark[8].x, handLMS.landmark[8].y, handLMS.landmark[8].z])
        #   cur = msh.pos()
        #   cur[0] = (handLMS.landmark[8].x)
        #   cur[1] = (handLMS.landmark[8].y)
        #   #cur[2] = 10*(handLMS.landmark[8].z * -1)
        #   msh.pos(cur[0], cur[1])
      else:
        startingHandPos[isRightHand] = [None, None, None]
        startingModelPos[isRightHand] = [None, None, None]
        #todo move around model for WAN


      if fingersUp == [1, 1, 0, 0, 0]:
        #zoom in zoom out mode
        dist = htm.getThumbIndexDistance(handLMS)
        sensDown, sensUp = 0.06, 0.06
        scaledDist = max(1 - sensDown, min(dist, 1 + sensUp))
        msh.scale(scaledDist)
  plt.render()


  cv2.imshow("Image", img)
  cv2.waitKey(1)
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# 3d model display setup
ironman = Mesh("Ironman2.obj")
ironman.texture("25.5_defaultMat_BaseColor.png", scale=0.1)
txt = Text2D(bg='yellow')

gauntlet = Mesh("gauntlet.obj")
# gauntlet.scale(0.3)
gauntlet.texture("gauntlet.png", scale=0.1)
# gauntlet.rotate_z(170)
gauntlet.pos(-1, -1, 1)

plt = Plotter(axes=1)
plt += [ironman, txt]
plt += [gauntlet]

plt.add_callback("timer", loop_func)
plt.timer_callback("start")
plt.show()
plt.close()


