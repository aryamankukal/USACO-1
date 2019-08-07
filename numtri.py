"""
ID: wrwwctb1
LANG: PYTHON3
TASK: numtri
1.6.2

key idea
bottom up, level by level. calc max route sum toward base
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

filename = 'numtri'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







N = int(input())
rows = []
for n in range(N):
    row = list(map(int, input().split()))
    rows.append(row)

for r in range(N-1, 0, -1):
    for i in range(r):
        rows[r-1][i] += max(rows[r][i], rows[r][i+1])

printwrite(rows[0][0])






fin.close()
fout.close()
del print, input

