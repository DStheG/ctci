#!/usr/bin/python

class Queue():
  def __init__(self):
    self.queue = []

  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if len(self.queue) == 0:
      return None
    return self.queue.pop(0)

  def __repr__(self):
    return str(self.queue)
