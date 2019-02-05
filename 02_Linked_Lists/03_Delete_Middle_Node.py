#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
02.03.Delete Middle Node
      Implement an algorithm to delete a node in the middle (i.e., any node
      but the first and last node, not necessarily the exact middle) of a
      singly linked list, given only access to that node.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen
from module.slist import SLinkedList

CHARS_SET = string.lowercase

class Ex_02_03(Exercise):
  def setup(self):
    SLL = SLinkedList()
    #self.param.append(string_gen(chars=CHARS_SET))
    for c in CHARS_SET:
      SLL.append(c)
    self.param.append(SLL)
    self.param.append('b')

class Ex0203(Solution):
  def Naive(self, param):
    n = param[0].headval
    prev = n
    n = n.nextval
    while(n.nextval != None):
      if(n.dataval is param[1]):
        prev.nextval = n.nextval
      n = n.nextval

    return param[0]

def solve():
  ex = Ex_02_03()

  ex.add_solution(Ex0203("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
