import math

# class HandTrackingModule():
def fistClosed(hand):
  coords = hand.landmark
  # print(hand)
  # print(hand.landmark[8])
  # print(hand.landmark[6])
  diff = coords[8].y - coords[6].y
  # print(coords[8].y - coords[6].y)
  return diff > 0

def getThumbIndexDistance(hand):
  coords = hand.landmark
  # print([coords[4].x, coords[4].y],[coords[8].x, coords[8].y])
  scale =math.dist([coords[4].x, coords[4].y],[coords[2].x, coords[2].y])
  dist = math.dist([coords[4].x, coords[4].y],[coords[8].x, coords[8].y])
  return dist/scale

def fingersUp(hand):
  coords = hand.landmark
  fingers = []
  isRight = isRightHand(hand)

  # Thumb
  if(coords[4].x < coords[2].x):
    if isRight:
      fingers.append(0)
    else:
      fingers.append(1)
  else:
    if isRight:
      fingers.append(1)
    else:
      fingers.append(0)
  #pointer
  if(coords[8].y > coords[6].y):
    fingers.append(0)
  else:
    fingers.append(1)
  #middle
  if(coords[12].y > coords[10].y):
    fingers.append(0)
  else:
    fingers.append(1)
  #ring
  if(coords[16].y > coords[14].y):
    fingers.append(0)
  else:
    fingers.append(1)
  #pinky
  if(coords[20].y > coords[18].y):
    fingers.append(0)
  else:
    fingers.append(1)

  return fingers


def isRightHand(hand):
  coords = hand.landmark
  return (coords[5].x - coords[17].x) > 0