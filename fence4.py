"""
ID: wrwwctb1
LANG: PYTHON3
TASK: fence4
6.5.2

problem description ambiguous about "intersect"
is this an intersection?

    |
    |_____
    |
    |

turns out, for this problem, no

usaco sol has a different way of finding visible edges
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

filename = 'fence4'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










def outer(x1, y1, x2, y2):
    '''
    x2 y2
    ^
    |
    . --> x1 y1
    '''
    return x1 * y2 - y1 * x2

def intersect(f, g):
    fx1, fy1, fx2, fy2, fvx, fvy = f
    gx1, gy1, gx2, gy2, gvx, gvy = g
    return ((outer(fx1-gx1, fy1-gy1, gvx, gvy) *
             outer(fx2-gx1, fy2-gy1, gvx, gvy)) < 0 and
            (outer(gx1-fx1, gy1-fy1, fvx, fvy) *
             outer(gx2-fx1, gy2-fy1, fvx, fvy)) < 0)

def isSimple(edges):
    N = len(edges)
    for i in range(3, N):
        start = i == N-1 # exclude i, j == N-1, 0
        for j in range(start, i-1):
            if intersect(edges[i], edges[j]):
                return False
    return True

def isCollinear(ox, oy, edge):
    x1, y1, x2, y2, vx, vy = edge
    ux = x1 - ox
    uy = y1 - oy
    return abs(vy * ux - vx * uy) < EPS_collinear # vy/vx == uy/ux

def innerPoints(edge):
    x1, y1, x2, y2, vx, vy = edge
    dx = vx * EPS_innerPoints
    dy = vy * EPS_innerPoints
    return x1 + dx, y1 + dy, x2 - dx, y2 - dy

def isVisible(ox, oy, i, edges):
    def clearView(edge):
        for j in range(len(edges)):
            if j == i:
                continue
            if intersect(edges[j], edge):
                return False
        return True

    if isCollinear(ox, oy, edges[i]):
        return False
    x3, y3, x4, y4 = innerPoints(edges[i])
    edgeo3 = ox, oy, x3, y3, x3-ox, y3-oy
    edgeo4 = ox, oy, x4, y4, x4-ox, y4-oy
    return clearView(edgeo3) or clearView(edgeo4)

EPS_innerPoints = 1e-6
EPS_collinear = 1e-6

N = int(input())
ox, oy = map(int, input().split())
xs = []
ys = []
for n in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

edges = []
for n in range(N-1):
    edges.append([xs[n], ys[n], xs[n+1], ys[n+1],
                  xs[n+1]-xs[n], ys[n+1]-ys[n]])
edges.append([xs[0], ys[0], xs[N-1], ys[N-1],
              xs[N-1]-xs[0], ys[N-1]-ys[0]])

ifsimple = isSimple(edges)

if ifsimple:
    visibleList = []
    for i in list(range(N-2)) + [N-1, N-2]:
        if isVisible(ox, oy, i, edges):
            visibleList.append(i)
    printwrite(len(visibleList))
    for i in visibleList:
        printwrite('%d %d %d %d' % tuple(edges[i][:4]))
else:
    printwrite('NOFENCE')


#import matplotlib.pyplot as pl
#for x1, y1, x2, y2, _, _ in edges:
#    pl.plot([x1, x2], [y1, y2])
#pl.plot(ox, oy, 'x')










fin.close()
fout.close()
del print, input

