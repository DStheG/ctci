#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
02.08.Loop Detection
      Given a circular linked list, implement an algorithm that returns the
      node at the beginning of the loop.
      DEFINITION
      Circular linked list: A(corrupt) linked list in which a node's next
      pointer points to an earlier node, so as to make a loop in the linked
      list.
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

class Ex_02_08(Exercise):
  def setup(self):
    #SLL = SLinkedList()
    #for c in string_gen(size=4, chars=CHARS_SET):
    #  SLL.append(c)
    #self.param.append(SLL)
    #SLL = SLinkedList()
    #for c in string_gen(size=3, chars=CHARS_SET):
    #  SLL.append(c)
    #self.param.append(SLL)
    n = Node('C')
    SLL = SLinkedList()
    SLL.append('A')
    SLL.append('B')
    SLL.append(n)
    SLL.append('D')
    SLL.append('E')
    SLL.append(n)
    self.param.append(SLL)

class Ex0208(Solution):
  def Naive(self, param):
    op = param[0].headval

    L = SLinkedList()
    while(op):
      l = L.headval
      while(l):
        if id(op) == l.getData():
          return op.getData()
        l = l.Next()
      L.append(id(op))
      op = op.Next()
    return None

def solve():
  ex = Ex_02_08()

  ex.add_solution(Ex0208("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
