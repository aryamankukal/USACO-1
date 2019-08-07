"""
ID: wrwwctb1
LANG: PYTHON3
TASK: fact4
3.2.2

key idea
curr = 1
for each i in range(2, N + 1):
    factor out 2s and 5s
    curr *= i
    curr %= 10 to keep the last dig
consider 2s and 5s in the end

this
    fixes the ans at the last digit, allowing %= 10
    avoids any potential error such as 12 * 15 = 180 vs 2 * 15 = 30
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

filename = 'fact4'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









N = int(input())
curr = 1
n2n5 = 0 # num 2s - num 5s
for i in range(2, N + 1):
    # remove 2s
    while True:
        m, r = divmod(i, 2)
        if r:
            break
        else:
            n2n5 += 1
            i = m
    # remove 5s
    while True:
        m, r = divmod(i, 5)
        if r:
            break
        else:
            n2n5 -= 1
            i = m
    # multiply
    curr *= i
    curr %= 10

# put back excess 2s
for i in range(n2n5):
    curr *= 2
    curr %= 10
printwrite(curr)










fin.close()
fout.close()
del print, input

