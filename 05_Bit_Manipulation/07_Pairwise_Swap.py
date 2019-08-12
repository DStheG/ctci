#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
05.07.Pairwise Swap
  Write a program to swap odd and even bits in an integer with as few instru-
  ctions as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are
  swapped, and so on).
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

import ctypes

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    #self.param.append(0x55555555)
    #self.param.append(0xaaaaaaaa)
    self.param.append(1023)

class Sol(Solution):
  def Naive(self, param):
    A = ctypes.c_uint32(param[0]).value
    maskbit = ctypes.c_uint32(0x55555555).value

    return ((A >> 1) & maskbit) | ((A << 1) & (maskbit << 1))

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
