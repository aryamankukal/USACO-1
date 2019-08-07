"""
ID: wrwwctb1
LANG: PYTHON3
TASK: namenum
1.3.4

key idea
for any matching problem, given an element a in A,
to find corresponding elements in B, which of the following is easier?

1. using a, assemble possible elements bcand, see which is in B

2. go through all b in B, see which matches a

here, 1 involves backtracking. 2 is much faster, much easier to code
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

filename = 'namenum'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








ch2num = {'A': 2, 'B': 2, 'C': 2,
          'D': 3, 'E': 3, 'F': 3,
          'G': 4, 'H': 4, 'I': 4,
          'J': 5, 'K': 5, 'L': 5,
          'M': 6, 'N': 6, 'O': 6,
          'P': 7, 'R': 7, 'S': 7,
          'T': 8, 'U': 8, 'V': 8,
          'W': 9, 'X': 9, 'Y': 9,

          'Q':-1, 'Z':-1}


N = int(input())
digs = []
while N > 0:
    N, rem = divmod(N, 10)
    digs.append(rem)
digs = digs[::-1]

namef = open('dict.txt', 'r')

hasans = False
while True:
    name = namef.readline().strip()
    if name == '':
        break
    namenum = []
    for ch in name:
        namenum.append(ch2num[ch])
    if namenum == digs:
        printwrite(name)
        hasans = True

if not hasans:
    printwrite('NONE')





namef.close()
fin.close()
fout.close()
del print, input

