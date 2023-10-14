# class HandTrackingModule():
def fistClosed(hand):
  coords = hand.landmark
  # print(hand)
  # print(hand.landmark[8])
  # print(hand.landmark[6])
  diff = coords[8].y - coords[6].y
  # print(coords[8].y - coords[6].y)
  return diff < 0
