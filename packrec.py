"""
ID: wrwwctb1
LANG: PYTHON3
TASK: packrec
6.2.2

review
always work out the number of cases
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

filename = 'packrec'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')










def box(x1, x2, x3, x4, y1, y2, y3, y4, minArea, bestXYs):

    x = x1 + x2 + x3 + x4;
    y = max(y1, y2, y3, y4);
    minArea = update(x, y, minArea, bestXYs);

    x = max(x1, x2 + x3 + x4);
    y = y1 + max(y2, y3, y4);
    minArea = update(x, y, minArea, bestXYs);

    x = x1 + max(x2, x3 + x4);
    y = max(y1, y2 + max(y3, y4));
    minArea = update(x, y, minArea, bestXYs);

    x = x1 + x4 + max(x2, x3);
    y = max(y1, y4, y2 + y3);
    minArea = update(x, y, minArea, bestXYs);

    x = max(x1 + x2, x3 + x4, x1 + x4);
    y = max(y1 + y3, y2 + y4, y2 + y3);
    minArea = update(x, y, minArea, bestXYs);

    return minArea

def update(x, y, minArea, bestXYs):
    candArea = x * y
    if candArea < minArea:
        minArea = candArea
        bestXYs.clear()
        bestXYs.add((min(x, y), max(x, y)))
    elif candArea == minArea:
        bestXYs.add((min(x, y), max(x, y)))
    return minArea

xs = []
ys = []
for i in range(4):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)


minArea = inf
bestXYs = set()

for i, j, k, l in permutations([0, 1, 2, 3]):
    for swapi in [0, 1]:
        if swapi == 1:
            xs[i], ys[i] = ys[i], xs[i]

        for swapj in [0, 1]:
            if swapj == 1:
                xs[j], ys[j] = ys[j], xs[j]

            for swapk in [0, 1]:
                if swapk == 1:
                    xs[k], ys[k] = ys[k], xs[k]

                for swapl in [0, 1]:
                    if swapl == 1:
                        xs[l], ys[l] = ys[l], xs[l]

                    minArea = box(xs[i], xs[j], xs[k], xs[l],
                                  ys[i], ys[j], ys[k], ys[l],
                                  minArea, bestXYs)


                    if swapl == 1:
                        xs[l], ys[l] = ys[l], xs[l]


                if swapk == 1:
                    xs[k], ys[k] = ys[k], xs[k]
            if swapj == 1:
                xs[j], ys[j] = ys[j], xs[j]
        if swapi == 1:
            xs[i], ys[i] = ys[i], xs[i]


printwrite(minArea)
for x, y in sorted(bestXYs):
    printwrite('%d %d' % (x, y))









fin.close()
fout.close()
del print, input

