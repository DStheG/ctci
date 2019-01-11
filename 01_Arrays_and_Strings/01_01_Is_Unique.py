#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.1 Is Unique
  Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
import string
import sys

sys.path.append("../")

from module.ctci import Exercise
from module.ctci import Solution
from module.sort import quick_sort
from module.sort import merge_sort

CHARS_SET = string.printable

def string_gen(size=10, chars=CHARS_SET):
  return ''.join(random.choice(chars) for _ in range(size))

class Ex_01_01(Exercise):
  def setup(self):
    self.param.append(string_gen())

class Ex0101(Solution):
  # O(N*N)
  def Naive(self, param):
    r_str = param[0]
    for i in range(len(r_str)):
      for j in range(i+1, len(r_str)):
        if r_str[i] == r_str[j]:
          return "NOT Unique"
    return "    Unique"

  #O(NlogN)
  def QuickSort(self, param):
    r_str = param[0]
    sorted_str = quick_sort(list(r_str))

    for i in range(1, len(sorted_str)):
      if sorted_str[i-1] == sorted_str[i]:
        return "NOT Unique"
    return "    Unique"

  #O(NlogN)
  def MergeSort(self, param):
    r_str = param[0]
    sorted_str = merge_sort(list(r_str))

    for i in range(1, len(sorted_str)):
      if sorted_str[i-1] == sorted_str[i]:
        return "NOT Unique"
    return "    Unique"

  # O(??)
  def libSort(self, param):
    r_str = param[0]
    sorted_str = ''.join(sorted(r_str))

    for i in range(1, len(sorted_str)):
      if sorted_str[i-1] == sorted_str[i]:
        return "NOT Unique"
    return "    Unique"

  # O(N)
  def Bucket(self, param):
    r_str = param[0]

    # THERE ARE ONLY 128 ASCIIs
    number_of_printable_chars = len(CHARS_SET)
    bucket = [0] * 128

    for i in range(len(r_str)):
      if bucket[ord(r_str[i])] == 0:
        bucket[ord(r_str[i])] = 1
      else:
        return "NOT Unique"
    return "    Unique"

def solve():
  ex = Ex_01_01()

  ex.add_solution(Ex0101("Naive"))
  ex.add_solution(Ex0101("QuickSort"))
  ex.add_solution(Ex0101("MergeSort"))
  ex.add_solution(Ex0101("libSort"))
  ex.add_solution(Ex0101("Bucket"))

  ex.solve()

if __name__ == "__main__":
  solve()
