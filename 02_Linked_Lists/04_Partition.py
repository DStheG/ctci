#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
02.04.Partition
      Write code to partition a linked list around a value x, such that all
      nodes less than x come before all nodes greater than or equal to x. If
      x is contained within the list, the values of x only need to be after
      the elements less than x(see below). The partition element x can appear
      anywhere in the "right partition"; it does not need to appear between
      the left and right partitions.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen
from module.slist import SLinkedList

CHARS_SET = string.digits

class Ex_02_04(Exercise):
  def setup(self):
    SLL = SLinkedList()
    #self.param.append(string_gen(chars=CHARS_SET))
    for c in string_gen(chars=CHARS_SET):
      SLL.append(c)
    self.param.append(SLL)
    self.param.append(3)

class Ex0204(Solution):
  def Naive(self, param):
    n = param[0].headval
    K = param[1]
    prev = None
    while(n != None):
      if(int(n.dataval) < int(K)):
        if(prev is not None):
          prev.nextval = n.nextval
          n.nextval = param[0].headval
          param[0].headval = n
          n = prev.nextval
          continue
      prev = n
      n = n.nextval

    return param[0]

def solve():
  ex = Ex_02_04()

  ex.add_solution(Ex0204("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
