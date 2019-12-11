import os
import math
from collections import Counter 

def process():
  data = readFile('input')
  layers = createLayers(data, 25, 6)
  print(layers)
  # part 1
  # targetLayer = findLayerWithFewestChar(layers, '0')
  # count = Counter(targetLayer)
  # print(count['1'] * count['2'])

  imageLayer = deriveImage(layers)
  printLayer(imageLayer, 25, 6)
  print(imageLayer)


def printLayer(data, x, y):
  data = list(data)
  string = ''
  while len(data):
    for iY in range(y):
      for iX in range(x):
        string += getPixel(data.pop(0))
      string += '\n'
  print(string)


def getPixel(pixel):
  if (pixel == '2'):
    return ' '
  if (pixel == '1'):
    return '1'
  if (pixel == '0'):
    return ' '
  return ''
  
def deriveImage(layers):
  length = len(layers[0])
  canonicalLayer = []
  for i in range(length):
    color = '2'
    j = 0
    while color == '2':
      color = layers[j][i]
      j+=1

    canonicalLayer.append(color)
  return canonicalLayer

def findLayerWithFewestChar(layers, char):
  targetLayer = None
  lowestCharCount = math.inf
  for layer in layers:
    count = Counter(layer)
    charCount = count['0']
    if (charCount < lowestCharCount):
      lowestCharCount = charCount
      targetLayer = layer
  return targetLayer


def createLayers(data, x, y):
  data = list(data)
  layers = []
  while len(data):
    layer = []
    for iY in range(y):
      for iX in range(x):
        layer.append(data.pop(0))
    layers.append(layer)
  return layers


def readFile(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  return f.read()

if __name__ == "__main__":
  process()