#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.4 Palindrome Permutation
  Given a string, write a function to check if it is a permutation of a pali-
  ndrome. A palindrome is a word or phrase that is the same forwards and bac-
  kwards. A permutation is a rearrangement to letters. The palindrome does n-
  ot need to be limited to just dictionary words.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import random
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

from collections import Counter

CHARS_SET = string.ascii_letters + ' '

class Ex_01_04(Exercise):
  def setup(self):
    self.param.append("Tact Coa")

class Ex0104(Solution):
  # O(N)
  def Naive(self, param):
    Str = param[0].lower()

    len_of_bucket = [0] * (len(CHARS_SET) / 2)

    # When the length of string (exception space) is even
    # The all each character should be occurs even.
    # Otherwise, the only one character occurs odd.
    Total = odd = even = 0
    for s in Str:
      if s != ' ':
        idx = ord(s) - ord('a')
        len_of_bucket[idx] += 1
        if(len_of_bucket[idx] % 2):
          odd += 1
          if(len_of_bucket[idx] != 1):
            even -= 1
        else:
          even += 1
          odd -= 1

        Total += 1

    if(Total % 2):
      if(odd == 1):
        return True
    elif(odd == 0):
      return True
    return False

  def PyStyle(self, param):
    Str = ''.join([c.replace(' ', '') for c in param[0].lower()])

    return sum(v % 2 for v in Counter(Str).values()) <= 1

  def ImprovedNaive(self, param):
    Str = param[0].lower()

    len_of_bucket = [0] * (len(CHARS_SET) / 2)

    # When the length of string (exception space) is even
    # The all each character should be occurs even.
    # Otherwise, the only one character occurs odd.
    for s in Str:
      if s != ' ':
        idx = ord(s) - ord('a')
        len_of_bucket[idx] += 1

    return sum(l % 2 for l in len_of_bucket) <= 1

def solve():
  ex = Ex_01_04()

  ex.add_solution(Ex0104("Naive"))
  ex.add_solution(Ex0104("PyStyle"))
  ex.add_solution(Ex0104("ImprovedNaive"))

  ex.solve()

if __name__ == "__main__":
  solve()
