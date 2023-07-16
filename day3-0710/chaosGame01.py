import random
import numpy as np
import matplotlib.pyplot as plt


A = np.array([0, 0])
B = np.array([1, 1])
C = np.array([2, 0])


def midpoint(P1, P2) :
  return (P1 + P2)/2


numOfPoints = 1000000


currentPoint = np.array([2, 1])
listOfPoints = np.zeros([numOfPoints, 2])
#listOfPoints[0] = currentPoint
print(listOfPoints)


for i in range(numOfPoints) :
  num = int(random.random()*3)
  if num == 0 :
    newPoint = midpoint(currentPoint, A)
  elif num == 1 :
    newPoint = midpoint(currentPoint, B)
  else :
    newPoint = midpoint(currentPoint, C)
  listOfPoints[i] = newPoint
  currentPoint = newPoint


#print(listOfPoints)
x = listOfPoints[:,0]
y = listOfPoints[:,1]
fig, ax = plt.subplots()
ax.scatter(x, y, s=1)
plt.show()
