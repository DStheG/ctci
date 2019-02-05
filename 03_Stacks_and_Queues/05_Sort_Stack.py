#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
03.05. Sort Stack
  Write a program to sort a stack such that the smallest items are on the
  top. You can use an additional temporary stack, but you may not copy the
  elements into any other data structure (such as an array). The stack suppo-
  rts the following operations: push, pop, peek, and isEmpty.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

CHARS_SET = string.lowercase

class Ex(Exercise):
  def setup(self):
    N = random.randint(10, 10)
    stack = [random.randint(0,100) for _ in range(N)]

    self.param.append(stack)

class Stack():
  def __init__(self, size=10):
    self.size = size
    self.stack = [0] * size
    self.sp = 0

  def show(self):
    print self

  def __str__(self):
    s = '['
    for i in range(self.sp):
      s += str(self.stack[i]) + ' '

    s += ']'
    return s

  __repr__ = __str__

  def isEmpty(self):
    return self.sp == 0

  def isFull(self):
    return self.sp == self.size

  def push(self, val):
    if self.isFull():
      return

    self.stack[self.sp] = val
    self.sp += 1

  def pop(self):
    if self.isEmpty():
      return None

    self.sp -= 1
    val = self.stack[self.sp]

    return val

  def peek(self):
    if self.isEmpty():
      return None

    val = self.stack[self.sp-1]
    return val

class SortStack():
  def __init__(self):
    self.stack = Stack()

  def  __str__(self):
    return self.stack.__str__()

  __repr__ = __str__

  def pour(self, stack):
    val = stack.pop()
    while(val is not None):
      self.stack.push(val)
      val = stack.pop()

  def push(self, val):
    if self.stack.isEmpty():
      self.stack.push(val)
      return

    temp_stack = Stack()
    peek = self.stack.peek()
    while(peek is not None):
      if (peek >= val):
        self.stack.push(val)
        self.pour(temp_stack)
        return
      self.stack.pop()
      temp_stack.push(peek)
      peek = self.stack.peek()

    self.stack.push(val)
    self.pour(temp_stack)

  def pop(self):
    return self.stack.pop()

class Sol(Solution):
  def Naive(self, param):
    val = param[0]
    stack = SortStack()

    for s in val:
      stack.push(s)

    return stack

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
