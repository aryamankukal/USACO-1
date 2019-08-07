"""
ID: wrwwctb1
LANG: PYTHON3
TASK: combo
1.4.6
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

filename = 'combo'
fin = open(filename + '.in', 'r')
fout = open(filename + '.out', 'w')









def isnear(n1, n2, N):
    delta = abs(n1 - n2)
    return delta <= 2 or delta >= N - 2




N = int(input())
john = list(map(int, input().split()))
mast = list(map(int, input().split()))

cnt = 0

for i in range(1, N+1):
    jflag0 = isnear(i, john[0], N)
    mflag0 = isnear(i, mast[0], N)
    if not (jflag0 or mflag0):
        continue
    for j in range(1, N+1):
        jflag1 = isnear(j, john[1], N)
        mflag1 = isnear(j, mast[1], N)
        if not ((jflag0 and jflag1) or (mflag0 and mflag1)):
            continue
        for k in range(1, N+1):
            jflag2 = isnear(k, john[2], N)
            mflag2 = isnear(k, mast[2], N)
            if (jflag0 and jflag1 and jflag2) or \
               (mflag0 and mflag1 and mflag2):
                   cnt += 1


printwrite(cnt)





fin.close()
fout.close()
del print, input

