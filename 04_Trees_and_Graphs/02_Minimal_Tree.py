#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.02.Minimal Tree
      Given a sorted (incresing order) array with unique integer elements.
      write an algorithm to create binary search tree with minimal height.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.btree import BTree
from module.btree import Node

class BST(BTree):
  def insert(self, val):
    pass

  def createMinTree(self, arr, l_idx, r_idx):
    mid_idx = l_idx + (r_idx - l_idx + 1) / 2

    node = Node()
    node.setValue(arr[mid_idx])

    if(l_idx != r_idx):
      l_node = self.createMinTree(arr, l_idx, mid_idx-1)
      node.setLeft(l_node)
      if(r_idx - l_idx > 1):
        r_node = self.createMinTree(arr, mid_idx+1, r_idx)
        node.setRight(r_node)

    return node

class Ex(Exercise):
  def setup(self):
    arr = [i for i in range(0, 10)]
    self.param.append(arr)

class Sol(Solution):
  def Naive(self, param):
    bst = BST()
    arr = param[0]
    bst.root = bst.createMinTree(param[0], 0, len(arr)-1)

    bst.BFS()

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
