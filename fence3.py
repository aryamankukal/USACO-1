"""
ID: wrwwctb1
LANG: PYTHON3
TASK: fence3
6.4.2

review

convex optimization

dist of a point to a line segment, parameter clamping


.py1 mistook that a fence wouldn't need a wire if electricity can go to the
target point via other fences. more difficult more fun. but is it convex?
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

filename = 'fence3'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








def p2f(px, py, f):
    fx1, fy1, fx2, fy2, fvx, fvy, fl = f
    if fl == 0:
        return hypot(px - fx1, py - fy1)
    else:
        t = ((px - fx1) * fvx + (py - fy1) * fvy) / (fl * fl)
        t = max(0, min(1, t)) # clamp
        projx = fx1 + t * fvx
        projy = fy1 + t * fvy
        return hypot(px - projx, py - projy)


def totdist(ox, oy, fences):
    tot = 0
    for fence in fences:
        tot += p2f(ox, oy, fence)
    return tot


from random import random

F = int(input())
fences = []
totx = 0
toty = 0
for f in range(F):
    x1, y1, x2, y2 = map(int, input().split())
    vx = x2 - x1
    vy = y2 - y1
    length = hypot(vx, vy)
    fences.append((x1, y1, x2, y2, vx, vy, length))
    totx += x1 + x2
    toty += y1 + y2


# solver
ox = totx / 2/F
oy = toty / 2/F
prevd = inf
best = inf
bestx = inf
besty = inf

lr = 1
dx = dy = 1e-1

history = []

for i in range(100):
    history.append((ox, oy))
    currd = totdist(ox, oy, fences)
#    print('% .3f '*3 % (ox, oy, currd))

    if currd < best:
        best = currd
        bestx = ox
        besty = oy

#    if abs(currd - prevd) < 1e-3:
#        break

    prevd = currd

    th = random() * 2 * pi
    dux =  dx * cos(th)
    duy =  dx * sin(th)
    dvx = -dy * sin(th)
    dvy =  dy * cos(th)

    pertu = totdist(ox+dux, oy+duy, fences)
    pertv = totdist(ox+dvx, oy+dvy, fences)

    gu = pertu - currd
    gv = pertv - currd

    gx = gu * cos(th) - gv * sin(th)
    gy = gu * sin(th) + gv * cos(th)

    ox -= gx * lr
    oy -= gy * lr

print(bestx, besty, best)
printwrite('%.1f %.1f %.1f' % (bestx, besty, best))


# visualization

#import matplotlib.pyplot as pl
#import numpy as np
#NN = 101
#xx = np.linspace(0, 2, NN)
#yy = np.linspace(0, 3, NN)
#XX, YY = np.meshgrid(xx, yy)
#ZZ = np.zeros_like(XX)
#for i in range(XX.shape[0]):
#    for j in range(XX.shape[1]):
#        ZZ[i][j] = totdist(XX[i][j], YY[i][j], fences)
#pl.contourf(XX, YY, ZZ, 10)
#pl.axis('equal')
#for x1, y1, x2, y2, vx, vy, length in fences:
#    pl.plot([x1, x2], [y1, y2], '-x', linewidth=2)
#historyx, historyy = zip(*history)
#pl.plot(historyx, historyy, '-o')
#pl.plot(totx/2/F, toty/2/F, 'x')


fin.close()
fout.close()
del print, input

