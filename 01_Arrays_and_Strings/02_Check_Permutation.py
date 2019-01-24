#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.2 Check Permutation
  Given two strings, Write a method to decide if on is a permutation of the
  other.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import random
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.sort  import quick_sort
from module.sort  import merge_sort
from module.str   import string_gen

CHARS_SET = string.printable
#CHARS_SET = string.digits

class Ex_01_02(Exercise):
  def setup(self):
    #size = 200
    #self.param.append(string_gen(size=size, chars=CHARS_SET))
    #self.param.append(string_gen(size=random.randint(1, size), chars=CHARS_SET))
    size = 5
    self.param.append("aabcde")
    self.param.append("acbde")

class Ex0102(Solution):
  # O(N*M)
  def Naive(self, param):
    large_str = list(param[0])
    small_str = list(param[1])

    if(len(large_str) != len(small_str)):
      return "NOT Perm"

    for i in range(len(small_str)):
      found = False
      for j in range(len(large_str)):
        if(small_str[i] == large_str[j]):
          found = True
          large_str[j] = ' '
          break
      print large_str
      if(found == False):
        return "NOT Perm"

    return "Perm"

  # O(N+M)
  def Bucket(self, param):
    large_str = param[0]
    small_str = param[1]

    if(len(large_str) != len(small_str)):
      return "NOT Perm"

    bucket = [0] * 128
    for i in range(len(large_str)):
      bucket[ord(large_str[i])] += 1
      bucket[ord(small_str[i])] -= 1

    return "Perm" if sum(abs(n) for n in bucket) == 0 else "NOT Perm"

def solve():
  ex = Ex_01_02()

  ex.add_solution(Ex0102("Naive"))
  ex.add_solution(Ex0102("Bucket"))

  ex.solve()

if __name__ == "__main__":
  solve()
