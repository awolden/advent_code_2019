# https://adventofcode.com/2019/day/1
import math
import os
from collections import OrderedDict 

def process():
  data = readFile('input')
  # printDimensionalArr(data)
  visibleGrid = buildGridOfVisible(data)
  # printDimensionalArr(visibleGrid)
  laserPoint = getHighest(visibleGrid)
  print(laserPoint)
  degreeGrid = getVisibleAsteroids(visibleGrid, laserPoint)
  printDimensionalArr(degreeGrid)
  angleDict = buildAngleDict(degreeGrid)
  print(angleDict)
  cycleDestroyAsteroids(angleDict)


def cycleDestroyAsteroids(angleDict): 
  totalAsteroids = 0
  for key in angleDict:
    totalAsteroids += len(angleDict[key])

  destroyedCount = 0
  while destroyedCount < totalAsteroids:
    for key in angleDict:
      pointsAtAngle = angleDict[key]
      # I may need to order the pointsAtAngle array by distance from origin for more reliabilty
      if(not len(pointsAtAngle)):
        continue
      else:
        destroyed = pointsAtAngle.pop()
        destroyedCount += 1
        print(f'{destroyedCount} destroyed at: {destroyed}')



def calculateDistance(p1,p2):  
     dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)  
     return dist  

def removeClosest(arrOfPoints, origin):
  return arrOfPoints.sort(key=lambda x: calculateDistance(x,origin))[1:]

def buildAngleDict(grid):
  newDict = {}
  for y, row in enumerate(grid):
    for x, angle in enumerate(row):
      if(angle == None):
        continue
      if(angle in newDict):
        newDict[angle].append((x,y))
      else:
        newDict[angle] = [(x,y)]

  ordered = OrderedDict()
  sortedKeys = list(newDict.keys())
  sortedKeys.sort()
  for key in sortedKeys:
    ordered[key] = newDict[key]

  return ordered 

def normalizeAngle(angle):
  # return angle
  if angle >= 0:
    return angle + 90
  if angle < 0 and angle >= -90:
    return 90 + angle
  if angle < -90:
    return (angle + 90) + 360


def buildGridOfVisible(grid):
  yLength = len(grid)
  xLength = len(grid[0])
  degreeGrid = [[0 for i in range(xLength)] for j in range(yLength)]

  for y in range(yLength):
    for x in range(xLength):
      if (grid[y][x] == '.'):
        degreeGrid[y][x] = '.'
      else:
        degreeGrid[y][x] = countVisibleAsteroids(getVisibleAsteroids(grid, [x, y]))

  return degreeGrid

def getVisibleAsteroids(grid, currentPoint):
  yLength = len(grid)
  xLength = len(grid[0])

  degreeGrid = [[0 for i in range(xLength)] for j in range(yLength)]
  for y in range(yLength):
    for x in range(xLength):
      if (grid[y][x] == '.'):
        degreeGrid[y][x] = None
      else:
        degreeGrid[y][x] = round(getDegreeFromOrigin(currentPoint, (x, y)), 9)
  return degreeGrid

def countVisibleAsteroids(grid):
  flatList = [item for sublist in grid for item in sublist]
  return len(set(flatList))

def getHighest(grid):
  highest = 0
  highestPoint = ()
  yLength = len(grid)
  xLength = len(grid[0])
  for y in range(yLength):
    for x in range(xLength):
      if (grid[y][x] == '.'):
        continue
      if (grid[y][x] > highest):
        highest = grid[y][x]
        highestPoint = (x, y)
  print('highest', highest)      
  return highestPoint

def getDegreeFromOrigin(origin, destination):
  radian = math.atan2(destination[1] - origin[1], destination[0] - origin[0])
  return normalizeAngle(round(radian * 180 / math.pi, 6))

def printDimensionalArr(arr):
  string = ''
  for y in arr:
    for x in y:
      string += f'({x})'
    string += '\n'
  print(string)


def readFile(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    a = list(line.rstrip())
    lines.append(a)
  return lines

if __name__ == "__main__":
  process()