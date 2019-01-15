#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.5 One Away
  There are three types of edits that can be performed on strings: insert a
  character, remove a chracter, or replace a character. Given two strings,
  write a function to check if they are one edit (or zero edits) away.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import random
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

from collections import Counter

CHARS_SET = string.ascii_letters + ' '

class Ex_01_05_01(Exercise):
  def setup(self):
    self.param.append("pale")
    self.param.append("ple")

class Ex_01_05_02(Exercise):
  def setup(self):
    self.param.append("pales")
    self.param.append("pale")

class Ex_01_05_03(Exercise):
  def setup(self):
    self.param.append("pale")
    self.param.append("bale")

class Ex_01_05_04(Exercise):
  def setup(self):
    self.param.append("pale")
    self.param.append("bake")

class Ex0105(Solution):
  def findDelimeterIdx(self, org_str, edit_str):
    min_len = min(len(org_str), len(edit_str))
    olist = list(org_str)
    elist = list(edit_str)
    for i in range(min_len):
      if olist[i] != elist[i]:
        return i
    return -1

  def Naive(self, param):
    org_str = param[0]
    edit_str = param[1]

    if(org_str == edit_str):
      return True

    d_idx = self.findDelimeterIdx(org_str, edit_str)
    if(d_idx == -1):
      return True

    if(len(org_str) == len(edit_str)):
      l_pre   = org_str[:d_idx]
      l_post  = org_str[d_idx+1:]
      s_pre   = edit_str[:d_idx]
      s_post  = edit_str[d_idx+1:]
    elif(len(org_str) > len(edit_str)):
      l_pre   = org_str[:d_idx]
      l_post  = org_str[d_idx+1:]
      s_pre   = edit_str[:d_idx]
      s_post  = edit_str[d_idx:]
    else:
      l_pre   = edit_str[:d_idx]
      l_post  = edit_str[d_idx+1:]
      s_pre   = org_str[:d_idx]
      s_post  = org_str[d_idx:]

    if(l_pre == s_pre and l_post == s_post):
      return True

    return False

def solve():
  ex = Ex_01_05_01()
  ex.add_solution(Ex0105("Naive"))
  ex.solve()

  ex = Ex_01_05_02()
  ex.add_solution(Ex0105("Naive"))
  ex.solve()

  ex = Ex_01_05_03()
  ex.add_solution(Ex0105("Naive"))
  ex.solve()

  ex = Ex_01_05_04()
  ex.add_solution(Ex0105("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
