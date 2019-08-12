#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
06.07.The Apocalypse
  In the new post-apocalyptic world, the world queen is desperately concerned
  about the birth rate. Therefore, she decrees that all families should ensu-
  re that they have one girl or else they face massive fines. If all families
  abide by this policy - that is, they have continue to have children until
  they have one girl, at which point they immediately stop - what will the g-
  ender ratio of the new generation be? (Assume that the odds of someone hav-
  ing a boy or a girl on any given pregnancy is equal.) Solve this out logic-
  ally and then write a computer simulation of it.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(3)

class Sol(Solution):
  def Naive(self, param):
    N = param[0]
    return 0.5 ** N

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
