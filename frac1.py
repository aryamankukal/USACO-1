"""
ID: wrwwctb1
LANG: PYTHON3
TASK: frac1
2.1.4
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

filename = 'frac1'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')






# import fractions # not allowed

N = int(input())
st = set()
for n in range(1, N+1):
    for i in range(n+1):
        g = gcd(i, n)
        st.add((i//g, n//g))
ls = sorted(st, key=lambda a: a[0]/a[1])
for i, n in ls:
    printwrite('%d/%d' % (i, n))




fin.close()
fout.close()
del print, input

