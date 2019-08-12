#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.04.Check Balanced
    Implement a function to check if a binary tree is balanced. For the purp-
    oses of this question, a balanced tree is defined to be a tree such that
    the heights of the two subtrees of any node never differ by more than one
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
  def __init__(self, name):
    super(Sol, self).__init__(name)
    MAX_DEPTH = 987654321
    MIN_DEPTH = 0

    self.depth_min = MAX_DEPTH
    self.depth_max = 0

  def dfs(self, node, depth):
    if node is None:
      return

    if(node.left is None and node.right is None):
      self.depth_min = depth if depth < self.depth_min else self.depth_min
      self.depth_max = depth if depth > self.depth_max else self.depth_max

    self.dfs(node.left, depth+1)
    self.dfs(node.right, depth+1)

  def Naive(self, param):
    bt = BTree(param[0])
    self.result = []
    self.dfs(bt.root, 0)

    print self.depth_max, self.depth_min
    return "Balanced" if (self.depth_max - self.depth_min) < 2 else "Not Balanced"

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
