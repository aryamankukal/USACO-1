"""
ID: wrwwctb1
LANG: PYTHON3
TASK: calfflac
6.2.1

review

turns out length of palindrome is a key.. no need for 2d dp
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

filename = 'calfflac'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')
















rawString = fin.read()

chars = []
oldLoc = []
for i, c in enumerate(rawString):
    if c.isalpha():
        chars.append(c.lower())
        oldLoc.append(i)


N = len(chars)

isp = [[True ] * N, # isp = ispalindrome
       [False] * N,
       [False] * N]
if N > 0:
    best = 1
else:
    best = 0
besti = 0
bestj = 0

d = 1 # j - i
l = 2 # j - i + 1
for i in range(N - d):
    j = i + d
    if chars[i] == chars[j]:
        isp[1][i] = True
        if best < l:
            best = l
            besti = i
            bestj = j
    else:
        isp[1][i] = False

#print('')

for d in range(2, N):
    l = d + 1
    currd = d % 3
    prevd = (d-2) % 3
    for i in range(N - d):
        j = i + d
#        print(chars[i], chars[j])
        if chars[i] == chars[j] and isp[prevd][i+1]:
            isp[currd][i] = True
            if best < l:
                best = l
                besti = i
                bestj = j
        else:
            isp[currd][i] = False

printwrite(best)
if best > 0:
    printwrite(rawString[oldLoc[besti]:oldLoc[bestj]+1])
else:
    printwrite('')














fin.close()
fout.close()
del print, input

