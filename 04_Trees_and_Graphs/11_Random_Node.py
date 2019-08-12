#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.11.Random Node
  You are implementing a binary tree class from scratch which, in addition to
  insert, find, and delete, has a method getRandomNode() which returns a ran-
  dom node from the tree. All nodes should be equally likely to be chosen.
  Design and implement an algorithm for getRandomNode, and explain how you
  would implement the rest of the methods.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

import random

class Ex(Exercise):
  def setup(self):
    arr = [i for i in range(0, 10)]
    self.param.append(arr)

class Node():
  def __init__(self, val, parent = None):
    self.parent = parent
    self.left = None
    self.right = None
    self.val = val

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

class Sol(Solution):
  def Naive(self, param):
    bt = BinaryTree()
    for v in param[0]:
      bt.insert(v)
    bt.BFS()
    print bt.find(7).getVal()
    node = bt.getRandomNode()
    print node.getVal()
    bt.delete(node)
    bt.BFS()

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
