#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.11.Paths with sum
  You are given a binary tree in which each node. contains an integer value
  (which might be positive or negative). Design an algorithm to count the
  number of paths that sum to a given value. The path does not need to start
  or end at the root or a leaf, but it must go downwards (traveling only from
  parent nodes to child nodes).
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

import copy
import random

class Node():
  def __init__(self, val, parent = None):
    self.parent = parent
    self.left = None
    self.right = None
    self.val = val
    self.acc = 0

  def getVal(self):
    return self.val

class BinaryTree():
  def __init__(self):
    self.root = None

  def allocLeafNode(self, val):
    queue = [self.root]
    while(queue):
      node = queue.pop(0)
      if(node.left is not None):
        queue.append(node.left)
      else:
        n = Node(val, node)
        node.left = n
        return n
      if(node.right is not None):
        queue.append(node.right)
      else:
        n = Node(val, node)
        node.right = n
        return n
    return None

  def getLastNode(self):
    queue = [self.root]
    while(queue):
      node = queue.pop(0)
      if(node.left is not None):
        queue.append(node.left)
      if(node.right is not None):
        queue.append(node.right)

      if(not queue):
        return node
    return None

  def delete(self, node):
    n = self.getLastNode()
    if(n is not node):
      node.val = n.val
    pn = n.parent
    if pn.left is n:
      pn.left = None
    else:
      pn.right = None

  def insert(self, val):
    if self.root is None:
      self.root = Node(val)
    else:
      self.allocLeafNode(val)

  def find(self, val):
    queue = [self.root]
    while(queue):
      node = queue.pop(0)

      if(node.getVal() is val):
        return node

      if(node.left is not None):
        queue.append(node.left)
      if(node.right is not None):
        queue.append(node.right)

    return None

  def getRandomNode(self):
    queue = [self.root]
    ret = [self.root]
    while(queue):
      node = queue.pop(0)
      ret += [node]

      if(node.left is not None):
        queue.append(node.left)
      if(node.right is not None):
        queue.append(node.right)
    return random.choice(ret)

  def BFS(self):
    queue = [self.root]
    while(queue):
      node = queue.pop(0)
      if node is None:
        print 'None',
        continue
      print node.getVal(),
      queue.append(node.left)
      queue.append(node.right)
    print

class Ex(Exercise):
  def setup(self):
    arr = [random.randrange(-10, 10) for _ in range(30)]
    self.param.append(arr)

class Sol(Solution):
  def __init__(self, name):
    super(Sol, self).__init__(name)
    self.paths = []

  def travel(self, node, acc, s):
    if node is None:
      return

    node.acc = acc + node.val

    pnode = node.parent
    paths = [node.val]
    while(pnode):
      paths += [pnode.val]
      if node.acc - pnode.acc + pnode.val is s:
        self.paths += paths
      pnode = pnode.parent

    self.travel(node.left, acc + node.val, s)
    self.travel(node.right, acc + node.val, s)

  def Naive(self, param):
    bt = BinaryTree()
    for v in param[0]:
      bt.insert(v)
    self.travel(bt.root, 0, 3)

    print self.paths
    return len(self.paths)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
