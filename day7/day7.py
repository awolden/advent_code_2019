# https://adventofcode.com/2019/day/1
import math
import os

INPUT = [5]

def process():
  data = readFile('input')
  realPermutations = loadPermutations('permutations')
  highest = 0
  for program in realPermutations:
    registerCache = [0, 0, 0, 0, 0]
    programCache = [data.copy(), data.copy(), data.copy(), data.copy(), data.copy()]
    inputCache = [[program.pop(0)], [program.pop(0)], [program.pop(0)], [program.pop(0)] ,[program.pop(0)]]
    # print('inputCache', inputCache)
    output = 0
    i = 0
    complete = False
    while not complete:
      if(i >= len(programCache)):
        i = 0
      inputCache[i].append(output)
      # print('input', programCache[i], registerCache[i], inputCache[i])
      immediateOutput = getRegister(programCache[i], registerCache[i], inputCache[i])
      # print('returned output', immediateOutput)
      if(immediateOutput[1]):
        registerCache[i] = immediateOutput[1]
        output = immediateOutput[0]
      elif(not immediateOutput[1]):
        complete = True
      i+=1

    print('finalOutput', output)
    if(output > highest):
      highest = output
  print('highest', highest)


def getRegister(program, i = 0, input=[]):
  data = program
  complete = False
  paused = False
  finalOutput = 0
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

    # print('opcode: {} modes: {}{}{}'.format(opcode, mode1, mode2, mode3))

    if (opcode == 1):
      # print('data', data[i+1])
      add1 = data[i+1] if mode1 == 1 else data[data[i+1]]
      add2 = data[i+2] if mode2 == 1 else data[data[i+2]]
      insertIdx = data[i+3]
      data[insertIdx] = add1 + add2
      # print('{}-add {}, {}, {}'.format(opcode, insertIdx, add1, add2))
      i+=4
      continue
    if (opcode == 2):
      multi1 = data[i+1] if mode1 == 1 else data[data[i+1]]
      multi2 = data[i+2] if mode2 == 1 else data[data[i+2]]
      insertIdx = data[i+3]
      data[insertIdx] = multi1 * multi2
      # print('{}-multi {}, {}, {}'.format(opcode, insertIdx, multi1, multi2))
      i+=4
      continue
    if (opcode == 3):
      data[data[i+1]] = input.pop(0)
      i+=2
      continue
    if (opcode == 4):
      finalOutput = data[i+1] if mode1 == 1 else data[data[i+1]]
      i+=2
      return [finalOutput, i]
    if (opcode == 5):
      check = data[i+1] if mode1 == 1 else data[data[i+1]]
      pointer = data[i+2] if mode2 == 1 else data[data[i+2]]
      if(check > 0):
        i = pointer
      else:
        i+=3
      continue
    if (opcode == 6):
      check = data[i+1] if mode1 == 1 else data[data[i+1]]
      pointer = data[i+2] if mode2 == 1 else data[data[i+2]]
      if(check == 0):
        i = pointer
      else:
        i+=3
      continue
    if (opcode == 7):
      first = data[i+1] if mode1 == 1 else data[data[i+1]]
      second = data[i+2] if mode2 == 1 else data[data[i+2]]
      data[data[i+3]] = 1 if (first < second) else 0
      i+=4
      continue
    if (opcode == 8):
      first = data[i+1] if mode1 == 1 else data[data[i+1]]
      second = data[i+2] if mode2 == 1 else data[data[i+2]]
      data[data[i+3]] = 1 if (first == second) else 0
      i+=4
      continue
    if (opcode == 99):
      complete = True
      return [finalOutput, None]
    
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