#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.08.First Common Ancestor
  Design an algorithm and write code to find the first common ancestor of two
  nodes in a binary tree. Avoid storing additional nodes in a data structure.
  NOTE: This is not necessarily a binary search tree.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.btree import BTree
from module.btree import BST
from module.btree import Node

import random

class Ex(Exercise):
  def setup(self):
    arr = [i for i in range(0, 10)]
    self.param.append(arr)
    r1 = random.randint(0, len(arr)-1)
    self.param.append(r1)
    r2 = random.randint(0, len(arr)-1)
    while(r2 is r1):
      r2 = random.randint(0, len(arr)-1)
    self.param.append(r2)

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

  def getCommonAncenstorNaive(self, node1, node2):
    while(node1 != None):
      node = node2
      while(node != None):
        if(node1 == node):
          return node
        node = node.parent
      node1 = node1.parent

    # neven return here
    return 'ERROR'

  def Naive(self, param):
    #bst = BTree(param[0])
    bst = BST(param[0])
    bst.BFS()
    bst.DFS()
    #selectedNode1 = self.selectRandNode(bst.root, param[1])
    #selectedNode2 = self.selectRandNode(bst.root, param[2])
    selectedNode1 = self.selectRandNode(bst.root, 4)
    selectedNode2 = self.selectRandNode(bst.root, 7)
    print selectedNode1.val, selectedNode2.val

    return self.getCommonAncenstorNaive(selectedNode1, selectedNode2).val

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
