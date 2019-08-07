"""
ID: wrwwctb1
LANG: PYTHON3
TASK: rect1
6.2.3

review

sys.setrecursionlimit() useful for the first time

similar to window.py
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
sys.setrecursionlimit(5782)
# python -m cProfile -s time ha.py

print = functools_partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'rect1'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










def crop(wa, wb):
    '''
    crop window a by window b
    return non degenerate windows

    .................
    .    .    .     .
    .    . 4  .     .
    .    ......     .
    .    .    .     .
    . 1  .    .  3  .
    .    ......     .
    .    .    .     .
    .    . 2  .     .
    .................

    '''
    ax, aX, ay, aY, ac = wa
    bx, bX, by, bY, bc = wb
    if (bX <= ax or aX <= bx or # not overlapped at all
        bY <= ay or aY <= by):
        return [wa]

    out = []

    if ax < bx and bx <= aX: # 1
        out.append([ax, bx, ay, aY, ac])

    if ax <= bX and bX < aX: # 3
        out.append([bX, aX, ay, aY, ac])

    x = max(ax, bx)
    X = min(aX, bX)

    if ay < by and by <= aY: # 2
        out.append([x, X, ay, by, ac])

    if ay <= bY and bY < aY: # 4
        out.append([x, X, bY, aY, ac])

    return out


def recursiveCrop(base, onTop, progress):
    if progress == len(onTop):
        x, X, y, Y, c = base
        return (X-x) * (Y-y)
    allCropped = crop(base, onTop[progress])
    tot = 0
    for cropped in allCropped:
        tot += recursiveCrop(cropped, onTop, progress+1)
    return tot



A, B, N = map(int, input().split())

wins = [[0, A, 0, B, 1]]
for n in range(N):
    x, y, X, Y, c = map(int, input().split())
    wins.append([x, X, y, Y, c]) # note format is mx Mx my My c

areas = Counter()

for i in range(N+1):
    base = wins[i]
    tot = recursiveCrop(base, wins, i+1)
    areas[base[-1]] += tot

out = []
for key, val in areas.items():
    if val > 0:
        out.append([key, val])

out.sort()
for key, val in out:
    printwrite('%d %d' % (key, val))











fin.close()
fout.close()
del print, input

