# Find Angle MBC

import math

AB = int(input())
BC = int(input())

Theta = math.atan(AB/BC)

print(str(int(round(math.degrees(Theta))))+"°")
