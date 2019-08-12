#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
06.09.100 Lockers
  There are 100 closed lockers in a hallway. A man begins by opening all 100
  lockes. Next, he closes every second locker. Then, on this third pass, he
  toggles every third locker (closes it if it is open or opens it if it is
  closed). This process continues for 100 passes, such that on each pass i,
  the man toggles every i th locker. After his 100th pass in the hallways,
  in which he toggles only locker #100, how many lockers are open?
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random
import math

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(100)

class Sol(Solution):
  def Naive(self, param):
    N = param[0]
    cnt = 0
    for i in range(1, N+1):
      acc = 1
      for j in range(1, i):
        n = 0 if i % j else 1
        acc += n
      if(acc % 2):
        cnt += 1
    return cnt

  def Fast(self, param):
    N = param[0]
    cnt = 0
    # The locker opened mean, there are odd numbers which can divide the # locker
    # If some number can divide some other number mean there are pair number,
    # In other word, N = x * y. x and y is pair.
    # So that, the only chance N opened if and only if sqrt(N) is integer
    for i in range(1, N+1):
      if not (math.sqrt(i) - int(math.sqrt(i))):
        cnt += 1

    return cnt

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.add_solution(Sol("Fast"))
  ex.solve()

if __name__ == "__main__":
  solve()
