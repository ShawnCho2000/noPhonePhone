# class HandTrackingModule():
def fistClosed(hand):
  coords = hand.landmark
  # print(hand)
  # print(hand.landmark[8])
  # print(hand.landmark[6])
  diff = coords[8].y - coords[6].y
  # print(coords[8].y - coords[6].y)
  return diff > 0

def fingersUp(hand):
  coords = hand.landmark
  fingers = []
  # Thumb 
  if(coords[4].x < coords[2].x):
    fingers.append(1)
  else:
    fingers.append(0)
  #pointer
  if(coords[8].y > coords[6].y):
    fingers.append(1)
  else:
    fingers.append(0)
  #middle
  if(coords[12].y > coords[10].y):
    fingers.append(1)
  else:
    fingers.append(0)
  #ring
  if(coords[16].y > coords[14].y):
    fingers.append(1)
  else:
    fingers.append(0)
  #pinky
  if(coords[20].y > coords[18].y):
    fingers.append(1)
  else:
    fingers.append(0)

  return fingers
