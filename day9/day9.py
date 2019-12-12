# https://adventofcode.com/2019/day/1
import math
import os

def process():
  data = readFile('input')
  input = [2]
  immediateOutput = getRegister(data, 0, input)
  print(immediateOutput)

def getRegister(program, i = 0, input=[]):
  data = program
  complete = False
  paused = False
  finalOutput = 0
  relativeBase = 0
  while not complete and not paused:


    opcode = data[i]
    mode1 = 0
    mode2 = 0
    mode3 = 0

    opcodeStr = str(opcode)
    # print('str', opcodeStr, data)
    if(len(opcodeStr) > 1): 
      opcodeStr = opcodeStr.zfill(5)
      mode3 = int(opcodeStr[0:1])
      mode2 = int(opcodeStr[1:2])
      mode1 = int(opcodeStr[2:3])
      opcode = int(opcodeStr[3:])

    # print('opcode: {} modes: {}{}{}'.format(opcode, mode1, mode2, mode3))

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
      print('input', input)
      setValue(data, input.pop(0), mode1, i+1, relativeBase)
      i+=2
      continue
    if (opcode == 4):
      finalOutput = getValue(data, mode1, i+1, relativeBase)
      i+=2
      print(finalOutput)
      # return [finalOutput, i]
    if (opcode == 5):
      check = getValue(data, mode1, i+1, relativeBase)
      pointer = getValue(data, mode2, i+2, relativeBase)
      if(check > 0):
        i = pointer
      else:
        i+=3
      continue
    if (opcode == 6):
      check = getValue(data, mode1, i+1, relativeBase)
      pointer = getValue(data, mode2, i+2, relativeBase)
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