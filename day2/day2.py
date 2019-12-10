# https://adventofcode.com/2019/day/1
import math
import os

def process():
  data = readFile('input')

  found = False
  for noun in range(100):
    for verb in range(100):
      result = getRegister(data, noun, verb)
      print('{}  -> noun: {} | verb: {}'.format(result, noun, verb))
      if (result == 19690720):
        print('got it! {}'.format(100 * noun + verb))
        found = True
        break;
    if(found):
      break;



def getRegister(orignal_data, noun, verb):
  data = orignal_data.copy()
  data[1] = noun
  data[2] = verb

  i = 0
  complete = False
  while not complete:
    opcode = data[i]
    if (opcode == 1):
      add1 = data[data[i+1]]
      add2 = data[data[i+2]]
      insertIdx = data[i+3]
      data[insertIdx] = add1 + add2
      # print('{}-add {}, {}, {}'.format(opcode, insertIdx, add1, add2))
      i+=4
      continue
    if (opcode == 2):
      multi1 = data[data[i+1]]
      multi2 = data[data[i+2]]
      insertIdx = data[i+3]
      data[insertIdx] = multi1 * multi2
      # print('{}-multi {}, {}, {}'.format(opcode, insertIdx, multi1, multi2))
      i+=4
      continue
    if (opcode == 99):
      complete = True
      continue
  return data[0]

def readFile(file):
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  opcodes = f.read().split(',')
  return [int(x) for x in opcodes]

if __name__ == "__main__":
  process()