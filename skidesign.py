"""
ID: wrwwctb1
LANG: PYTHON3
TASK: skidesign
1.4.8
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

print = functools.partial(print, flush=True)
input = lambda: fin.readline().strip()

def printwrite(string):
    print(string)
    fout.write(str(string) + '\n')

filename = 'skidesign'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')





N = int(input())
hills = []
for n in range(N):
    hills.append(int(input()))

bestcost = inf
for finalmin in range(101-17):
    finalmax = finalmin + 17
    candcost = 0
    for hill in hills:
        if hill < finalmin:
            candcost += (finalmin - hill) ** 2
        elif hill > finalmax:
            candcost += (hill - finalmax) ** 2
    bestcost = min(bestcost, candcost)
printwrite(bestcost)




fin.close()
fout.close()
del print, input

