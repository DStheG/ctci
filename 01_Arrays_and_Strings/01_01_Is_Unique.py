#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
1.1 Is Unique
  Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import random
import string

import timeit

CHARS_SET = string.ascii_letters + string.digits + string.punctuation

def string_gen(size=10, chars=CHARS_SET):
  return ''.join(random.choice(chars) for _ in range(size))

class Exercise(object):
  def __init__(self):
    self.solutions = []
    self.param = []

  def setup(self):
    pass

  def teardown(self):
    pass

  def add_solution(self, solution):
    self.solutions.append(solution)

  def solve(self):
    self.setup()
    print self.param

    for s in self.solutions:
      print s.name
      self.start = timeit.default_timer()
      print "\t[    Unique]" if s.solution(self.param) else "[NOT Unique]",
      self.stop = timeit.default_timer()
      print " [Time: %.4f ms]" % ((self.stop - self.start) * 1000)

    self.teardown()

class Solution:
  def __init__(self, name):
    self.name = name

  def solution(self, param):
    return getattr(self, self.name)(param)

class Ex_01_01(Exercise):
  def setup(self):
    self.param.append(string_gen())

class Naive(Solution):
  # O(N*N)
  def NaiveSolution(self, param):
    r_str = param[0]
    for i in range(len(r_str)):
      for j in range(i+1, len(r_str)):
        if r_str[i] == r_str[j]:
          return False
    return True

class Sort(Solution):
  def qsort(self, s):
    p = 0; l = 1
    r = len(s) - 1

    if(r <= 0):
      return ''.join(s)

    while (l <= r):
      while ((s[p] >= s[l]) and (l < r)):
        l = l + 1
      while ((s[p] < s[r]) and (l < r)):
        r = r - 1
      if(l == r):
        if(s[p] > s[l]):
          s[p], s[l] = s[l], s[p]
        else:
          s[p], s[l-1] = s[l-1], s[p]
        break;
      else:
        s[l], s[r] = s[r], s[l]

    return ''.join(self.qsort(s[:l])) + ''.join(self.qsort(s[l:]))

  def SortSolution(self, param):
    r_str = param[0]
    sorted_str = self.qsort(list(r_str))

    for i in range(1, len(sorted_str)):
      if sorted_str[i-1] == sorted_str[i]:
        return False
    return True

def solve():
  ex = Ex_01_01()

  ex.add_solution(Naive("NaiveSolution"))
  ex.add_solution(Sort("SortSolution"))

  ex.solve()

if __name__ == "__main__":
  solve()
