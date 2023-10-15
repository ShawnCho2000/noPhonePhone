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
