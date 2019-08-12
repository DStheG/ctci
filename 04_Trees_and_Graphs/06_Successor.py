#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.06.Successor
    Write an algorithm to find the "next" node (i.e., in-order successor) of
    a given node in a binary search tree. You may assume that each node has a
    link to its parent.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.btree import BST
from module.btree import Node

import random

class Ex(Exercise):
  def setup(self):
    arr = [i for i in range(0, 10)]
    self.param.append(arr)
    r = random.randint(0, len(arr)-1)
    self.param.append(r)

class Sol(Solution):
  def selectRandNode(self, rootNode, r):
    node = rootNode
    if node is None:
      return
    queue = [node]
    cnt = 0
    while(queue):
      node = queue.pop(0)
      if cnt == r :
        return node
      if node.left is not None:
        queue.append(node.left)
      if node.right is not None:
        queue.append(node.right)
      cnt += 1

  def getSuccessorNaive(self, node, rnode):
    if node is None:
      return None

    tnode = self.getSuccessorNaive(node.left, rnode)
    if tnode :
      return tnode
    if self.flag == True:
      return node
    if node == rnode:
      self.flag = True
    tnode = self.getSuccessorNaive(node.right, rnode)
    if tnode :
      return tnode

  def Naive(self, param):
    bst = BST(param[0])
    selectedNode = self.selectRandNode(bst.root, param[1])
    self.flag = False
    ret = self.getSuccessorNaive(bst.root, selectedNode)

    print selectedNode, '->', ret

    return ret

  def getSuccessor(self, node):
    if node.right == None:
      if node.parent.left == node:
        ret = node.parent
      else:
        node = node.parent
        while(node != None):
          if(node.parent == None):
            ret = None
            break;
          if node.parent.left == node:
            ret = node.parent
            break
          node = node.parent
    else:
      node = node.right
      while(node != None):
        ret = node
        node = node.left

    return ret

  def Travel(self, param):
    bst = BST(param[0])
    selectedNode = self.selectRandNode(bst.root, param[1])
    self.flag = False
    ret = self.getSuccessor(selectedNode)

    print selectedNode, '->', ret

    return ret

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.add_solution(Sol("Travel"))
  ex.solve()

if __name__ == "__main__":
  solve()
