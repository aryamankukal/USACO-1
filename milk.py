"""
ID: wrwwctb1
LANG: PYTHON3
TASK: milk
1.4.2
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

filename = 'milk'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')








N, M = list(map(int, input().split()))
PA = []
for m in range(M):
    PA.append(list(map(int, input().split())))

PA.sort()

spent = 0
has = 0
for p, a in PA:
    if has + a <= N:
        has += a
        spent += p * a
    else:
        delta =  N - has
        has = N
        spent += p * delta
        break

printwrite(spent)


fin.close()
fout.close()
del print, input

