#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.3 URLify
  Write a method to replace all spaces in a string with '%20'. You may assume
  that the string has sufficient space at the end to hold the additional
  characters, and that you are given the "true" lengh of the string. (Note:If
  implementing in java, please use a character array so that you can perform
  this operation in place.)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import random
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

CHARS_SET = string.printable

class Ex_01_03(Exercise):
  def setup(self):
    self.param.append(["Mr John Smith    ", 13])

class Ex0103(Solution):
  # O(N)
  def Backward(self, param):
    str_buffer      = list(param[0][0])
    str_true_length = param[0][1]

    str_len = len(str_buffer) - 1

    for i in range(str_true_length-1, -1, -1):
      if(str_buffer[i] != ' '):
        str_buffer[str_len] = str_buffer[i]
        str_len -= 1
      else:
        str_buffer[str_len]   = '0'
        str_buffer[str_len-1] = '2'
        str_buffer[str_len-2] = '%'
        str_len -= 3
        pass

    return ''.join(str_buffer)

def solve():
  ex = Ex_01_03()

  ex.add_solution(Ex0103("Backward"))

  ex.solve()

if __name__ == "__main__":
  solve()
