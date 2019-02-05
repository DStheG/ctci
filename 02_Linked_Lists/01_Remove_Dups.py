#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
02.01. Remove Dups: Write code to remove duplicates from an unsorted linked
       list.
       FOLLOW UP
       How would you solve this problem if a temporary buffer is not allowed?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen
from module.slist import SLinkedList

CHARS_SET = string.lowercase

class Ex_02_01(Exercise):
  def setup(self):
    SLL = SLinkedList()
    #self.param.append(string_gen(chars=CHARS_SET))
    for c in string_gen(chars=CHARS_SET):
      SLL.append(c)
    self.param.append(SLL)

class Ex0201(Solution):
  # O(N*N)
  def Naive(self, param):
    n = param[0].headval
    while(n != None):
      search = n.nextval
      while(search != None):
        target = search
        search = search.nextval
        if(n.dataval is target.dataval):
          param[0].remove(target)
      n = n.nextval
    return param[0]

def solve():
  ex = Ex_02_01()

  ex.add_solution(Ex0201("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
