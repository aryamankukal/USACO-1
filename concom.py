"""
ID: wrwwctb1
LANG: PYTHON3
TASK: concom
2.3.5

key idea
iteratively find controllable companies/shares
for each company, given a list of shares owned, which companies can be controlled?
                          |     ^
                          |     |
                          v     |
for each company, given a list of companies owned, can they contribute to shares owned?

must follow: understanding -> unambiguous solution -> implementation
"""

import os, sys, re, itertools, functools, heapq
from collections import Counter, deque
from copy import copy
from itertools import combinations, permutations, accumulate, \
                      combinations_with_replacement
from functools import lru_cache, cmp_to_key
from bisect import bisect_left, bisect_right
from math import ceil, floor, factorial, gcd, modf, log, log2, log10, sqrt, \
             sin, cos, tan, asin, acos, atan, atan2, hypot, erf, erfc, inf, nan
# sys.setrecursionlimit(5782)

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip()

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'concom'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')







def pall():
    for i in range(N1):
        print(own[i][:N1])
    print('')
    for i in range(N1):
        print(control[i][:N1])
    print('')

def updatecontrol(control, own, i, N1):
    '''
    for company i, given own[i], check companies controled by i
    return newly controled
    '''
    out = []
    for j in range(N1):
        if own[i][j] > 50 and control[i][j] != 1:
            control[i][j] = 1
            out.append(j)
    return out

def updateindown(newlycontrolled, own, i, N1):
    '''
    for company i, given newlycontrolled, update own[i]
    '''
    for j in newlycontrolled:
        for k in range(N1):
            own[i][k] += own[j][k]


N1 = NCOM1 = 101 # max # of companies + 1
n = int(input()) # # of lines
own = [[0] * N1 for _ in range(N1)] # owned shares, dir or indir
for _ in range(n):
    i, j, p = map(int, input().split())
    own[i][j] = p


control = [[0] * N1 for _ in range(N1)] # 0: no control. 1: control

for i in range(N1):
    while True:
        newlycontrolled = updatecontrol(control, own, i, N1)
        if len(newlycontrolled) == 0:
            break
        updateindown(newlycontrolled, own, i, N1)

for i in range(N1):
    for j in range(N1):
        if i != j and control[i][j]:
            printwrite('%d %d' % (i, j))








fin.close()
fout.close()
del print, input

