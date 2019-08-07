"""
ID: wrwwctb1
LANG: PYTHON3
TASK: fracdec
2.4.6

point 1/1:

    the following function works. it can generate >1 outputs at one call

    does it suit our need?


def step(n, d):
    # n < d
    out = []
    n *= 10
    while n < d:
        n *= 10
        out.append(0)
    o, n = divmod(n, d)
    out.append(o)
    return out, n
"""

import os, sys, re, itertools, functools
from collections import Counter, deque, defaultdict
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key
from heapq import heappush, heappop, nlargest, nsmallest
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
         pi, sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip('\n')

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'fracdec'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









def step(n, d):
    '''
    n < d
    '''
    n *= 10
    if n < d:
        return 0, n
    else:
        return divmod(n, d)

#for n, d in [(1,3),(22,5),(1,7),(2,2),(3,8),(45,56),(1243,56),(884279719003555, 281474976710656),
#             (100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
#              999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)]:
n, d = map(int, input().split())

ipart, n = divmod(n, d)

seen = {}
outs = []

while True:
    if (n, d) in seen:
        break
    if n == 0:
        break
    seen[n, d] = len(outs)
    out, n = step(n, d)
    outs.append(out)

outs = list(map(str, outs))
if n == 0:
    # complete division, which might mean integer
    if len(outs) == 0:
        outs = ['0']
else:
    outs.insert(seen[n, d], '(')
    outs.append(')')

outs = ''.join(outs)


toprint = '%d.%s' % (ipart, outs)

#printwrite(toprint)

curr = 0
while curr < len(toprint):
    printwrite(toprint[curr:curr+76])
    curr += 76








fin.close()
fout.close()
del print, input

