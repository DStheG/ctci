#!/usr/bin/python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
05.08.Draw Line
  A monochrome screen is stored as a single array of bytes, allowing eight c-
  onsecutive pixels to be stored in one byte. The screen has width w, where w
  is divisible by 8 (that is, no byte will be split across rows). The height
  of the screen, of course, can be derived from the length of the array and
  the width. Implement a function that draws a horizontal line from(x1, y) to
  (x2, y). The method signature should look something like:
  drawLine(byte[] screen, int width, int x1, int x2, int y)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string
import sys

import ctypes

sys.path.append("../")

from module.ctci  import Exercise
from module.ctci  import Solution

class Ex(Exercise):
  def setup(self):
    self.param.append(64)
    self.param.append(20)
    self.param.append(42)
    self.param.append(1)

class Sol(Solution):
  def setPixel(self, screen, width, x, y):
    group = x / 8
    offset = x % 8
    idx = (width / 8) * y + group
    value = screen[idx]
    screen[idx] |= (0x80 >> offset)

  def drawLine(self, screen, width, x1, x2, y):
    for x in range(x1, x2 + 1):
      self.setPixel(screen, width, x, y)

  def Naive(self, param):
    width = param[0]
    x1    = param[1]
    x2    = param[2]
    y     = param[3]
    if (width % 8):
      print "Width should be divisible by 8"
      return False

    screen = [0] * (width / 8) * (y + 1)
    self.drawLine(screen, width, x1, x2, y)

    return screen

  def setByte(self, screen, width, x, y, val):
    group = x / 8
    offset = x % 8
    idx = (width / 8) * y + group
    screen[idx] = val

  def drawLineBetter(self, screen, width, x1, x2, y):
    new_base = (x1 / 8) * 8
    next_base = new_base + 8
    bitmap = (1 << (next_base - x1)) - 1
    if(x2 < next_base - 1):
      bitmap ^= (1 << (next_base - 1) - x2) - 1
    self.setByte(screen, width, x1, y, bitmap)

    idx1 = next_base / 8
    idx2 = (x2 / 8)
    for idx in range(idx1, idx2):
      self.setByte(screen, width, idx*8, y, 255)

    if( x2 - x1 > 8):
      last_base = (x2 / 8) * 8
      bitmap = (0xff << (8 - (x2 - last_base + 1))) & 0xff
      self.setByte(screen, width, x2, y, bitmap)

  def Better(self, param):
    width = param[0]
    x1    = param[1]
    x2    = param[2]
    y     = param[3]
    if (width % 8):
      print "Width should be divisible by 8"
      return False

    screen = [0] * (width / 8) * (y + 1)
    self.drawLineBetter(screen, width, x1, x2, y)

    return screen

def solve():
  ex = Ex()

  ex.add_solution(Sol("Naive"))
  ex.add_solution(Sol("Better"))
  ex.solve()

if __name__ == "__main__":
  solve()
