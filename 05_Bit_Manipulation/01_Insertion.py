#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
05.01.Insertion
  You are given two 32-bit numbers, N and M, and two bit positions, i and j.
  Write a method to insert M into N such that M starts at bit j and ends at
  bit i. You can assume that the bits j through i have enough space to fit
  all of M. That is if M = 10011, you can assume that there are at least 5
  bits between j and i. You would not, for example, have j = 3 and i = 2,
  because M could not fully fit between bit 3 and bit 2.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(int('10000000000',2))
    #self.param.append(int('11111111111',2))
    self.param.append(int('10011',2))
    self.param.append(2)
    self.param.append(6)

class Sol(Solution):
  def Naive(self, param):
    N = param[0]
    M = param[1]
    i = param[2]
    j = param[3]

    bitmask = (((1 << j+1) - 1) >> i) << i
    N = (N & ~bitmask) | (M << i)

    return "{0:b}".format(N)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
