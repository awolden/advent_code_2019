# https://adventofcode.com/2019/day/1
import math
import os

#diiiiirty fix
#I need to rewrite the intcode machine
relativeBase = 0

def process():
  data = readFile('input').copy()
  register = 0
  outputCache = {
    (0, 0): 1
  }
  outputBuffer = []
  currentDirection = '^'
  currentLocation = (0, 0)
  complete = False
  while not complete:
    currentTileColor = outputCache.get(currentLocation, 0)
    # print(f'currentLocation: {currentLocation}, currentTileColor: {currentTileColor}')
    immediateOutput = getRegister(data, register, [currentTileColor])
    # print(f'immediate output {immediateOutput}')
    if(immediateOutput[1]):
      register = immediateOutput[1]
      output = immediateOutput[0]
      outputBuffer.append(output)
      if(len(outputBuffer) == 2):
        outputCache[currentLocation] = outputBuffer[0]
        newDir = outputBuffer[1]
        if(currentDirection == '^'):
          currentDirection = '<' if newDir == 0 else '>'
          currentLocation = (currentLocation[0]-1, currentLocation[1]) if newDir == 0 else (currentLocation[0]+1, currentLocation[1])
        elif(currentDirection == '<'):
          currentDirection = 'v' if newDir == 0 else '^'
          currentLocation = (currentLocation[0], currentLocation[1]+1) if newDir == 0 else (currentLocation[0], currentLocation[1]-1)
        elif(currentDirection == '>'):
          currentDirection = '^' if newDir == 0 else 'v'
          currentLocation = (currentLocation[0], currentLocation[1]-1) if newDir == 0 else (currentLocation[0], currentLocation[1]+1)
        elif(currentDirection == 'v'):
          currentDirection = '>' if newDir == 0 else '<'
          currentLocation = (currentLocation[0]+1, currentLocation[1]) if newDir == 0 else (currentLocation[0]-1, currentLocation[1])
        # print(f'output buffer {outputBuffer}')
        outputBuffer = []

    elif(not immediateOutput[1]):
      complete = True
  # print(outputCache, len(outputCache.keys()))
  drawMap(outputCache)


def drawMap(map):
  leftBound = 0
  rightBound = 0
  topBound = 0
  bottomBound = 0
  for v,k in enumerate(map):
    x, y = k[0], k[1]
    if(x < leftBound):
      leftBound = x
    if(x > rightBound):
      rightBound = x
    if(y > topBound): 
      topBound = y
    if(y < bottomBound):
      bottomBound = y

  for y in range(bottomBound, topBound+1, 1):
    row = ''
    for x in range(leftBound, rightBound, 1):
      if(map.get((x, y), 0) == 1):
        row += 'X'
      else:
        row += ' '
    print(row)
  print(topBound, rightBound, bottomBound, leftBound)


def getRegister(program, i = 0, input=[]):
  data = program
  complete = False
  paused = False
  finalOutput = 0
  global relativeBase
  while not complete and not paused:

    opcode = data[i]
    mode1 = 0
    mode2 = 0
    mode3 = 0

    opcodeStr = str(opcode)
    # print('str', opcodeStr)
    if(len(opcodeStr) > 1): 
      opcodeStr = opcodeStr.zfill(5)
      mode3 = int(opcodeStr[0:1])
      mode2 = int(opcodeStr[1:2])
      mode1 = int(opcodeStr[2:3])
      opcode = int(opcodeStr[3:])

    # print('i: {}, opcode: {} modes: {}{}{}'.format(i, opcode, mode1, mode2, mode3))

    if (opcode == 1):
      add1 = getValue(data, mode1, i+1, relativeBase)
      add2 = getValue(data, mode2, i+2, relativeBase)
      result = add1 + add2
      setValue(data, result, mode3, i+3, relativeBase)
      i+=4
      continue
    if (opcode == 2):
      multi1 = getValue(data, mode1, i+1, relativeBase)
      multi2 = getValue(data, mode2, i+2, relativeBase)
      result = multi1 * multi2
      setValue(data, result, mode3, i+3, relativeBase)
      i+=4
      continue
    if (opcode == 3):
      # print('input', input)
      setValue(data, input.pop(0), mode1, i+1, relativeBase)
      i+=2
      continue
    if (opcode == 4):
      finalOutput = getValue(data, mode1, i+1, relativeBase)
      i+=2
      # print(finalOutput)
      return [finalOutput, i]
    if (opcode == 5):
      check = getValue(data, mode1, i+1, relativeBase)
      pointer = getValue(data, mode2, i+2, relativeBase)
      if(check != 0):
        i = pointer
      else:
        i+=3
      continue
    if (opcode == 6):
      check = getValue(data, mode1, i+1, relativeBase)
      pointer = getValue(data, mode2, i+2, relativeBase)
      # print('foo', check, pointer, mode2, data[i+2] + relativeBase)
      if(check == 0):
        i = pointer
      else:
        i+=3
      continue
    if (opcode == 7):
      first = getValue(data, mode1, i+1, relativeBase)
      second = getValue(data, mode2, i+2, relativeBase)
      result = 1 if (first < second) else 0
      setValue(data, result, mode3, i+3, relativeBase)
      i+=4
      continue
    if (opcode == 8):
      first = getValue(data, mode1, i+1, relativeBase)
      second = getValue(data, mode2, i+2, relativeBase)
      result = 1 if (first == second) else 0
      setValue(data, result, mode3, i+3, relativeBase)
      i+=4
      continue
    if (opcode == 9):
      relativeBase += getValue(data, mode1, i+1, relativeBase)
      i+=2
      continue
    if (opcode == 99):
      complete = True
      return [finalOutput, None]
    raise Exception(f'{opcode} not a valid opcode')

def setValue(data, value, mode, i, base):
  if(mode == 0):
    safeFillArray(data, data[i])
    data[data[i]] = value
  elif(mode == 1):
    # this should never happen
    print('set Value should never be immediate')
  elif(mode == 2):
    safeFillArray(data, data[i] + base)
    data[data[i] + base] = value

def safeFillArray(arr, i):
  while len(arr) <= i:
    arr.append(0)

def getValue(data, mode, i, base):
  if(mode == 0):
    safeFillArray(data, data[i])
    return data[data[i]]
  elif(mode == 1):
    return data[i]
  elif(mode == 2):
    safeFillArray(data, data[i] + base)
    print('inget', data[i], data[i] + base)
    return data[data[i] + base]


def readFile(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  opcodes = f.read().split(',')
  return [int(x) for x in opcodes]

def loadPermutations(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    a = line.rstrip().split(',')

    lines.append([int(x) for x in a])
  return lines


if __name__ == "__main__":
  process()