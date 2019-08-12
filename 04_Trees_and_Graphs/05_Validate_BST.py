#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.05.Validate BST
    Implement a function to check if a binary tree is a binary search tree.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.btree import BTree
from module.btree import BST
from module.btree import Node

class Ex(Exercise):
  def setup(self):
    arr = [i for i in range(0, 10)]
    self.param.append(arr)

class Sol(Solution):
  def checkBST(self, root):
    queue = [root]

    while(queue):
      node = queue.pop(0)
      if(node is None):
        continue

      if((node.left is not None and node.val < node.left.val)
          or (node.right is not None and node.val > node.right.val)):
        return False
      queue.append(node.left)
      queue.append(node.right)

    return True

  def Naive(self, param):
    bt = BTree(param[0])
    bst = BST(param[0])

    return self.checkBST(bt.root)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
