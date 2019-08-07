"""
ID: wrwwctb1
LANG: PYTHON3
TASK: money
2.3.4

key idea
unbounded knapsack
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

filename = 'money'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')
ttt = time.time()








'''

c1 n1 + c2 n2 + c3 n3 .. = N

'''
V, N = map(int, input().split())
coins = [0]
while True:
    line = input()
    if line == '':
        break
    coins.extend(map(int, line.split()))
coins = sorted(set(coins))
V = len(coins) - 1

nw = [0] * (N + 1)
nw[0] = 1
for v in range(1, V + 1):
    for n in range(N + 1):
        if n + coins[v] <= N:
            nw[n + coins[v]] += nw[n]

printwrite(nw[-1])







fin.close()
fout.close()
del print, input
print(time.time() - ttt)
