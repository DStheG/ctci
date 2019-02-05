#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
03.06. Animal Shelter
  An animal shelter, which holds only dogs and cats, operates on a trickly
  "first in, first out" basis. People must adopt the "oldest" (based on arri-
  val time) of all animals at the shelter, or they can select wheter they wo-
  uld prefer a dog or a cat (and will receive the oldest animal of that type)
  They cannot select which specific animal they would like. Create the data
  structures to maintain this system and implement operations such as enqueu-
  e, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked-
  List data structure.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.slist import SLinkedList

class Ex(Exercise):
  def setup(self):
    N = random.randint(10, 10)
    Animals = [random.randint(0,100) for _ in range(N)]

    self.param.append(Animals)

class Sol(Solution):
  def isDog(self, v):
    return (v % 2) == 0
  def isCat(self, v):
    return (v % 2)

  def enqueue(self, v):
    if not self.isDog(v):
      n = self.Cats.append(v)
    else:
      n = self.Dogs.append(v)
    self.Animals.appendAsIs(n)

  def dequeueAny(self):
    n = self.Animals.headval
    if(n is not None):
      self.Animals.remove(n)
      if(self.isDog(n.dataval.dataval)):
        self.Dogs.remove(n.dataval)
      else:
        self.Cats.remove(n.dataval)

    return n.dataval.dataval

  def dequeueDog(self):
    n = self.Dogs.headval
    self.Dogs.remove(n)
    if(n is not None):
      an = self.Animals.headval
      while(an is not None):
        if(an.dataval is n):
          self.Animals.remove(an)
          return n.dataval
        an = an.nextval
    return n.dataval

  def dequeueCat(self):
    n = self.Cats.headval
    self.Cats.remove(n)
    if(n is not None):
      an = self.Animals.headval
      while(an is not None):
        if(an.dataval is n):
          self.Animals.remove(an)
          return n.dataval
        an = an.nextval
    return n.dataval

  def Naive(self, param):
    self.Animals = SLinkedList()
    self.Dogs = SLinkedList()
    self.Cats = SLinkedList()

    val = param[0]

    # even Dog, odd Cat
    for v in val:
      self.enqueue(v)

    print self.Dogs
    print self.Cats

    print self.dequeueAny()
    print self.dequeueCat()
    print self.dequeueCat()
    print self.dequeueCat()

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))

  ex.solve()

if __name__ == "__main__":
  solve()
