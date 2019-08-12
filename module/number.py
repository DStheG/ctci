#!/usr/bin/python

import math

def crossOff(flags, prime):
  for i in range(prime*prime, len(flags), prime):
    flags[i] = False

def getNextPrime(flags, prime):
  Next = prime + 1
  while(Next < len(flags) and not flags[Next]):
    Next+=1
  return Next

def sieveOfEratosthenes(Max):
  flags = [True] * (Max + 1)
  prime = 2
  print math.sqrt(Max)
  while(prime <= math.sqrt(Max)):
    crossOff(flags, prime)
    prime = getNextPrime(flags, prime)

  return flags

print sieveOfEratosthenes(10)
