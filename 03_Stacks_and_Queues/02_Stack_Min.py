#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
03.02.Stack Min
      How would you design a stack which, in addition to push and pop, has a
      function min which returns the minimum element? Push, pop and min 
      should all operate in O(1) time.
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

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
    self.prev = None
    self.min_node = None

  def setNext(self, Next):
    self.next = Next

  def setPrev(self, Prev):
    self.prev = Prev

  def setMin(self, MinNode):
    self.min_node = MinNode

  def getMin(self):
    return self.min_node

  def getMinVal(self):
    return self.min_node.getVal()

  def getNext(self):
    return self.next

  def getPrev(self):
    return self.prev

  def getVal(self):
    return self.val

class Stack():
  def __init__(self):
    self.head = None
    self.sp = None
    self.min = None

  def show(self):
    print self

  def __str__(self):
    node = self.head
    s = '['
    while(node != None):
      s += str(node.getVal()) + ' '
      node = node.getNext()

    s += ']'
    return s

  __repr__ = __str__

  def push(self, val):
    node = Node(val)
    if(self.head == None):
      self.head = node
      self.sp = node
      self.min = node
      node.setMin(node)
    else:
      self.sp.setNext(node)
      node.setPrev(self.sp)
      if(node.getVal() < self.sp.getMinVal()):
        node.setMin(node)
      else:
        node.setMin(self.sp.getMin())
      self.sp = node

  def pop(self):
    if(self.sp == None):
      return None
    node = self.sp
    self.sp = node.getPrev()
    if(self.sp is not None):
      self.sp.setNext(None)
    else:
      self.head = None

    return node.getVal()

  def getMinVal(self):
    if(self.sp is None):
      return None
    return self.sp.getMinVal()

class Sol(Solution):
  def Naive(self, param):
    val = param[0]
    stack = Stack()

    for s in val:
      stack.push(s)
    stack.pop()

    print
    print '\tCurrent Stack: ',
    print stack

    return stack.getMinVal()

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
