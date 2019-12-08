# https://adventofcode.com/2019/day/1
import math
import os

def process():
  data = readFile('input')
  cable1 = buildCable(data[0])
  cable2 = buildCable(data[1])
  nearestPoint = getNearestIntersection(cable1, cable2)
  print(nearestPoint)

#BRUTE FORCE POINT METHOD
def getNearestIntersection(cable1, cable2):
  intersections = set(cable1).intersection(set(cable2))

  # manhattan distance
  # closestPoint=(0,0)
  # closestDistance=math.inf
  # for intersection in intersections:
  #   distance = abs(0 - intersection[0]) + abs(0 - intersection[1])
  #   if (distance<closestDistance): 
  #     closestPoint = intersection
  #     closestDistance = distance
  # return (closestPoint[0], closestPoint[1], closestDistance)
  
  # step distance
  closestPoint=(0,0)
  closestDistance=math.inf
  for intersection in intersections:
    print('distance {} {} {}'.format(cable1.index(intersection), cable2.index(intersection), cable1.index(intersection) + cable2.index(intersection)))
    distance = cable1.index(intersection) + cable2.index(intersection) +2
    if (distance<closestDistance): 
      closestPoint = intersection
      closestDistance = distance
  return (closestPoint[0], closestPoint[1], closestDistance)

def buildCable(instructions):
  currentPoint = (0,0)
  cablePoints = []
  for instruction in instructions:
    direction = instruction[0]
    distance = int(instruction[1:])
    for i in range(distance):
      if(direction == 'D'):
          currentPoint = (currentPoint[0], currentPoint[1]-1)
      if(direction == 'U'):
          currentPoint = (currentPoint[0], currentPoint[1]+1)
      if(direction == 'L'):
          currentPoint = (currentPoint[0]-1, currentPoint[1])
      if(direction == 'R'):
          currentPoint = (currentPoint[0]+1, currentPoint[1])
      cablePoints.append(currentPoint)
  return cablePoints

def readFile(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    lines.append(line.split(','))
  return lines


if __name__ == "__main__":
  process()