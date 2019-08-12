#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
05.03.Flip bit to Win
  You have an integer and you can flip exactly one bit from a 0 to a 1. Write
  code to find the length of the longest sequence of 1s you could create.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

import ctypes

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(0)

class Sol(Solution):
  def Naive(self, param):
    v = ctypes.c_uint32(param[0]).value
    print "{0:b}".format(v)

    queue = []
    acc = 0
    for i in range(32):
      if((v >> i) & 1):
        acc += 1
      else:
        queue += [acc]
        if(acc != 0):
          queue += [0]
        acc = 0

    result = 0 if queue else 63
    for i in range(len(queue)-2):
      result = max(result, queue[i] + queue[i+2])

    return result + 1

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
