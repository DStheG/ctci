#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.07.Build_Order
  You are given a list of projects and a list of dependencies (which is a li-
  st of pairs of projects, where the second project is dependent on the firs-
  t project). All of a project's depedencies must be built before the projec-
  t is. Find a build order that will allow the projects to be built. If there
  is no valid build order, return an error.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Node(object):
  def __init__(self, val):
    self.parent = {}
    self.child = {}
    self.val = val

class Ex(Exercise):
  def setup(self):
    self.param.append(['a', 'b', 'c', 'd', 'e', 'f'])
    self.param.append([['a', 'd'], ['f', 'b'], ['b', 'd'],
                        ['f', 'a'], ['d', 'c']])

class Sol(Solution):
  def getAllDescendants(self, node):
    queue = []
    visitQueue = []
    queue += node.child.keys()
    while(queue):
      v = queue.pop(0)
      if(v in visitQueue):
        continue
      visitQueue.append(v)
      queue += self.dict[v].child.keys()

    return visitQueue

  def checkCyclic(self):
    for i in self.dict:
      descendants = self.getAllDescendants(self.dict[i])
      if i in descendants:
        return True
    return False

  def isRoot(self, v):
    node = self.dict[v]
    return not node.parent

  def BFS(self, v):
    node = self.dict[v]
    queue = self.dict[v].child.keys()
    ret = [v]
    while(queue):
      val = queue.pop(0)
      ret.append(val)
      queue += self.dict[val].child.keys()

    return ret

  def removeDup(self, l):
    ret = []
    for v in l:
      if not v in ret:
        ret += v
    return ret

  def Naive(self, param):
    self.dict = {}
    for i in param[0]:
      self.dict[i] = Node(i)

    for i in param[1]:
      t, f = i
      node = self.dict[f]
      pnode = self.dict[t]
      if not t in node.parent:
        node.parent[t] = self.dict[t]
      if not f in pnode.child:
        pnode.child[f] = node

    if self.checkCyclic():
      return 'error'

    output = []
    for i in param[0]:
      if self.isRoot(i):
        output += self.BFS(i)

    return self.removeDup(output)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
