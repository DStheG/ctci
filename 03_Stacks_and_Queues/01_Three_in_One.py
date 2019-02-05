#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
03.01.Three in One
      Describe how you could use a single array to implement three stacks.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen

CHARS_SET = string.lowercase

class Ex_03_01(Exercise):
  def setup(self):
    stack_size = 10*3
    stack = [0] * stack_size

    self.param.append(stack)
    self.param.append(stack_size)

class Ex0301(Solution):
  def show(self, stack, base, size):
    for i in range(size):
      print stack[base + i],
    print

  def push(self, stack, base, sp, size, val):
    if sp - base >= size :
      print 'stack is full'
      return sp
    stack[sp] = val
    return sp + 1

  def pop(self, stack, base, sp, size):
    if sp - base <= 0 :
      print 'stack is empty'
      return sp, None
    val = stack[sp]
    return sp - 1, val

  def Naive(self, param):
    stack = param[0]
    full_stack_size = param[1]

    base_sp1 = sp1 = 0
    base_sp2 = sp2 = full_stack_size / 3
    base_sp3 = sp3 = 2 * full_stack_size / 3

    stack_size = full_stack_size / 3

    sp1, val = self.pop(stack, base_sp1, sp1, stack_size)

    for _ in range(11):
      sp1 = self.push(stack, base_sp1, sp1, stack_size, 1)
      sp2 = self.push(stack, base_sp2, sp2, stack_size, 2)
      sp3 = self.push(stack, base_sp3, sp3, stack_size, 3)
    sp1, val = self.pop(stack, base_sp1, sp1, stack_size)

    print val

    self.show(stack, base_sp1, stack_size)
    self.show(stack, base_sp2, stack_size)
    self.show(stack, base_sp3, stack_size)

def solve():
  ex = Ex_03_01()

  ex.add_solution(Ex0301("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
