#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)

def cal(n):
  if n <= 0 : return 0

  return n+cal(n-1)


n=1000
total=cal(n)

print(total)
