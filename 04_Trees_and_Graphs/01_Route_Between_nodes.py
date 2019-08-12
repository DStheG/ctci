#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
04.01.Route Between Nodes
      Given a directed graph, design an algorithm to find out whether there
      is a route between two nodes.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution
from module.str   import string_gen

class Graph():
  def __init__(self, node_size):
    self.graph = [[0] * node_size for i in range(node_size)]

  def add_path(self, From, To):
    self.graph[From][To] = 1

  def __str__(self):
    ret = '\n'
    for i in range(len(self.graph)):
      ret += str(self.graph[i]) + '\n'
    return ret
  __repr__ = __str__

  def __getitem__(self, row):
    return self.graph[row]

  def extract_can_move_list(self, node_idx):
    travel_queue = []
    for i in range(len(self.graph)):
      if self.graph[node_idx][i] == 1:
        travel_queue.append(i)
    return travel_queue

  def find_path(self, From, To):
    visit_list = [0] * len(self.graph)
    visit_list[From] = 1

    travel_queue = []

    travel_queue += self.extract_can_move_list(From)

    while(travel_queue):
      i = travel_queue.pop(0)
      if i == To:
        return True
      if visit_list[i]:
        continue
      visit_list[i] = 1
      travel_queue += self.extract_can_move_list(i)
    return False

class Ex(Exercise):
  def setup(self):
    node_size = 5

    graph = Graph(node_size)
    graph.add_path(0, 1)
    graph.add_path(1, 2)
    graph.add_path(2, 3)
    graph.add_path(3, 4)
    graph.add_path(4, 0)

    self.param.append(graph)

class Sol(Solution):
  def Naive(self, param):
    graph = param[0]
    print graph.find_path(2, 3)

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.solve()

if __name__ == "__main__":
  solve()
