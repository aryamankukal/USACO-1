"""
ID: wrwwctb1
LANG: PYTHON3
TASK: subset
2.2.4

key idea
0-1 knapsack
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

filename = 'subset'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')
ttt = time.time()




N = int(input())
tot = (1 + N) * N // 2
if tot % 2 == 1:
    printwrite(0)
else:
    need = tot // 2
    nw = [0] * (need + 1)
    nw[0] = 1
    for use in range(1, N + 1):
        for reach in range(need, 0, -1):
            if reach - use >= 0:
                nw[reach] += nw[reach - use]
    printwrite(nw[-1] // 2)





fin.close()
fout.close()
del print, input
print(time.time() - ttt)
