#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
05.05.Debugger
  Explain what the following code does: ((n & (n-1)) == 0).
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

import ctypes

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(12)

class Sol(Solution):
  def isOnlyOneBitSet(self, v):
    # the meaning of 'v-1' is that clear lowest set bit and set lower bits
    # So that, the 'and' operation from the bit and lowers always return 0
    # otherwise, the higher bits don't effective from substract operation
    # that is, it same as v & v for higher bits, only if they are zero
    # they can return 0.
    # So, the conditional phase means check the only one bit is set or not
    return (v & (v-1)) == 0

  def Naive(self, param):
    v = ctypes.c_uint32(param[0]).value
    return self.isOnlyOneBitSet(v)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
