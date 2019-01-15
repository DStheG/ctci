#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.6 String Compression
  Implement a method to perform basic string compression using the counts of
  repeated characters. For example, the string aabcccccaaa would become
  a2b1c5a3. If the "compressed" string would not become smaller than the ori-
  ginal string, your method should return the original string. You can assume
  the string has only uppercase and lowercase letters (a-z).
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import random
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

from collections import Counter

CHARS_SET = string.ascii_letters + ' '

class Ex_01_06(Exercise):
  def setup(self):
    #self.param.append("aabcccccaaa")
    self.param.append("abcd")

class Ex0106(Solution):
  def Naive(self, param):
    org_str = list(param[0])
    com_str = []
    prev_char = ''
    cnt = 0

    for c in org_str:
      if(prev_char != c):
        if(prev_char != ''):
          com_str += [str(prev_char), str(cnt)]
        prev_char = c
        cnt = 1
      else:
        cnt+=1
    com_str += [str(prev_char), str(cnt)]
    com_len = len(''.join(com_str))

    return ''.join(com_str) if com_len <= len(param[0]) else param[0]

def solve():
  ex = Ex_01_06()
  ex.add_solution(Ex0106("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
