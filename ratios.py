"""
ID: wrwwctb1
LANG: PYTHON3
TASK: ratios
3.2.5

key idea
matrix inverse and multiplication. check if any integral multiple of the result can be integral

brute force doesn't work here, might work in c++
but neither solution sheds light on general integer-vector-composition problems
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

filename = 'ratios'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









# geometry

def det(a):
    return + a[0][0] * a[1][1] * a[2][2] \
           + a[1][0] * a[2][1] * a[0][2] \
           + a[2][0] * a[0][1] * a[1][2] \
           - a[0][0] * a[2][1] * a[1][2] \
           - a[2][0] * a[1][1] * a[0][2] \
           - a[1][0] * a[0][1] * a[2][2]

def inv(a):
    d = det(a)
    b = [[(a[1][1] * a[2][2] - a[1][2] * a[2][1]) / d,
          (a[0][2] * a[2][1] - a[0][1] * a[2][2]) / d,
          (a[0][1] * a[1][2] - a[0][2] * a[1][1]) / d],
         [(a[1][2] * a[2][0] - a[1][0] * a[2][2]) / d,
          (a[0][0] * a[2][2] - a[0][2] * a[2][0]) / d,
          (a[0][2] * a[1][0] - a[0][0] * a[1][2]) / d],
         [(a[1][0] * a[2][1] - a[1][1] * a[2][0]) / d,
          (a[0][1] * a[2][0] - a[0][0] * a[2][1]) / d,
          (a[0][0] * a[1][1] - a[0][1] * a[1][0]) / d]]
    return b

def multmat(a, b):
    m = len(a)
    n = len(a[0])
    assert len(b) == n
    p = len(b[0])
    c = [[0] * p for i in range(m)]
    for i in range(m):
        for j in range(p):
            c[i][j] = sum([a[i][k] * b[k][j] for k in range(n)])
    return c

def multv(x, a):
    m = len(a)
    assert len(x) == m
    n = len(a[0])
    out = [0] * n
    for j in range(n):
        out[j] = sum([x[i] * a[i][j] for i in range(m)])
    return out

def multc(c, x):
    out = []
    for i in x:
        out.append(c * i)
    return out

def add(x, y):
    n = len(x)
    assert len(y) == n
    return [x[i] + y[i] for i in range(n)]

x = list(map(int, input().split()))
a = []
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))


maxs = add(add(multc(99, a[0]), multc(99, a[1])), multc(99, a[2]))
ia = inv(a) # assume invertible. sol might exist even if a is not full rank
ratio = multv(x, ia)

EPS = 1e-6

flag = False

if ratio[0] < -EPS or ratio[1] < -EPS or ratio[2] < -EPS: # negaive ratio
    pass
else:
    # can ratio be all integers?
    cnt = 1
    curr = copy(ratio)

    while True:
        if curr[0] > maxs[0] or curr[1] > maxs[1] or curr[2] > maxs[2]:
            break
        if abs(round(curr[0]) - curr[0]) < EPS and \
           abs(round(curr[1]) - curr[1]) < EPS and \
           abs(round(curr[2]) - curr[2]) < EPS:
            flag = True
            break
        curr = add(curr, ratio)
        cnt += 1

if flag:
    printwrite('%d %d %d %d' % (round(curr[0]),
                                round(curr[1]),
                                round(curr[2]),
                                cnt))
else:
    printwrite('NONE')




fin.close()
fout.close()
del print, input

