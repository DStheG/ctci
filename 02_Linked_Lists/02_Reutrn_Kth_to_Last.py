#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
02.02.Return Kth to last
      Implement an algorithm to find the kth to last element of a singly
      linked list.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen
from module.slist import SLinkedList

CHARS_SET = string.lowercase

class Ex_02_02(Exercise):
  def setup(self):
    SLL = SLinkedList()
    #self.param.append(string_gen(chars=CHARS_SET))
    for c in string_gen(chars=CHARS_SET):
      SLL.append(c)
    self.param.append(SLL)
    self.param.append(0)

class Ex0202(Solution):
  def Naive(self, param):
    n = param[0].headval
    K = param[1]
    SL = SLinkedList()
    while(n != None):
      SL.front(n.dataval)
      n = n.nextval
    n = SL.headval
    idx = 0
    ret = ''
    while(n != None):
      if(K == idx) :
        ret = n.dataval
        break
      n = n.nextval
      idx+=1
    return ret

def solve():
  ex = Ex_02_02()

  ex.add_solution(Ex0202("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
