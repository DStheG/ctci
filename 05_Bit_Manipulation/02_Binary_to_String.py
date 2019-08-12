#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
05.02.Binary to String
  Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a do-
  uble, print the binary representation. If the number cannot be represented
  accurately in binary with at most 32 characters, print "ERROR"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

import ctypes

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(0.3)

class Sol(Solution):
  def Naive(self, param):
    if( param[0] == 0 ):
      return "0.0"
    elif( param[0] == 1):
      return "1.0"
    elif( param[0] < 0 or param[0] > 1):
      return "ERROR"
    v = ctypes.c_longlong.from_buffer(ctypes.c_double(param[0] + 1)).value
    s = "{0:b}".format(v)
    s =  "0" * (64-len(s)) + s
    frac = s[12:]
    if(int(frac[32:]) != 0) :
      return "ERROR"
    return "0." + frac[:32]

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
