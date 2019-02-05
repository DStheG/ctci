#!/usr/bin/python
class Node:
  def __init__(self, dataval=None):
    self.dataval = dataval
    self.nextval = None

  def Next(self):
    return self.nextval

  def getData(self):
    return self.dataval

class SLinkedList:
  def __init__(self):
    self.headval = None
    self.l = 0

  def __str__(self):
    s = '['
    n = self.headval
    idx = 0
    while(n != None):
      if( idx > self.l ):
        break
      s += ' '
      s += str(n.dataval)
      n = n.nextval
      idx += 1
    s += ' ]'

    return s

  __repr__ = __str__

  def __len__(self):
    return self.l

  def append(self, newData):
    if isinstance(newData, Node):
      NewNode = newData
    else :
      NewNode = Node(newData)
    if self.headval is None:
      self.headval = NewNode
      return NewNode
    laste = self.headval
    while(laste.nextval):
      laste = laste.nextval
    laste.nextval = NewNode
    self.l += 1

    return NewNode

  def appendAsIs(self, newData):
    NewNode = Node(newData)
    if self.headval is None:
      self.headval = NewNode
      return NewNode
    laste = self.headval
    while(laste.nextval):
      laste = laste.nextval
    laste.nextval = NewNode
    self.l += 1

    return NewNode

  def front(self, newData):
    if isinstance(newData, Node):
      NewNode = newData
    else:
      NewNode = Node(newData)
    if self.headval is None:
      self.headval = NewNode
      return
    NewNode.nextval = self.headval
    self.headval = NewNode
    self.l += 1

  def remove(self, n):
    if(n is None):
      return
    prev = self.headval
    if(prev is n):
      self.headval = n.nextval
      self.l -= 1
      return
    while(prev.nextval != n):
      prev = prev.nextval
      if(prev is None):
        return
    prev.nextval = n.nextval
    self.l -= 1
