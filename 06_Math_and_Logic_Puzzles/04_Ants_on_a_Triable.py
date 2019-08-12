#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
06.04.Ants on a Triangle
  There are three ants on different vertices of a triagle. What is the proba-
  bility of collision (between any two or all of them) if they start walking
  on the sides of the triangle? Assume that each ant randomly picks a direct-
  ion, with either direction being equally likely to be chosen, and that they
  walk at the same speed.
  Similary, find the probaility of collision with n ants on an n-vertex poly-
  gon.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(3)
    pass

class Sol(Solution):
  def Naive(self, param):
    # the only possible they never meet each other
    # is when they choose all same direction so that,
    # the p(no_coliision) = 0.5^n for single direction
    # and the direction could be left or right.
    n = param[0]
    return 1 - 2 * 0.5**n

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
