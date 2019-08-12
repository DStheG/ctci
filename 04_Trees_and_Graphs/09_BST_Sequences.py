#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.09.BST Sequences
  A binary search tree was created by traversing through an array from left
  to right and inserting each element. Given a binary search tree with disti-
  nct elements, print all possible arrays that could have led to this tree.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.btree import BST
from module.btree import Node
import copy

import random

class Ex(Exercise):
  def setup(self):
    arr = [i for i in range(1, 10)]
    self.param.append(arr)

class Sol(Solution):
  def travel(self, l, ret):
    if len(l) == 0:
      print ret
    for i in range(len(l)):
      new_l = copy.copy(l)
      new_ret = copy.copy(ret)
      node = new_l.pop(i)
      if node.left is not None:
        new_l += [node.left]
      if node.right is not None:
        new_l += [node.right]
      new_ret += [node.val]

      self.travel(new_l, new_ret)

  def Naive(self, param):
    bst = BST(param[0])
    self.travel([bst.root], [])

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
