# https://adventofcode.com/2019/day/1
import math
import os

INPUT = (246515, 739105)

def process():
  totalPasswords=0
  for password in range(INPUT[0], INPUT[1]):
    strPassword = str(password)
    if(not validatePassword(password)):
      continue

    isMatch = False

    i = 0
    while i < len(strPassword):
      c = strPassword[i]
      matches = numberOfMatches(strPassword[i:], c)
      i+=matches
      if (matches == 2): 
        isMatch = True
        break

    if(isMatch): 
      totalPasswords+=1
  print(totalPasswords)

def numberOfMatches(string, char):
  matches = 0
  for c in string:
    if (c == char): matches += 1
    else: break;
  return matches;

def safeGet(string, i):
  try:
    return string[i]
  except:
    return -1


def validatePassword(password):
  highPoint = 0
  valid = True
  for i in str(password):
    if (int(i) < highPoint): valid = False
    else: highPoint =int(i)
  return valid


def readFile(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    lines.append(line.split(','))
  return lines


if __name__ == "__main__":
  process()