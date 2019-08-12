#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.10.Check Subtree
  T1 and T2 are two very large binary trees, with T1 much bigger than T2.
  Create an algorithm to determine if T2 is a subtree of T1.
  A tree T2 is a subtree of T1 if there exists a node n in T1 such that subt-
  ree of n is identical to T2. That is, if you cut off the tree at node n,
  the two trees would be identical.
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
    arr = [i for i in range(0, 3)]
    self.param.append(arr)

class Sol(Solution):
  def _BFS(self, node):
    ret = []
    queue = [node]
    while(queue):
      node = queue.pop(0)
      if(node is None):
        ret += ['None']
        continue
      else:
        ret += [node.val]

      queue.append(node.left)
      queue.append(node.right)

    return ret

  def _checkSubtree(self, n1, n2):
    return self._BFS(n1) == self._BFS(n2)

  def checkSubtree(self, T1, T2):
    ref = T2.root.val

    queue = [T1.root]
    while(queue):
      node = queue.pop(0)

      if(node.val == ref):
        if self._checkSubtree(node, T2.root) is True:
          return True

      if(node.left is not None):
        queue.append(node.left)
      if(node.right is not None):
        queue.append(node.right)

    return False

  def Naive(self, param):
    #bst = BTree(param[0])
    bst = BST(param[0])
    bst2 = BST(param[1])

    bst.BFS()
    bst2.BFS()

    return self.checkSubtree(bst, bst)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
