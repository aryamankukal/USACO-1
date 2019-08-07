"""
ID: wrwwctb1
LANG: PYTHON3
TASK: barn1
1.4.3

key idea
don't cover the M-1 largest voids (continuous sequence of stalls without cows)

always consider change of perspective: here, start with boards or voids?
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

filename = 'barn1'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







M, S, C = list(map(int, input().split()))
cows = []
for c in range(C):
    cows.append(int(input()))

# look for voids
cows.sort()
voids = []
for i in range(C-1):
    if cows[i] + 1 != cows[i+1]:
        voids.append([cows[i], cows[i+1], cows[i+1] - cows[i] - 1])

# decide which voids to not cover
if len(voids) <= M-1:
    # choose all
    pass
else:
    # choose M-1 largest voids
    voids.sort(key=lambda void: void[2], reverse=True)
    del voids[M-1:]

# find length between voids
voids.sort(key=lambda void: void[0])

voids = [[0, cows[0], None]] + voids + [[cows[-1], len(cows)-1, None]]

tot = 0
for i in range(len(voids)-1):
    tot += voids[i+1][0] - voids[i][1] + 1

printwrite(tot)




fin.close()
fout.close()
del print, input

