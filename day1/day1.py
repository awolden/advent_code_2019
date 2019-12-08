# https://adventofcode.com/2019/day/1
import math
import os

def process():
  data = readFile('input')

  sum = 0

  for module in data:
    print('starting mass {}'.format(module))
    fuelMass = module
    while fuelMass > 0:
      fuelMass = math.floor(fuelMass / 3) - 2
      print('next mass {}'.format(fuelMass))
      if(fuelMass > 0):
        sum += fuelMass
    

  print(sum)

def readFile(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    lines.append(line)
  return [int(x) for x in lines]

if __name__ == "__main__":
  process()