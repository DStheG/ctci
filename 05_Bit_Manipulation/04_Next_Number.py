#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
05.04.Next Number
  Given a positive integer, print the next smallest and the next largest num-
  ber that have the same number of 1 bits in their binary representation.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

import ctypes

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(8)

class Sol(Solution):
  def csb(self, bits):
    ret = 0
    for b in '{0:b}'.format(bits):
      if b == '1':
        ret += 1
    return ret

  def Naive(self, param):
    v = ctypes.c_uint32(param[0]).value
    csb = self.csb(v)
    V = v+1
    while(1):
      if(csb == self.csb(V)):
        nextLarge = V
        break
      if(V == 2**32 - 1):
        nextLarge = None
        break
      V += 1
    V = v-1
    while(1):
      if(csb == self.csb(V)):
        nextSmall = V
        break
      if(V == 0):
        nextSmall = None
        break
      V -= 1
    return [nextLarge, nextSmall]

  def ON(self, param):
    v = ctypes.c_uint32(param[0]).value

    nextLarget = nextSmall = None
    cnt = 0
    for i in range(32):
      if (((v >> i) & 0b11) ^ 0b10) == 0b11:
        nextLarge = (v ^ (0b01 << i)) | 0b10 << i
        nextLarge = (nextLarge >> i) << i
        nextLarge |= ((1 << i) - 1) >> (i - cnt)
        break
      elif((v >> i) & 0b1):
        cnt += 1

    cnt = 0
    for i in range(32):
      if (((v >> i) & 0b11) ^ 0b01) == 0b11:
        nextSmall = (v ^ (0b10 << i)) | 0b01 << i
        nextSmall = (nextSmall >> i) << i
        nextSmall |= (((1 << i) - 1) >> (i - cnt)) << (i - cnt)
        break
      elif((v >> i) & 0b1):
        cnt += 1

    return [nextLarge, nextSmall]

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.add_solution(Sol("ON"))
  ex.solve()

if __name__ == "__main__":
  solve()
