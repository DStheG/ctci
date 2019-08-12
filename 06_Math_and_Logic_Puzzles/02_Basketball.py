#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
06.02.Basketball
  You have a basketball hoop and someone says that you can play one of two g-
  ames.
  Game 1: You get one shot to make the hoop.
  Game 2: You get three shots and you have to make two of three shots.
  If p is the probability of making a particular shot, for which value of p
  should you pick one game or the other?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    p = random.random()
    self.param.append(p)

class Sol(Solution):
  def Naive(self, param):
    # Solution:
    #   p(G1) = p
    #   p(G2) = 3p^2 - 2p^3
    #   p(G1) - p(G2) = 2p^3 - 3p^2 + p
    #   p = p**3 + 3(p**2 - p**3)
    #   p = 3p**2 - 2p**3
    #   2p**3 - 3p**2 + p = 0
    #   p = 0, p = 0.5, p = 1
    #   0 <= p <= 0.5, Game1
    #   0.5 < p <= 1, Game2
    p = param[0]
    print 'P(Game1): %.2f' % p
    p_g2 = p * p * p + 3*(p * p * (1-p))
    print 'P(Game2): %.2f' % p_g2
    return "Game1" if p <= 0.5 else "Game2"

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
