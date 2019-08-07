"""
ID: wrwwctb1
LANG: PYTHON3
TASK: sprime
1.6.4

key idea
dfs. check primality every level
the top level has different choices (2, 3, 5, 7) from other levels (1, 3, 7, 9)
"""

import os, sys, re, itertools, functools, heapq
from collections import Counter, deque
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
             sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan


print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip()

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'sprime'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







def isprime(n):
    if n <= 1:
        return False
    top = int(sqrt(n)) + 1
    for i in range(2, top):
        if n % i == 0:
            return False
    return True

def dfs(curr, left, out):
    if left == 0:
        currnum = int(''.join(curr))
        out.append(currnum)
        return

    left -= 1
    for i in [1, 3, 7, 9]: # others will make currnum divisible by 2 or 5
        curr += str(i)
        currnum = int(''.join(curr))
        if isprime(currnum):
            dfs(curr, left, out)
        del curr[-1]


N = int(input())

out = []

dfs(['2'], N-1, out)
dfs(['3'], N-1, out)
dfs(['5'], N-1, out)
dfs(['7'], N-1, out)

for n in out:
    printwrite(n)







fin.close()
fout.close()
del print, input

