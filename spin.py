"""
ID: wrwwctb1
LANG: PYTHON3
TASK: spin
3.2.4

key idea
the system returns to the starting state after 360 seconds
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

filename = 'spin'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')






def cyclic(ls, n):
    n = -n
    n %= len(ls)
    ls[:] = ls[n:] + ls[:n]

def wedges2list(wedges):
    ls = [0] * 360
    for start, span in wedges:
        for ang in range(start, start+span+1):
            ang %= 360
            ls[ang] = 1
    return ls


def check(lss, S):
    for t in range(360):
        for i in range(360):
            if lss[0][i] and lss[1][i] and lss[2][i] and lss[3][i] and lss[4][i]:
                return t
        cyclic(lss[0], S[0])
        cyclic(lss[1], S[1])
        cyclic(lss[2], S[2])
        cyclic(lss[3], S[3])
        cyclic(lss[4], S[4])
    return 'none'

S = []
W = []
wed = []
for i in range(5):
    line = list(map(int, input().split()))
    S.append(line[0])
    W.append(line[1])
    del line[:2]
    wed.append(list(zip(line[::2], line[1::2])))

lss = []
for wedges in wed:
    lss.append(wedges2list(wedges))

#import matplotlib.pyplot as pl
#pl.plot(lss[4])
#assert False
printwrite(check(lss, S))





fin.close()
fout.close()
del print, input

