"""
ID: wrwwctb1
LANG: PYTHON3
TASK: checker
6.5.5
"""

import os, sys, re, time
from collections import Counter, deque, defaultdict
from queue import Queue
from copy import copy, deepcopy
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

filename = 'checker'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








def recurse(row):
    if row == N + 1:
        global cnt
        cnt += 1
        if cnt <= 3:
            printwrite(' '.join(['%d'] * N) % tuple(history))
        return
    for col in range(1, N+1):
        if cc[col]: # occupied
            continue
        if d1[N - row + col]:
            continue
        if d2[row + col - 1]:
            continue
        if cnt <= 3:
            history.append(col)
        cc[col] = True
        d1[N - row + col] = True
        d2[row + col - 1] = True

        recurse(row + 1)

        if cnt <= 3:
            del history[-1]
        cc[col] = False
        d1[N - row + col] = False
        d2[row + col - 1] = False



N = int(input())


Nmax = 13
d1 = [False] * (2 * Nmax) # diagonals 73. False: can occupy
d2 = [False] * (2 * Nmax) # diagonals 19
cc = [False] * (Nmax + 1) # columns
history = []
cnt = 0

recurse(1)

printwrite(cnt)










fin.close()
fout.close()
del print, input

