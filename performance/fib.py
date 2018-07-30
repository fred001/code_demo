#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)

def fibonacci(i):
  if i<2:
    return i

  return fibonacci(i-2) + fibonacci(i-1)

print(fibonacci(34))
