#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
02.06.Palindrome
      Implement a function to check if a linked list is a palindrome.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen
from module.slist import SLinkedList

CHARS_SET = string.digits

class Ex_02_06(Exercise):
  def setup(self):
    #SLL = SLinkedList()
    #for c in string_gen(size=4, chars=CHARS_SET):
    #  SLL.append(c)
    #self.param.append(SLL)
    #SLL = SLinkedList()
    #for c in string_gen(size=3, chars=CHARS_SET):
    #  SLL.append(c)
    #self.param.append(SLL)
    SLL = SLinkedList()
    SLL.append('6')
    SLL.append('1')
    SLL.append('6')
    self.param.append(SLL)

class Ex0206(Solution):
  def Naive(self, param):
    op = param[0].headval

    L = SLinkedList()
    carry = 0
    while(op is not None):
      L.front(op.getData())
      op = op.Next()

    op = param[0].headval
    op_r = L.headval

    while( op is not None):
      if op.getData() is not op_r.getData():
        return "Not Palindrome"
      op = op.Next()
      op_r = op_r.Next()

    return "Palindrome"

def solve():
  ex = Ex_02_06()

  ex.add_solution(Ex0206("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
