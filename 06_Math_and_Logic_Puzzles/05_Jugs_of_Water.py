#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
06.05.Jugs of Water
  You have a five-quart jug, a three-quart jug, and an unlimited supply of w-
  ater (but no measuring cups). How would you come up with exactly four quar-
  ts of water? Note that the jugs are oddly shaped, such that filling up exa-
  ctly "half" of the jug would be impossible.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    pass

class Jug():
  def __init__(self, volume):
    self.volume = volume
    self.currentVolume = 0
    self.availVolume = [0, volume]
    self.updateAvailVolume()

  def updateAvailVolume(self):
    if self.currentVolume not in self.availVolume:
      self.availVolume += [self.currentVolume]
      self.availVolume.sort()

  def fill(self, volume):
    originVolume = self.currentVolume
    newVolume = self.currentVolume + volume
    self.currentVolume = min(self.volume, newVolume)
    self.updateAvailVolume()
    return volume - (self.currentVolume - originVolume)

  def fullFill(self):
    self.currentVolume = self.volume
    self.updateAvailVolume()

  def empty(self):
    self.currentVolume = 0

  def pour(self, to = None):
    if(to == None):
      self.empty()
    else:
      self.currentVolume = to.fill(self.currentVolume)
    self.updateAvailVolume()

  def __str__(self):
    return '(%d/%d) %s' % (self.currentVolume, self.volume, self.availVolume)


class Sol(Solution):
  def Naive(self, param):
    A = Jug(3)
    B = Jug(5)

    B.fullFill()

    B.pour(A)
    A.empty()
    B.pour(A)
    B.empty()
    B.fullFill()
    B.pour(A)

    print A, B

  def Travel(self, param):
    A = Jug(3)
    B = Jug(5)

    prevNumOfStateA = len(A.availVolume)
    prevNumOfStateB = len(B.availVolume)

    while True:
      for a in A.availVolume:
        for b in B.availVolume:
          A.empty()
          A.fill(a)
          B.empty()
          B.fill(b)
          A.pour(B)

          A.empty()
          A.fill(a)
          B.empty()
          B.fill(b)
          B.pour(A)

      if( prevNumOfStateA == len(A.availVolume)
          and prevNumOfStateB == len(B.availVolume)):
        break
      prevNumOfStateA = len(A.availVolume)
      prevNumOfStateB = len(B.availVolume)

    print A, B

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.add_solution(Sol("Travel"))
  ex.solve()

if __name__ == "__main__":
  solve()
