#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.7 Rotate Matrix
  Given an image represented by an NxN matrix, where each pixel in the image
  is 4 bytes, write a method to rotate the image by 90 degrees, Can you do in
  place?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import math
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

from collections import Counter

class Ex_01_07(Exercise):
  def setup(self):
    N = 5
    INPUT = [[i] * N for i in range(N)]
    for i in range(N):
      for j in range(N):
        INPUT[i][j] = N*INPUT[i][j] + j + 1
    self.param.append(INPUT)

class Ex0107(Solution):
  def moveTo(self, ret, N, x, y, l, depth):
    X = N - y - 1
    Y = x
    ret[Y][X] = l[y][x]

  def Naive(self, param):
    mat = param[0]
    N = len(mat)

    ret = [[0] * N for i in range(N)]
    for i in range(N):
      for j in range(N):
        self.moveTo(ret, N, j, i, mat, 4)

    return ret

def solve():
  ex = Ex_01_07()
  ex.add_solution(Ex0107("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
