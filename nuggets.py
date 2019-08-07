"""
ID: wrwwctb1
LANG: PYTHON3
TASK: nuggets
4.1.2

key idea
unbounded knapsack

past[curr]: at curr nuggets, is there a solution?

condition (2e9) only looks harsh
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

filename = 'nuggets'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









from functools import reduce



N = int(input())
aa = []
for n in range(N):
    aa.append(int(input()))

g = reduce(gcd, aa)

if g != 1: # not coprime
    printwrite(0)
else:
    aa = sorted(set(aa))
    mina = aa[0]
    maxa = aa[-1]
    combo = 0
    tomod = maxa + 1
    past = [False] * tomod # only need maxa + 1 terms
    curr = mina - 1 # everything < mina has no sol
    while True:

        # exit condition
        if combo > mina:
            printwrite(curr - mina - 1)
            break

        curr += 1

        # is multiple of some a? this turns out not necessary
        flag = False
        for a in aa:
            if curr % a == 0:
                flag = True
                break
        if flag:
            past[curr % tomod] = True
            combo += 1
            continue

        # does some of curr's past allow sol? unbounded knapsack
        flag = False
        for a in aa:
            if past[(curr - a) % tomod]:
                flag = True
                break
        if flag:
            past[curr % tomod] = True
            combo += 1
            continue

        # no sol
        past[curr % tomod] = False
        combo = 0





















fin.close()
fout.close()
del print, input

