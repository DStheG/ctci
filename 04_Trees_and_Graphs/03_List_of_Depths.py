#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.03.List of Depths
    Given a binary tree, design an algorithm which creates a linked list of
    all the nodes at each depth (e.g., if you have a tree with depth D,
    you'll have D linked lists).
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.btree import BTree
from module.btree import Node

class Ex(Exercise):
  def setup(self):
    arr = [i for i in range(0, 10)]
    self.param.append(arr)

class Sol(Solution):
  def dfs(self, node, depth):
    if node is not None:
      l = None
      try:
        l = self.result[depth]
      except:
        self.result.append([])
        l = self.result[depth]

      l.append(node.val)
      self.dfs(node.left, depth+1)
      self.dfs(node.right, depth+1)
      return

  def Naive(self, param):
    bt = BTree(param[0])
    self.result = []
    self.dfs(bt.root, 0)

    return self.result

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
