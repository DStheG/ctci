#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
06.06.Blue-Eyed Island
  A bunch of people are living on an island, when a visitor comes with a str-
  ange order: all blue-eyed people must leave the island as soon as possible.
  There will be a flight out at 8:00 pm every evening. Each person can see e-
  veryone else's eye color. but they do not know their own (nor is anyone al-
  lowed to tell them). Additionally, they do not know how many people have b-
  lue eyes, although they do know that at least one person does. How many da-
  ys will it take the blue-eyed people to leave?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    pass

class Sol(Solution):
  def Naive(self, param):
    print '?'

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
