#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
02.05.Sum Lists
      You have two numbers represented by a linked list, where each node con-
      tains a single digit. The digits are stored in reverse order, such that
      the 1's digit is at the head of the list. Write a function that adds t-
      he two numbers and returns the sum as a linked list.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen
from module.slist import SLinkedList

CHARS_SET = string.digits

class Ex_02_05(Exercise):
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
    SLL.append('7')
    self.param.append(SLL)
    SLL = SLinkedList()
    SLL.append('2')
    SLL.append('9')
    SLL.append('5')
    self.param.append(SLL)

class Ex0205(Solution):
  def Naive(self, param):
    l1 = len(param[0])
    l2 = len(param[1])
    op1 = param[0].headval if l1 > l2 else param[1].headval
    op2 = param[1].headval if l1 > l2 else param[0].headval

    L = SLinkedList()
    carry = 0
    while(op1 is not None):
      s = (int(op1.getData()) + int(op2.getData() if op2 is not None else 0) + carry)
      carry = 1 if s >= 10 else 0
      if carry :
        val = s - 10
      else:
        val = s
      L.append(str(val))

      op1 = op1.Next()
      op2 = op2.Next() if op2 is not None else None

    return L

  def NaiveFor(self, param):
    l1 = len(param[0])
    l2 = len(param[1])
    op1 = param[0].headval if l1 > l2 else param[1].headval
    op2 = param[1].headval if l1 > l2 else param[0].headval

    L = SLinkedList()
    while(op1 is not None):
      s = (int(op1.getData()) + int(op2.getData() if op2 is not None else 0))
      L.front(str(s))

      op1 = op1.Next()
      op2 = op2.Next() if op2 is not None else None

    n = L.headval
    carry = 0
    ret = SLinkedList()
    while(n is not None):
      s = (int(n.getData()) + carry)
      if(s >= 10):
        carry = 1
        val = s - 10
      else:
        carry = 0
        val = s
      ret.front(str(val))
      n = n.Next()

    return ret

def solve():
  ex = Ex_02_05()

  ex.add_solution(Ex0205("Naive"))
  ex.add_solution(Ex0205("NaiveFor"))

  ex.solve()

if __name__ == "__main__":
  solve()
