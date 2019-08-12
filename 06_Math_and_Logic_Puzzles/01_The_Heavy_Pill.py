#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
06.01.The Heavy Pill
  You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has
  pills of weight 1.1 grams. Given a scale that provides an exact measuremen-
  t, how would you find the heavy bottle? You can only use the scale once.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Bottle(object):
  def __init__(self, pills = 20, weight = 1.0):
    self.pills = pills
    self.weight = weight

  def setWeight(self, weight):
    self.weight = weight

  def getWeightPerPill(self):
    return self.weight / self.pills

  def grabPills(self, pills):
    return self.getWeightPerPill() * pills

  def __str__(self):
    return '<%d, %.1f>' % (self.pills, self.weight)

  __repr__ = __str__

class Ex(Exercise):
  def setup(self):
    l = [Bottle() for _ in range(20)]
    r = random.randint(0, 19)
    l[r].setWeight(1.1)
    self.param.append(l)
    self.param.append(r)

class Sol(Solution):
  def useScale(self, l):
    return sum(l)

  def Naive(self, param):
    pills = []
    for i, o in enumerate(param[0]):
      pills += [o.grabPills(i)]
    expectPillsWeight = 9.5
    idxBottle = self.useScale(pills) - expectPillsWeight
    return param[1] == int(round(idxBottle / 0.005))

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
