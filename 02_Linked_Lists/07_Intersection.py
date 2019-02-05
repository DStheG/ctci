#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
02.07.Intersection
      Given two (singly) linked lists, determine if the two lists intersect.
      Return the intersection node. Note that the intersection is defined ba-
      sed on reference, not value. That is, if the kth node of the first lin-
      ked list is the exact same node (by reference) as the jth node of the
      second linked list, then they are intersecting.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen
from module.slist import SLinkedList
from module.slist import Node

CHARS_SET = string.digits

class Ex_02_07(Exercise):
  def setup(self):
    #SLL = SLinkedList()
    #for c in string_gen(size=4, chars=CHARS_SET):
    #  SLL.append(c)
    #self.param.append(SLL)
    #SLL = SLinkedList()
    #for c in string_gen(size=3, chars=CHARS_SET):
    #  SLL.append(c)
    #self.param.append(SLL)
    n = Node('3')
    SLL = SLinkedList()
    SLL.append('6')
    SLL.append(n)
    SLL.append('1')
    SLL.append('6')
    self.param.append(SLL)
    SLL = SLinkedList()
    SLL.append('6')
    SLL.append('1')
    SLL.append(n)
    SLL.append('6')
    self.param.append(SLL)

class Ex0207(Solution):
  def Naive(self, param):
    op1 = param[0].headval

    while(op1 is not None):
      op2 = param[1].headval
      while(op2 is not None):
        if op1 is op2:
          return op1.getData()
        op2 = op2.Next()
      op1 = op1.Next()
    return None

def solve():
  ex = Ex_02_07()

  ex.add_solution(Ex0207("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
