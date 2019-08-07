"""
ID: wrwwctb1
LANG: PYTHON3
TASK: bigbrn
5.3.5

key idea
dp

compare with rectbarn
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

filename = 'bigbrn'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')






N, T = map(int, input().split()) # 1-1k, 1-10k

barn = [[None] * (N+1) for n in range(N+1)]
for t in range(T):
    i, j = map(int, input().split())
    barn[i][j] = 0
for i in range(N+1):
    barn[0][i] = barn[i][0] = 0

best = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if barn[i][j] == 0:
            continue
        else:
            temp = min(barn[i-1][j], barn[i][j-1], barn[i-1][j-1]) + 1
            best = max(best, temp)
            barn[i][j] = temp

printwrite(best)








fin.close()
fout.close()
del print, input

