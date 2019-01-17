#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.8 Zero Matrix
  Write an algorithm such that if an element in an MxN matrix is 0, its
  entire row and column are set to 0
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

from collections import Counter

class Ex_01_08(Exercise):
  def setup(self):
    M = random.randint(3, 3)
    N = random.randint(4, 4)

    mat = [[0] * N for i in range(M)]
    for i in range(M):
      for j in range(N):
        mat[i][j] = random.randint(0, 9)

    self.param.append(mat)

class Ex0108(Solution):
  def setZeroCol(self, mat, c):
    l = len(mat[0])
    for i in range(l):
      mat[c][i] = 0

  def setZeroRol(self, mat, r):
    l = len(mat)
    for i in range(l):
      mat[i][r] = 0

  def Naive(self, param):
    mat = param[0]

    zero = []
    for i in range(len(mat)):
      for j in range(len(mat[0])):
        if mat[i][j] == 0:
          zero += [(i, j)]

    for pos in zero:
      self.setZeroCol(mat, pos[0])
      self.setZeroRol(mat, pos[1])

    return mat

def solve():
  ex = Ex_01_08()
  ex.add_solution(Ex0108("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
