"""
ID: wrwwctb1
LANG: PYTHON3
TASK: msquare
3.2.6
bfs. remember visited nodes. remembering entire hist at every step is fine
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

filename = 'msquare'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')




def A(a):
    return a[::-1]

def B(a):
    return a[3], a[0], a[1], a[2], a[5], a[6], a[7], a[4]

def C(a):
    return a[0], a[6], a[1], a[3], a[4], a[2], a[5], a[7]

def bfs(curr, goal):
    dq = deque()
    dq.append([curr, []])
    seen = set()
    seen.add(curr)
    while len(dq) > 0:
        curr, hist = dq.popleft()
        if curr == goal:
            return hist
        aa = A(curr)
        bb = B(curr)
        cc = C(curr)
        if aa not in seen:
            dq.append([aa, hist+['A']])
            seen.add(aa)
        if bb not in seen:
            dq.append([bb, hist+['B']])
            seen.add(bb)
        if cc not in seen:
            dq.append([cc, hist+['C']])
            seen.add(cc)
    assert False

goal = tuple(map(int, input().split()))

curr = 1, 2, 3, 4, 5, 6, 7, 8

ans = bfs(curr, goal)
printwrite(len(ans))
towrite = []
i = 0
while True:
    if i >= len(ans):
        break
    towrite.append(''.join(ans[i:i+60]))
    i += 60
printwrite('\n'.join(towrite))






fin.close()
fout.close()
del print, input

