# https://adventofcode.com/2019/day/6
import os

def process():
  objects = readFile('input-og')
  tree = buildTree('COM', objects, Node('COM'))

  # part 1: count orbits
  # counts = countOrbits(tree)
  # print(counts)
  # print('total {}'.format(counts['direct'] + counts['indirect']))

  # part 2: tree traversal
  print(findPathTraversals(tree, 'SAN', 'YOU'))

# ------------
# Tree methods and class
# ------------
def findPathTraversals(tree, destinationId, sourceId):
  sourceNode = findNode(sourceId, tree)
  currentLocation = sourceNode
  traversals = 0

  # find common parent
  foundCommonNode = False
  while not foundCommonNode:
    currentLocation = currentLocation.parent
    destination = findNode(destinationId, currentLocation)
    print('parent find', currentLocation.id, currentLocation.parent.id)
    if (destination):
      foundCommonNode = True
    traversals += 1

  # find child
  foundDestination = False
  while not foundDestination:
    print('child find', currentLocation.id)
    if (currentLocation.id == destinationId):
      foundDestination = True
    else:
      for child in currentLocation.children:
        if findNode(destinationId, child):
          currentLocation = child
    traversals += 1
  # -3 to account for the original jump, and the 2 child jumps that don't count
  return traversals-3

def countOrbits(node, level=0, counts=None):
  counts = counts if counts else {
    'direct': 0,
    'indirect': 0
  }
  if(node.parent):
    counts['direct'] += 1

  if(level):
    counts['indirect'] += (level-1)

  for child in node.children:
    countOrbits(child, level+1, counts)
  return counts

def buildTree(rootObjectId, objDictList, tree):
  objDicts = [obj for obj in objDictList if obj['parentId'] == rootObjectId]
  for objDict in objDicts:
    addChild(tree, objDict['parentId'], objDict['childId'])
    buildTree(objDict['childId'], objDictList, tree)
  return tree

def findNode(id, node):
  if(node.id == id):
    return node
  for child in node.children:
    foundNode = findNode(id, child)
    if (foundNode): return foundNode
  return None

def addChild(tree, parentId, childId):
  parentNode = findNode(parentId, tree)
  if (not parentNode):
    raise Exception('No parent node found for {}'.format(parentId))
  child = Node(childId, parentNode)
  parentNode.children.append(child)
  return child

def printTree(tree, level=0):
  print('{} {}'.format('-' * level, tree))
  for child in tree.children:
    printTree(child, level+1)


class Node:
  def __init__(self, id, parent=None):
    self.id = id
    self.parent = parent
    self.children = []

  def __str__(self):
    parentId = self.parent.id if self.parent else ''
    childList = []
    for child in self.children:
      childList.append(str(child.id))
    return '{}<-{}->{}'.format(parentId, self.id, ', '.join(childList))


# ------
# Generic Helpers
# ------
def readFile(file):
  lines = []
  f = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file), 'r')
  for line in f.readlines():
    objects = line.split(')')
    newDict = {
      'parentId': objects[0],
      'childId': objects[1].rstrip()
    }
    lines.append(newDict)
  return lines

if __name__ == "__main__":
  process()