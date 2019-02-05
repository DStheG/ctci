#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
03.04.Queue via Stacks
  Implement a MyQueue class which implements a queue using two stacks.
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
      return

    self.sp -= 1
    val = self.stack[self.sp]

    return val

class MyQueue():
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def push(self, val):
    self.stack1.push(val)

  def pop(self):
    val = self.stack1.pop()
    while(val != None):
      self.stack2.push(val)
      val = self.stack1.pop()
    ret = self.stack2.pop()

    val = self.stack2.pop()
    while(val != None):
      self.stack1.push(val)
      val = self.stack2.pop()

    return ret

class Sol(Solution):
  def Naive(self, param):
    val = param[0]
    queue = MyQueue()

    for s in val:
      queue.push(s)

    val = queue.pop()
    while(val != None):
      print val
      val = queue.pop()

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
