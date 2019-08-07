"""
ID: wrwwctb1
LANG: PYTHON3
TASK: picture
5.5.1

key idea
x, y considered separately. for each dir, record exposed side wall height
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

filename = 'picture'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')












def checkEvents(events):
    tot = 0
    num = [0] * (10000 + 1 + 9999) # num[0] = # of coverage at loc: -10000
    for x, io, ym, yM in events:
        prev = copy(num)
        if io == 0:
            for y in range(ym+10000, yM+10000):
                num[y] += 1
        else:
            for y in range(ym+10000, yM+10000):
                num[y] -= 1

        for y in range(20000):
            if not prev[y] and num[y]:
                tot += 1
            elif prev[y] and not num[y]:
                tot += 1

    return tot

N = int(input())
rects = []
for n in range(N):
    line = list(map(int, input().split()))
    rects.append(line)

# pre process

xevents = []
yevents = []
for xm, ym, xM, yM in rects:
    xevents.append([xm, 0, ym, yM]) # 0: into a rect
    xevents.append([xM, 1, ym, yM]) # 1: leaving a rect
    yevents.append([ym, 0, xm, xM])
    yevents.append([yM, 1, xm, xM])


xevents.sort()
yevents.sort()

totx = checkEvents(xevents)
toty = checkEvents(yevents)

printwrite(totx + toty)
















fin.close()
fout.close()
del print, input

