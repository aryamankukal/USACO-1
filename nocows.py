"""
ID: wrwwctb1
LANG: PYTHON3
TASK: nocows
2.3.2

key idea
top-down dp with memoization
consider two tree counts
a[n][k]: n and k fixed
b[n][k]: n fixed, but height <= k
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

filename = 'nocows'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








@lru_cache(maxsize=None)
def afun(n, k):
    '''
    a[n,k]: ans
    '''
    if n % 2 == 0:
        return 0
    if 2*k-1 > n or n > 2**k-1:
        return 0
    if n == 1 and k == 1:
        return 1
    out = 0
    for i in range(2*k-3, n, 2):
        out += afun(i, k-1) * afun(n-1-i, k-1) + \
               afun(i, k-1) * bfun(n-1-i, k-2) * 2
    return out

@lru_cache(maxsize=None)
def bfun(n, k):
    '''
    b[n,k]: n nodes, height <= k
    '''
    if n > 2**k-1:
        return 0
    if n == 1 and k == 1:
        return 1
    return afun(n, k) + bfun(n, k-1)

N, K = map(int, input().split())

ans = afun(N, K)

printwrite(ans % 9901)







fin.close()
fout.close()
del print, input

