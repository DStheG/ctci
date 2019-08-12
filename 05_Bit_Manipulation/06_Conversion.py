#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
05.06.Conversion
  Write a function to determine the number of bits you would need to flip to
  convert integer A to integer B
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

import ctypes

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(29)
    self.param.append(15)

class Sol(Solution):
  def csb(self, bits):
    ret = 0
    for b in '{0:b}'.format(bits):
      if b == '1':
        ret += 1
    return ret

  def Naive(self, param):
    A = ctypes.c_uint32(param[0]).value
    B = ctypes.c_uint32(param[1]).value

    return self.csb(A ^ B)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
