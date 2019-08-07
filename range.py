"""
ID: wrwwctb1
LANG: PYTHON3
TASK: range
3.3.5

key idea
l_ij: the largest sq size if i j is the sq's lower right corner

if l_ij >= 2, it contributes 1 count to squares of size 2, 3, ..., and l_ij


had another sol using pairwise "and". confidence building
"""

import os, sys, re
from collections import Counter, deque, defaultdict
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key, partial as functools_partial
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
         pi, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)
# python -m cProfile -s time ha.py

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'range'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')












# input
N = int(input())
s = [[0] * (N + 1)]
for n in range(N):
    line = input()
    line = [int(i) for i in line]
    s.append([0] + line)

# find l, largest sq size, i j as lower right
l = [[0] * (N + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if s[i][j] == 0:
            continue
        else:
            left = l[i][j-1]
            top = l[i-1][j]
            if left != top:
                l[i][j] = min(left, top) + 1
            else:
                if s[i-left][j-left]:
                    l[i][j] = left + 1
                else:
                    l[i][j] = left

ans = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for size in range(2, l[i][j] + 1):
            ans[size] += 1

for size, num in enumerate(ans):
    if num:
        printwrite('%d %d' % (size, num))








fin.close()
fout.close()
del print, input

