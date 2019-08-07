"""
ID: wrwwctb1
LANG: PYTHON3
TASK: palsquare
1.3.5
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

filename = 'palsquare'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')






def changebases(n, B):
    out = []
    while n > 0:
        n, rem = divmod(n, B)
        out.append(rem)
    return out[::-1]


def tostr(nB):
    out = []
    for dig in nB:
        out.append('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[dig])
    return ''.join(out)


B = int(input())
for n in range(1, 301):
    n2 = n * n
    n2B = changebases(n2, B)
    if n2B == n2B[::-1]:
        nB = changebases(n, B)

        #print(tostr(nB), tostr(n2B))
        printwrite('%s %s' % (tostr(nB), tostr(n2B)))





fin.close()
fout.close()
del print, input

