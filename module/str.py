#!/usr/bin/python
import string
import random

CHARS_SET = string.printable

def string_gen(size=10, chars=CHARS_SET):
  return ''.join(random.choice(chars) for _ in range(size))
