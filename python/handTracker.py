import cv2
import mediapipe as mp
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
  success, img = cap.read()

  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = hands.process(imgRGB)
  if results.multi_hand_landmarks:

    for handLMS in results.multi_hand_landmarks:
      #display hands
      mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS)
      # print(handLMS.landmark[8])

      #get fist close
      print(htm.fistClosed(handLMS))




  cv2.imshow("Image", img)
  cv2.waitKey(1)