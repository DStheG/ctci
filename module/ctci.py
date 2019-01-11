#!/usr/bin/python
import timeit

class Exercise(object):
  def __init__(self):
    self.solutions = []
    self.param = []
    self.max_name_size = 0

  def setup(self):
    pass

  def teardown(self):
    pass

  def add_solution(self, solution):
    self.solutions.append(solution)
    self.max_name_size = max(self.max_name_size, len(solution.name))

  def solve(self):
    self.setup()
    print self.param

    for s in self.solutions:
      print '{0: <{1}}'.format(s.name, self.max_name_size),
      self.start = timeit.default_timer()
      ret = s.solution(self.param)
      self.stop = timeit.default_timer()
      print '[{0}]'.format(ret),
      print " [Time: %.4f ms]" % ((self.stop - self.start) * 1000)

    self.teardown()

class Solution:
  def __init__(self, name):
    self.name = name

  def solution(self, param):
    return getattr(self, self.name)(param)
