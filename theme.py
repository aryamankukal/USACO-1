"""
ID: wrwwctb1
LANG: PYTHON3
TASK: theme
5.1.4

key idea
consider sequence starting at i, and sequence starting at j
define d[i][j]: length of theme common to the above sequences
naive d[i][j] gives bad alloc for c++ on usaco
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

filename = 'theme'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')













N = int(input())
m = []
while True:
    line = input()
    if line == '':
        break
    m.extend(map(int, line.split()))


# initialize
#d = [[1] * N for n in range(N)]
#for i in range(N):
#    for j in range(i+1):
#        d[i][j] = 0

# crawl
best = 1 # can be 0 but masked by output anyway

for imax in range(N-3, -1, -1):
    i = imax
    j = N - 2
    di1j1 = 1 # d[i+1][j+1]
    while i >= 0:
#        if m[i+1] - m[i] == m[j+1] - m[j]:
#            d[i][j] = min(1 + d[i+1][j+1], j-i)
#            best = max(best, d[i][j])

        if m[i+1] - m[i] == m[j+1] - m[j]:
            dij = min(1 + di1j1, j-i)
            best = max(best, dij)
            di1j1 = dij
        else:
            di1j1 = 1


        i -= 1
        j -= 1

if best >= 5:
    printwrite(best)
else:
    printwrite(0)










fin.close()
fout.close()
del print, input

