#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.9 String Rotation
  Assume you have a method isSubstring which checks if one word is a substri-
  ng of another. Given two strings, s1 and s2, write code to check if s2 is
  a rotation of s1 using only one call to isSubstring
  (e.g., "waterbottle" is a rotation of "erbottlewat").
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

from collections import Counter

class Ex_01_09(Exercise):
  def setup(self):
    self.param.append("waterbottle")
    self.param.append("erbottlewat")

class Ex0109(Solution):
  def isSubstring(self, s1, s2):
    return (s2 in s1)

  def Naive(self, param):
    s1 = param[0]
    s2 = param[1]

    if(len(s1) != len(s2)):
      return False

    i = -1
    for i in range(0, len(s2)):
      if s1[i:] == s2[:-i]:
        idx = i
        break

    if( i == -1 ):
      return False

    s3 = s2[len(s2)-i:] + s2[:len(s2)-i]

    return self.isSubstring(s1, s3)

def solve():
  ex = Ex_01_09()
  ex.add_solution(Ex0109("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
