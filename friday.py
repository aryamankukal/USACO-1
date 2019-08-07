"""
ID: wrwwctb1
LANG: PYTHON3
TASK: friday
1.2.6
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

filename = 'friday'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')




def isleap(yr):
    if yr % 400 == 0:
        return True
    elif yr % 100 == 0:
        return False
    elif yr % 4 == 0:
        return True
    else:
        return False

def numdays(yr):
    if isleap(yr):
        return 366
    else:
        return 365

def plaindays13th(yr):
    ls = [13, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    if isleap(yr):
        ls[2] = 29
    return list(accumulate(ls))

N = int(input())
daysInPrevYrs = 0
ans = [0] * 7
for yr in range(1900, 1900 + N):
    plaindays = plaindays13th(yr)
    for i in range(12):
        plaindays[i] += daysInPrevYrs + 1 # 01/01/1900 is a Monday, %7 == 2
        ans[plaindays[i] % 7] += 1
    daysInPrevYrs += numdays(yr)


printwrite(' '.join(map(str, ans)))





fin.close()
fout.close()
del print, input

