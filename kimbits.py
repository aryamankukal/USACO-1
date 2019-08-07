"""
ID: wrwwctb1
LANG: PYTHON3
TASK: kimbits
3.2.3

key idea
consider counting leaves of a tree
the thing dp'ed is not directly the ans
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

filename = 'kimbits'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








@lru_cache(maxsize=None)
def num(n, l):
    if n == l:
        return 2**n
    if l == 0:
        return 1
    return num(n-1, l) + num(n-1, l-1)


def genbits(n, l, i, out):
    if n == l:
        i -= 1
        i = bin(i)[2:]
        i = '0' * (n - len(i)) + i
        out.append(i)
        return
    if l == 0:
        # i == 1
        out.append('0' * n)
        return
    thresh = num(n-1, l)
    if i <= thresh:
        out.append('0')
        genbits(n-1, l, i, out)
    else:
        out.append('1')
        genbits(n-1, l-1, i-thresh, out)

N, L, I = map(int, input().split())



out = []
genbits(N, L, I, out)
printwrite(''.join(out))









fin.close()
fout.close()
del print, input

