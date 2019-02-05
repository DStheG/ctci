#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
03.03.Stack of Plates
  Imagine a (literal) stack of plates. If the stack gets too high, it might
  topple. Therefore, in real life, we would likely star a new stack when the
  previous stack exceeds some threashold, implement a data structure SetOfSt-
  acks that mimics this. SetOfStacks should be composed of several stacks and
  should create a new stack once the previous one exceeds capacity. SetOfSta-
  cks.push() and SetOfStacks.pop() should behave identically to a single sta-
  ck (that is, pop() should return the same values as it would if there were
  just a single stack).
  FOLLOW UP
  Implement a function popAt(int index) which performs a pop operations on
  specific sub-stack.
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
    N = random.randint(15, 15)
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

class SetOfStacks():
  def __init__(self):
    self.stacks = []
    self.idx = -1

  def __str__(self):
    s = ''
    for stack in self.stacks:
      s += '[ '
      for i in range(stack.sp):
        s += str(stack.stack[i]) + ' '
      s += ']'
    return s

  __repr__ = __str__

  def push(self, val):
    if(self.idx == -1):
      self.stacks.append(Stack())
      self.idx = 0

    stack = self.stacks[self.idx]
    if(stack.isFull()):
      self.stacks.append(Stack())
      self.idx += 1
      stack = self.stacks[self.idx]

    stack.push(val)

  def pop(self):
    if(self.idx == -1):
      return None

    return self.popAt(len(self.stacks) - 1)

  def popAt(self, index):
    if(index < 0 or index >= len(self.stacks)):
      return None

    stack = self.stacks[index]
    val = stack.pop()
    if(index < len(self.stacks) - 1):
      stack.size -= 1
    if(stack.isEmpty()):
      self.stacks.remove(stack)
      self.idx -= 1

class Sol(Solution):
  def Naive(self, param):
    val = param[0]
    stack = SetOfStacks()

    for s in val:
      stack.push(s)
    [stack.popAt(0) for _ in range(6)]
    [stack.push(-1) for _ in range(10)]
    [stack.popAt(1) for _ in range(2)]
    [stack.popAt(0) for _ in range(10)]

    print
    print '\tCurrent Stack: ',
    print stack

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
