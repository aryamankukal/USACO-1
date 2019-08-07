"""
ID: wrwwctb1
LANG: PYTHON3
TASK: window
5.3.3

point 1/2:

constant time w, t, b, d
for s:
    gather windows on top: linear time
    calc: exponential on #windows. branch~4

room for improvement?

point 2/2: crop logic. rule out non-overlapping cases first
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

filename = 'window'
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
    al, ax, aX, ay, aY = wa
    bl, bx, bX, by, bY = wb
    if (bX <= ax or aX <= bx or # not overlapped at all
        bY <= ay or aY <= by):
        return [wa]

    out = []

    if ax < bx and bx <= aX: # 1
        out.append([al, ax, bx, ay, aY])

    if ax <= bX and bX < aX: # 3
        out.append([al, bX, aX, ay, aY])

    x = max(ax, bx)
    X = min(aX, bX)

    if ay < by and by <= aY: # 2
        out.append([al, x, X, ay, by])

    if ay <= bY and bY < aY: # 4
        out.append([al, x, X, bY, aY])

    return out


def recursiveCrop(base, onTop, progress):
    # pass index (progress) instead of onTop[progress:] to save memory
    if progress == len(onTop):
        _, x, X, y, Y = base
        return (X-x) * (Y-y)
    allCropped = crop(base, onTop[progress])
    tot = 0
    for cropped in allCropped:
        tot += recursiveCrop(cropped, onTop, progress+1)
    return tot



top = None
bot = None
wins = {}
while True:
    line = input()
    if line == '':
        break
    op = line[0]
    ID = line[2]
#    print(op, ID)

    if op == 'w':
        x, y, X, Y = map(int, line[4:-1].split(','))

        if top == None:
            bot = top = loc = 0
        else:
            top += 1
            loc = top

        wins[ID] = [loc,
                   min(x, X), max(x, X),
                   min(y, Y), max(y, Y)]

    elif op == 't':
        top += 1
        wins[ID][0] = top

    elif op == 'b':
        bot -= 1
        wins[ID][0] = bot

    elif op == 'd':
        del wins[ID]

    else: # 's'
        # find all that's on top of wi
        base = wins[ID]
        onTop = []
        for win in wins.values():
            if base[0] < win[0]:
                onTop.append(win)

        # crop
        ansArea = recursiveCrop(base, onTop, 0)
        _, x, X, y, Y = base
        ans = ansArea / ((X-x) * (Y-y)) * 100
        printwrite('%.3f' % ans)














fin.close()
fout.close()
del print, input

