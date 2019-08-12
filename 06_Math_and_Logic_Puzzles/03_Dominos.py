#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
06.03.Dominos
  There is an 8x8 chessboard in which two diagonally opposite coners have be-
  en cut off. You are given 31 dominos, and a single dominos can cover exact-
  ly two squares. Can you use the 31 dominos to cover the entire board? Prove
  your answer (by providing an example or showing why it's impossible).
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
  def findFreeSpace(self, board):
    for y in range(8):
      for x in range(8):
        if( board[y][x] == 0 ):
          return x, y
    return -1, -1
  def dfs(self, board, num):
    self.m = max(num, self.m)
    if(num == 32):
      return True
    x, y = self.findFreeSpace(board)
    if(x < 0 or y < 0):
      return False
    if(x+1 < 8 and board[y][x+1] == 0):
        board[y][x] = board[y][x+1] = num
        if(self.dfs(board, num+1)):
          print board
          return True
        board[y][x] = board[y][x+1] = 0
    if(y+1 < 8 and board[y+1][x] == 0):
        board[y][x] = board[y+1][x] = num
        if(self.dfs(board, num+1)):
          print board
          return True
        board[y][x] = board[y+1][x] = 0
    return False

  def Naive(self, param):
    self.m = -1
    board = [
         [0, 0, 0, 0, 0, 0, 0, 99],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [99, 0, 0, 0, 0, 0, 0, 0] ]
    return self.dfs(board, 1)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
